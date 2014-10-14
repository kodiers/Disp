#encoding=utf8
from django import forms
from dispetchers.models import Order, OrderOfferDetail, Offer

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['FactTime', 'FactTotalSumm']

class AddOfferForm(forms.ModelForm):
    offer = forms.ModelChoiceField(queryset=Offer.objects.all(), empty_label=None, label='Услуга')
    def __init__(self, *args, **kwargs):
        super(AddOfferForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Offer
        exclude = ['OfferCategory', 'OfferPrice', 'OfferName']