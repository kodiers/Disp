from django import forms
from dispetchers.models import Order, OrderOfferDetail, Offer

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['FactTime', 'FactTotalSumm']

class AddOfferForm(forms.Form):
    offer = forms.ChoiceField()