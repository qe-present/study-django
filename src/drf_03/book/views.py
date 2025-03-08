from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import BookSerializer
from .models import Book

class BookListCreateView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookRetrieveUpdateDestroyView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    'message': '更新成功'
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
            data={
                'message': '更新失败'
            }
        )

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        res=book.delete()
        if res[0]:
            return Response(
                status=status.HTTP_200_OK,
                data={
                    'message': '删除成功'
                } )
        else:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={
                    'message': '删除失败'
                })
