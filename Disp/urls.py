from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Disp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'dispetchers.views.show_orders', name="index"),
    url(r'createorder/$', 'dispetchers.views.create_order', name="create_order"),

    url(r'^admin/', include(admin.site.urls)),
)
