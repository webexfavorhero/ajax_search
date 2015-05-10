from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models import Q

from models import Contact

# displays the index page
def index( request ):    
    return render_to_response('index.html', context_instance = RequestContext(request))
    
# search view 
def search(request):
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:            
            results = Contact.objects.filter(  
            	Q( name__contains = q ) |
                Q( city__contains = q ) )          
            return render_to_response('results.html', {'results': results}, 
                                       context_instance = RequestContext(request))
