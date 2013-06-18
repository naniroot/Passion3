import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from rants.models import Rant, Post

def blog_index(request):
	rants = Rant.objects.filter(active=True)
	return render_to_response('index.html', {
		'rants': rants,
	}, context_instance=RequestContext(request)) 

def rant(request, slug):
	rant = get_object_or_404(Rant, active=True, slug=slug)

	return render_to_response('rants/index.html', {
		'rant': rant
	}, context_instance=RequestContext(request))

def post(request, rant, slug):
	post = get_object_or_404(Post, active=True, 
				publish_at__lte=datetime.datetime.now(),
				rant__slug=rant,
				slug=slug)
	return render_to_response('rants/post.html', {
		'post': post,
	}, context_instance=RequestContext(request))
	
