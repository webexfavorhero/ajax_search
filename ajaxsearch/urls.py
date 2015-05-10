from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from demo.views import *

urlpatterns = patterns('',
	url( r'^', include( 'demo.urls' ) ),
    url(r'^admin/', include(admin.site.urls)),   

)
