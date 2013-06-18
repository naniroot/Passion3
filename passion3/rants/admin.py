from django.contrib import admin

from rants.models import Rant, Post

class RantAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",)}
	list_display = ('active', 'name', 'description','user',)
	list_display_links = ('name',)
	list_editable = ('active',)
	list_filter = ('modified', 'created','active',)
	
class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("title",)}
	list_display = ('active','title','excerpt','publish_at')
	list_display_links = ('title',)
	list_editable = ('active', )
	list_filter = ('publish_at', 'modified', 'created', 'active')
	date_hierarchy = 'publish_at'
	search_fields = ['title', 'excerpt', 'body','rant__name', 'rant__user__username']
	fieldsets = (
		(None, {
			'fields' : ('title','rant'),
		}),
		('Publication',{
			'fields':('active','publish_at'),
			'description': "Control <strong>whether</strong> or not <strong>when</strong> the post is visible to the whole world"
		}),
		('content',{
			'fields':('excerpt','body','tags'),
		}),
		('Optional',{
			'fields':('slug',),
			'classes': ('collapse',),
		}),
	)

admin.site.register(Rant, RantAdmin)
admin.site.register(Post, PostAdmin)
