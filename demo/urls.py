from django.conf.urls.defaults import *
from demo.views import *

urlpatterns = patterns( '',
	url( r'^$', index, name = 'index' ),
	url( r'^search/$', search, name = 'search' ),
) 
