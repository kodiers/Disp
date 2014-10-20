from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404, redirect
from dispetchers.models import Order, OrderOfferDetail, Worker, Offer, Category
from django.http import Http404, HttpResponse, HttpResponseNotFound
from dispetchers.forms import OrderForm, AddOfferForm, WorkerForm, OrderOfferFormset
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
def show_orders(request):
    orders = Order.objects.all()
    if orders != None:
        return render_to_response('index.html', {'orders':orders})
    else:
        return render_to_response('index.html')

def create_order(request):
    #TODO: old code - need to delete
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
    #TODO: old code - need to delete
    if request.method == 'POST':
        order = Order.objects.latest()
        if 'addOneMore' in request.POST:
            # Need some optimization
            orderoffers = OrderOfferDetail.objects.filter(OrderName=order.pk).values()
            actualoffers = []
            for o in orderoffers:
                actualoffer = Offer.objects.get(pk=o['OfferName_id'])
                actualoffers.append(actualoffer)
            form = AddOfferForm()
            # orderoffer = OrderOfferDetail()
            # orderoffer.OrderName = order
            # orderoffer.OfferName = Offer.objects.get(pk=request.POST['offer'])
            # orderoffer.save()
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
    #TODO: old code - need to delete
    # goto line 33
    order = Order.objects.latest()
    orderoffers = OrderOfferDetail.objects.filter(OrderName=order.pk)
    # workers = []
    # # for a in orderoffers:
    # #     category = Offer.objects.get(OfferName=a)
    # #     worker = Worker.objects.filter(WorkerCategory=category.OfferCategory)
    # #     worker_free = worker.exclude(IsBusy=True)
    # #     workers.append(worker_free)
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            for o in orderoffers:
                o.Worker = Worker.objects.get(pk=request.POST['worker'])
                o.save()
        return redirect('index')
    form = WorkerForm()
    return render_to_response('add_worker.html', {'actualoffers': orderoffers, 'form':form},
                              context_instance=RequestContext(request))


def create_order_detail(request, order_id=None):
    order = None
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

# Classes

class OrderCreateView(CreateView):
    #TODO: old code - need to delete
    model = Order
    template_name = "add_order_class.html"
    form_class = OrderOfferFormset
    def get_success_url(self):
        return self.get_object().get_absolute_url()