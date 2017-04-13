from django.db import models
from django.utils import timezone


class Project(models.Model):
	class Meta():
		db_table = 'project'
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	image_descriotion = models.ImageField(null=True, blank=True,upload_to='images/')
	content = models.TextField()
	created_date = models.DateTimeField(
            default=timezone.now)
	
	def __str__(self):
		return self.title
		
	def __publish(self):
		self.save()
		

class Message(models.Model):
	class Meta():
		db_table = 'message'
	message_title = models.CharField(max_length=200)
	author_name = models.CharField(max_length=200)
	e_mail = models.EmailField() 
	message_text = models.TextField()
	created_date_message = models.DateTimeField(
            default=timezone.now)
	
	def __str__(self):
		return self.message_title
		
	def __publish(self):
		self.save()
		
		
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title