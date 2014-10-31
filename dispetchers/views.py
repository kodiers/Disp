#encoding=utf-8
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404, redirect
from dispetchers.models import Order, OrderOfferDetail, Worker, Offer, Category, WorkerHours
from django.http import Http404, HttpResponse, HttpResponseNotFound
from dispetchers.forms import OrderForm, OrderOfferFormset, EditOrderForm, EditOrderOfferFormset
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView
from django import forms
import datetime

# Create your views here.
def show_orders(request):
    '''Show all orders'''
    orders = Order.objects.all()
    if orders != None:
        return render_to_response('index.html', {'orders':orders})
    else:
        return render_to_response('index.html')

def create_order_detail(request, order_id=None):
    '''Create order view.
    Check all forms and formset and calculate plan summ'''
    if order_id:
        order = Order.objects.get(id=order_id)
    else:
        order = Order()
    if request.method == 'POST':
        order_form = OrderForm(request.POST, instance=order)
        orderdetail_formset = OrderOfferFormset(request.POST, instance=order)
        if order_form.is_valid() and orderdetail_formset.is_valid():
            r = order_form.save()
            # Claculate plan summ
            plansumm = 0
            for form in orderdetail_formset:
                offer = form.cleaned_data.get('OfferName', None)
                worker = form.cleaned_data.get('Worker', None)
                if offer != None:
                    plansumm += offer.OfferPrice
                # Set busy time for worker
                # TODO: Recreate logic to check time
                if worker != None:
                    workerhours = WorkerHours()
                    existing_wh = WorkerHours.objects.filter(busyStartTime=r.PrefferedTime).filter(worker=worker.id)
                    if existing_wh.exists():
                    # if existing_wh != None:
                        raise forms.ValidationError(_('Worker %(worker)s is busy on %(time)s'), params={'worker':worker, 'time':r.PrefferedTime.strftime('%Y-%m-%d %H:%M')})
                        # TODO: don't work if meassage is Russian
                        # raise forms.ValidationError('Рабочий %s уже занят во время %s' % (worker, r.PrefferedTime.strftime('%Y-%m-%d %H:%M')))
                    workerhours.worker = Worker.objects.get(id=worker.id)
                    workerhours.busyStartTime = r.PrefferedTime
                    workerhours.busyEndTime = r.PrefferedTime + datetime.timedelta(seconds=(offer.Duration * 3600))
                    workerhours.save()
            r.PlanTotalSumm = plansumm
            orderdetail_formset.save()
            r.save()
            return redirect('index')
    else:
        order_form = OrderForm(instance=order)
        orderdetail_formset = OrderOfferFormset(instance=order)
    return render_to_response('create_order_detail.html',
                              {'order_form':order_form, 'orderdetail_formset':orderdetail_formset},
                              context_instance=RequestContext(request))

def edit_order(request, order_id=None):
    '''Edit order view
    Use create_order_template.html'''
    # TODO: similar code to create_order_detail view. Need some enhancement
    order = None
    if order_id:
        order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        order_form = EditOrderForm(request.POST, instance=order)
        orderdetail_formset = EditOrderOfferFormset(request.POST, instance=order)
        if order_form.is_valid() and orderdetail_formset.is_valid():
            r = order_form.save(commit=False)
            orderdetail_formset.save()
            r.save()
            return redirect('index')
    else:
        order_form = EditOrderForm(instance=order)
        orderdetail_formset = EditOrderOfferFormset(instance=order)
    return render_to_response('create_order_detail.html',
                              {'order_form':order_form, 'orderdetail_formset':orderdetail_formset},
                              context_instance=RequestContext(request))