from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
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
        if request.POST["offer"] != None:
            offer = Offer.objects.get(pk=request.POST["offer"])
            offers.append(offer)
    form = OrderForm()
    return render_to_response('create_order.html', {'form':form, 'offers':offers}, context_instance=RequestContext(request))

def add_offer(request):
    form = AddOfferForm()
    workers = Worker.objects.filter(IsBusy=False)
    return render_to_response('add_offer.html', {'form':form, 'workers':workers}, context_instance=RequestContext(request))
