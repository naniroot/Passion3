import datetime

from django.shortcuts import get_object_or_404

from annoying.decorators import render_to

from rants.models import Rant, Post

@render_to('index.html')
def blog_index(request):
	rants = Rant.objects.filter(active=True)
	
	return { 'rants':rants }

@render_to('rants/index.html')
def rant(request, slug):
	rant = get_object_or_404(Rant, active=True, slug=slug)

	return { 'rant': rant }

@render_to('rants/post.html')
def post(request, rant, slug):
	post = get_object_or_404(Post, active=True, 
				publish_at__lte=datetime.datetime.now(),
				rant__slug=rant,
				slug=slug)

	return { 'post': post }
	
