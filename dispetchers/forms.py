#encoding=utf8
from django import forms
from dispetchers.models import Order, OrderOfferDetail, Offer, Worker

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['FactTime', 'FactTotalSumm', 'PlanTotalSumm']

class WorkerForm(forms.Form):
    worker = forms.ModelChoiceField(queryset=Worker.objects.filter(IsBusy=False), empty_label=None, label='Рабочий')
    def __init__(self, *args, **kwargs):
        super(WorkerForm, self).__init__(*args, **kwargs)

class AddOfferForm(forms.Form):
    offer = forms.ModelChoiceField(queryset=Offer.objects.all(), empty_label=None, label='Услуга')
    addOneMore = forms.BooleanField(initial=False, label='Добавить еще услугу')
    def __init__(self, *args, **kwargs):
        super(AddOfferForm, self).__init__(*args, **kwargs)