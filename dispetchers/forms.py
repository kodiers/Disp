#encoding=utf8
from django import forms
from dispetchers.models import Order, OrderOfferDetail, Offer, Worker
from django.forms.models import inlineformset_factory, BaseInlineFormSet

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['FactTime', 'FactTotalSumm', 'PlanTotalSumm']

# TODO: old code - need to be deleted
# class WorkerForm(forms.Form):
#     # worker = forms.ModelChoiceField(queryset=Worker.objects.filter(IsBusy=False), empty_label=None, label='Рабочий')
#     def __init__(self, *args, **kwargs):
#         super(WorkerForm, self).__init__(*args, **kwargs)
#
# class AddOfferForm(forms.Form):
#     offer = forms.ModelChoiceField(queryset=Offer.objects.all(), empty_label=None, label='Услуга')
#     addOneMore = forms.BooleanField(initial=False, label='Добавить еще услугу')
#     def __init__(self, *args, **kwargs):
#         super(AddOfferForm, self).__init__(*args, **kwargs)

# class OrderOfferDetailForm(forms.ModelForm):
#     worker = forms.ModelChoiceField(queryset=Worker.objects.filter(IsBusy=False))
#     class Meta:
#         model = OrderOfferDetail

class OfferDetailInlineFormset(BaseInlineFormSet):
    #TODO: add method to check offer and worker category
    def clean(self):
        super(OfferDetailInlineFormset, self).clean()
        if any(self.errors):
            return
        for form in self.forms:
            worker1 = form.cleaned_data.get('Worker', None)
            offer1 = form.cleaned_data.get('OfferName', None)
            if worker1 != None and offer1 != None:
                if worker1.WorkerCategory != offer1.OfferCategory:
                    raise forms.ValidationError('Категория услуги не соответсвует категории рабочего')


OrderOfferFormset = inlineformset_factory(Order, OrderOfferDetail, can_delete=False, exclude=['FactWorkedHours'], formset=OfferDetailInlineFormset)
