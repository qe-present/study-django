from django.http import JsonResponse
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET
from . import models

# require_http_methods(['GET'])
@require_GET
def index(request: HttpRequest)->HttpResponse:
    name=request.GET.get('name')
    price=request.GET.get('price')
    description=request.GET.get('description')
    # 添加数据
    end=models.Goods.objects.create(name=name, price=price, description=description)
    if end is not None:
        return JsonResponse({
            'status': 200,
            'data': None,
            'message': '添加成功'
        })
    return JsonResponse({
        'status': 500,
        'data': None,
        'message': '添加失败'
    })
def show(request: HttpRequest)->HttpResponse:
    # 查询数据
    goods=models.Goods.objects.all()

    if goods is None:
        return JsonResponse({
            'status': 500,
            'data': None,
            'message': '查询失败'
        })
    data=[]
    for good in goods:
        data.append({
            'id': good.id,
            'name': good.name,
            'price': good.price,
            'description': good.description
        })
    return JsonResponse({
        'status': 200,
        'data': data,
        'message': '查询成功'
    })
@csrf_exempt
@require_http_methods(['POST'])
def index_post(request:HttpRequest)->JsonResponse:
    print(request.body)
    print(request.POST) # <QueryDict: {'params': ['123']}>
    print(request.POST.get('data')) # 123
    return JsonResponse({'status': 'ok'})