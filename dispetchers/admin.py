from django.contrib import admin
from dispetchers.models import Category, Offer, Worker, Order, OrderOfferDetail, WorkerHours

# Register your models here.
admin.site.register(Category)
admin.site.register(Offer)
admin.site.register(Worker)
admin.site.register(Order)
admin.site.register(OrderOfferDetail)
admin.site.register(WorkerHours)

