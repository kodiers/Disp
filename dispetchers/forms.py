#encoding=utf8
from django import forms
from dispetchers.models import Order, OrderOfferDetail, Offer, Worker
from django.forms.models import inlineformset_factory, BaseInlineFormSet

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['FactTime', 'FactTotalSumm', 'PlanTotalSumm']

class WorkerForm(forms.Form):
    # worker = forms.ModelChoiceField(queryset=Worker.objects.filter(IsBusy=False), empty_label=None, label='Рабочий')
    def __init__(self, *args, **kwargs):
        super(WorkerForm, self).__init__(*args, **kwargs)

class AddOfferForm(forms.Form):
    offer = forms.ModelChoiceField(queryset=Offer.objects.all(), empty_label=None, label='Услуга')
    addOneMore = forms.BooleanField(initial=False, label='Добавить еще услугу')
    def __init__(self, *args, **kwargs):
        super(AddOfferForm, self).__init__(*args, **kwargs)

# class OrderOfferDetailForm(forms.ModelForm):
#     worker = forms.ModelChoiceField(queryset=Worker.objects.filter(IsBusy=False))
#     class Meta:
#         model = OrderOfferDetail

class CustomInlineFormset(BaseInlineFormSet):
    #TODO: add method to check offer and worker category
    def clean(self):
        super(CustomInlineFormset, self).clean()
        if any(self.errors):
            return
        workers = []
        offers = []
        for form in self.forms:
            workers.append(form.cleaned_data['Worker'])
            offers.append(form.cleaned_data['OfferName'])
            for worker in workers:
                for offer in offers:
                    if worker.WorkerCategory != offer.OfferCategory:
                        msg = 'Offer category not equal worker category'
                        self.add_error('Worker', msg)
                        self.add_error('OfferName', msg)


OrderOfferFormset = inlineformset_factory(Order, OrderOfferDetail, can_delete=False, exclude=['FactWorkedHours'], formset=CustomInlineFormset)
