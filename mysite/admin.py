from django.contrib import admin
from mysite.models import Project
from mysite.models import Message
from mysite.models import Post

# Register your models here.
#class ProjectAdmin(admin.ModelAdmin):
#	fields = ['title', 'image_descriotion', 'content', 'created_date']

admin.site.register(Message)
admin.site.register(Project)
admin.site.register(Post)