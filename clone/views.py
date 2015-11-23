from django.shortcuts import render_to_response, get_object_or_404
from clone.models import Dplay

# Create your views here.

def index(request):
	return render_to_response('index.html',{
	'Dplay':Dplay.objects.all()
	})
