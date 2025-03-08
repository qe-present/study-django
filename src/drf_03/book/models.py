from django.db import models
from datetime import date
# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100,verbose_name='书名',unique=True)
    price=models.FloatField(verbose_name='价格',default=0)
    pub_date=models.DateField(verbose_name='出版日期',default=date.today)
    class Meta:
        verbose_name = '图书'
        verbose_name_plural = verbose_name
        db_table = 'books'




