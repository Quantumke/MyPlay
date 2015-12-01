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
	'english':Dplay.objects.filter(channel='English')
	})
def english(request):
 	return render_to_response('english.html',{
	'english':Dplay.objects.filter(channel='English')
	})
def chinese(request):
	return render_to_response('chinese.html',{
	'chinese':Dplay.objects.filter(channel='chinese')
	})
def hindi(request):
        return render_to_response('hindi.html',{
        'hindi':Dplay.objects.filter(channel='hindi')
        })
def animation(request):
	return render_to_response('animation.html',{
	'animation':Dplay.objects.filter(channel='animation')
	})

def view_more(request, slug):
	return render_to_response('single.html',{
	'post':get_object_or_404(Dplay, slug=slug)
	})


