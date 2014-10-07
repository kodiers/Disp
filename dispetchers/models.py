# encoding=utf8
from django.db import models
from django.utils import timezone
from datetime import datetime

ORDERSTATUS = (
    ('NEW', 'Новая'),
    ('SET', 'Назначена'),
    ('INPROGRESS', 'В работе'),
    ('COMPLETED', 'Выполнена'),
)

# Create your models here.
class Category(models.Model):
    '''Categories for offers'''
    CategoryName = models.CharField(max_length=30, verbose_name='Имя категории')
    def __unicode__(self):
        return self.CategoryName
    def __str__(self):
        return self.CategoryName
    class Meta:
        verbose_name_plural = 'Категории'

class Offer(models.Model):
    '''Offers'''
    OfferName = models.CharField(max_length=150, verbose_name='Название услуги')
    OfferCategory = models.ForeignKey(Category, verbose_name='Категория')
    OfferPrice = models.FloatField(verbose_name='Стоимость')
    def __unicode__(self):
        return self.OfferName
    def __str__(self):
        return self.OfferName
    class Meta:
        verbose_name_plural = 'Услуги'

class Worker(models.Model):
    '''Workers'''
    FirstName = models.CharField(max_length=30, verbose_name='Имя')
    LastName = models.CharField(max_length=50, verbose_name='Фамилия')
    WorkerCategory = models.ForeignKey(Category, verbose_name='Категория')
    IsBusy = models.BooleanField(default=False, verbose_name='Занят')
    IsChief = models.BooleanField(default=False, verbose_name='Бригадир')
    def __unicode__(self):
        return self.LastName + ' ' + self.FirstName
    def __str__(self):
        return self.LastName + ' ' + self.FirstName
    class Meta:
        verbose_name_plural = 'Рабочие'

class Order(models.Model):
    '''Orders'''
    ClientName = models.CharField(max_length=150)
    ClientAddress = models.CharField(max_length=200)
    PrefferedTime = models.DateTimeField(default=datetime.now())
    FactTime = models.DateTimeField(null=True, blank=True)
    PlanTotalSumm = models.FloatField()
    FactTotalSumm = models.FloatField()
    Status = models.CharField(max_length=15, choices=ORDERSTATUS, default='New')
    class Meta:
        verbose_name_plural = 'Заявки'

class OrderOfferDetail(models.Model):
    OrderName = models.ForeignKey(Order)
    OfferName = models.ForeignKey(Offer)
    Worker = models.ForeignKey(Worker)
    FactWorkedHours= models.TimeField(null=True, blank=True)
    Comments = models.TextField()
    class Meta:
        verbose_name_plural = 'Детали заявки'




