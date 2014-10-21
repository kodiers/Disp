from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404, redirect
from dispetchers.models import Order, OrderOfferDetail, Worker, Offer, Category
from django.http import Http404, HttpResponse, HttpResponseNotFound
from dispetchers.forms import OrderForm, OrderOfferFormset
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
def show_orders(request):
    orders = Order.objects.all()
    if orders != None:
        return render_to_response('index.html', {'orders':orders})
    else:
        return render_to_response('index.html')

def create_order_detail(request, order_id=None):
    order = None
    # errors = None
    if order_id:
        order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order_form = OrderForm(request.POST, instance=order)
        orderdetail_formset = OrderOfferFormset(request.POST, instance=order)
        if order_form.is_valid() and orderdetail_formset.is_valid():
            r = order_form.save(commit=False)
            orderdetail_formset.save()
            r.save()
            return redirect('index')
    else:
        order_form = OrderForm(instance=order)
        orderdetail_formset = OrderOfferFormset(instance=order)
    return render_to_response('create_order_detail.html',
                              {'order_form':order_form, 'orderdetail_formset':orderdetail_formset},
                              context_instance=RequestContext(request))
