#encoding=utf8
from django import forms
from dispetchers.models import Order, OrderOfferDetail, Offer, Worker
from django.forms.models import inlineformset_factory, BaseInlineFormSet

class OrderForm(forms.ModelForm):
    '''Create order form class'''
    class Meta:
        model = Order
        exclude = ['FactTime', 'FactTotalSumm', 'PlanTotalSumm']

class EditOrderForm(forms.ModelForm):
    '''Edit order form'''
    class Meta:
        model = Order
        fields = '__all__'

class OfferDetailInlineFormset(BaseInlineFormSet):
    '''Class for define formset for attach offer to order'''
    def clean(self):
        '''Check that offer category is equal worker category'''
        super(OfferDetailInlineFormset, self).clean()
        if any(self.errors):
            return
        for form in self.forms:
            worker = form.cleaned_data.get('Worker', None)
            offer = form.cleaned_data.get('OfferName', None)
            if worker != None and offer != None:
                if worker.WorkerCategory != offer.OfferCategory:
                    raise forms.ValidationError('Категория услуги не соответсвует категории рабочего')
        return self.cleaned_data


OrderOfferFormset = inlineformset_factory(Order, OrderOfferDetail, can_delete=False, exclude=['FactWorkedHours'], formset=OfferDetailInlineFormset) # Define formset instance ( add extra=N to show N forms)
EditOrderOfferFormset = inlineformset_factory(Order, OrderOfferDetail, formset=OfferDetailInlineFormset, fields='__all__')