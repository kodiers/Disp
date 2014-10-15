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
    Duration = models.FloatField(verbose_name='Базовая длительность', null=True, default=1.0)
    def __unicode__(self):
        return self.OfferName
    def __str__(self):
        return self.OfferName
    class Meta:
        verbose_name_plural = 'Услуги'


class Order(models.Model):
    '''Orders'''
    ClientName = models.CharField(max_length=150, verbose_name='Имя клиента')
    ClientAddress = models.CharField(max_length=200, verbose_name='Адрес клиента')
    PrefferedTime = models.DateTimeField(default=datetime.now(), verbose_name='Предпочетаемое время')
    CreateTime = models.DateTimeField(default=datetime.now(), verbose_name='Дата создания')
    FactTime = models.DateTimeField(null=True, blank=True, verbose_name='Фактическое время')
    PlanTotalSumm = models.FloatField(verbose_name='Плановая стоимость', null=True)
    FactTotalSumm = models.FloatField(verbose_name='Фактическая стоимость', null=True)
    Status = models.CharField(max_length=15, choices=ORDERSTATUS, default='New', verbose_name='Статус')
    class Meta:
        verbose_name_plural = 'Заявки'
        get_latest_by = "CreateTime"

class Worker(models.Model):
    '''Workers'''
    FirstName = models.CharField(max_length=30, verbose_name='Имя')
    LastName = models.CharField(max_length=50, verbose_name='Фамилия')
    WorkerCategory = models.ForeignKey(Category, verbose_name='Категория')
    IsBusy = models.BooleanField(default=False, verbose_name='Занят')
    IsChief = models.BooleanField(default=False, verbose_name='Бригадир')
    Orders = models.ManyToManyField(Order, verbose_name='Заявки')
    def __unicode__(self):
        return self.LastName + ' ' + self.FirstName
    def __str__(self):
        return self.LastName + ' ' + self.FirstName
    class Meta:
        verbose_name_plural = 'Рабочие'

class OrderOfferDetail(models.Model):
    OrderName = models.ForeignKey(Order, null=True)
    OfferName = models.ForeignKey(Offer, null=True)
    Worker = models.ForeignKey(Worker, null=True)
    FactWorkedHours= models.TimeField(null=True, blank=True)
    Comments = models.TextField(null=True)
    class Meta:
        verbose_name_plural = 'Детали заявки'

class WorkerHours(models.Model):
    '''Worker's busy hours'''
    worker = models.ManyToManyField(Worker)
    busyStartTime = models.DateTimeField(null=True)
    busyEndTime = models.DateTimeField(null=True)


