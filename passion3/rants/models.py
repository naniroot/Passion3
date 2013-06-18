import datetime

from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

class PostManager(models.Manager):
	def get_visible(self):
		return self.get_query_set().filter(publish_at__lte=datetime.datetime.now(), active=True)

class TimeStampedActivate(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=False,
			 help_text='Controls whether or not this item is live to the world')

	class Meta:
		abstract = True

class Rant(TimeStampedActivate):
	"""
	A rant that belongs to a user.

	>>> b = Rant()
	>>> b.name = 'Foo Blog'
	>>> b.slug = 'foo-blog'
	>>> b.user = User.objects.create(username='foo', password='test')
	>>> b.save()
	>>> print b.name
	Foo Blog
	
	"""
	name = models.CharField(max_length=255,
				help_text='Name of your rant. Can be 255 char')
	slug = models.SlugField()
	description = models.TextField(blank=True,
					help_text='Your rant basically')
	user = models.ForeignKey(User, related_name='rants')

	def __unicode__(self):
		return self.name
	
	@models.permalink
	def get_absolute_url(self):
		return ('rant', (), {
			'slug': self.slug
		})

class Post(TimeStampedActivate):
	"""
	A post that belongs to a rant.

	>>> b = Blog.objects.get(id=1)
	>>> p = Post()
	>>> p.title = "A test Post"
	>>> p.blog = b
	>>> p.body = "Just a small post"
	>>> p.slug = "a-test-slug"
	>>> p.save()
	>>> print p.blog.name
	Foo Blog
	>>> print p.active
	False

	"""
	title = models.CharField(max_length=255,
					help_text="Title of the post")
	slug = models.SlugField()
	excerpt = models.TextField(blank=True, 
					help_text="A small teaser of your content")
	body = models.TextField()
	publish_at = models.DateTimeField(default=datetime.datetime.now(),
					help_text="Date and time post should become visible")
	rant = models.ForeignKey(Rant, related_name='posts')
	tags = TaggableManager()
	objects = PostManager()

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ('-publish_at','-modified','-created')

	@models.permalink
	def get_absolute_url(self):
		return ('post', (), {
			'rant': self.rant.slug,
			'slug': self.slug
		})
