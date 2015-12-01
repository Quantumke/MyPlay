from django.shortcuts import render_to_response, get_object_or_404
from clone.models import Dplay


# Create your views here.

def index(request):
	return render_to_response('index.html',{
	'Dplay':Dplay.objects.order_by('-date')[:3],
	'animation':Dplay.objects.filter(category='animation')[:4],
	'popular':Dplay.objects.filter(uploaded_by='Ben Kiboko')[:4],
	'recommended':Dplay.objects.filter(views__gt=1000)[:4],
	'sport':Dplay.objects.filter(category='Sport')[:4],
	'blockbusters':Dplay.objects.filter(category='blockbuster')
	})
def view_more(request, slug):
	return render_to_response('single.html',{
	'post':get_object_or_404(Dplay, slug=slug)
	})

