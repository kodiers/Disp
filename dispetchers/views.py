from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from dispetchers.models import Order, OrderOfferDetail, Worker
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
    form = OrderForm()
    form2 = AddOfferForm()
    return render_to_response('create_order.html', {'form':form, 'form2':form2}, context_instance=RequestContext(request))
    #return HttpResponseNotFound("<h1>Page not found</h1>")
