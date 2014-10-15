from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404, redirect
from dispetchers.models import Order, OrderOfferDetail, Worker, Offer
from django.http import Http404, HttpResponse, HttpResponseNotFound
from dispetchers.forms import OrderForm, AddOfferForm
from django.template import RequestContext

# Create your views here.
def show_orders(request):
    orders = Order.objects.all()
    if orders != None:
        return render_to_response('index.html', {'orders':orders})
    else:
        return render_to_response('index.html')

def create_order(request):
    #TODO: create add offer
    offers = []
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_offer')
        else:
            return Http404
    form = OrderForm()
    return render_to_response('create_order.html', {'form':form, 'offers':offers}, context_instance=RequestContext(request))

def add_offer(request):
    #TODO: add workers and fix bug
    if request.method == 'POST':
        order = Order.objects.latest()
        if 'addOneMore' in request.POST:
            orderoffers = OrderOfferDetail.objects.filter(OrderName=order.pk).values()
            actualoffers = []
            for o in orderoffers:
                actualoffer = Offer.objects.get(pk=o['OfferName_id'])
                actualoffers.append(actualoffer)
            form = AddOfferForm()
            orderoffer = OrderOfferDetail()
            orderoffer.OrderName = order
            orderoffer.OfferName = Offer.objects.get(pk=request.POST['offer'])
            orderoffer.save()
            return render_to_response('add_offer.html', {'form':form, 'actualoffers':actualoffers}, context_instance=RequestContext(request))
        else:
            form = AddOfferForm()
            orderoffer = OrderOfferDetail()
            orderoffer.OrderName = order
            orderoffer.OfferName = Offer.objects.get(pk=request.POST['offer'])
            orderoffer.save()
            return redirect('add_worker')
    form = AddOfferForm()
    return render_to_response('add_offer.html', {'form':form}, context_instance=RequestContext(request))

def add_worker(request):
    #TODO: create add_worker view and template
    pass
