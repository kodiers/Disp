from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Disp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'dispetchers.views.show_orders', name="index"),
    # url(r'createorder/$', 'dispetchers.views.create_order', name="create_order"),
    # url(r'addoffer/$', 'dispetchers.views.add_offer', name="add_offer"),
    # url(r'addworker/$', 'dispetchers.views.add_worker', name="add_worker"),
    # url(r'^add_order_class/$', OrderCreateView.as_view(), name="add_order_class"),
    url(r'^create_order_detail/$', 'dispetchers.views.create_order_detail', name='create_order_detail'),
    url(r'^admin/', include(admin.site.urls)),
)
