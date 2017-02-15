from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.shortcuts import render_to_response
from mysite.models import Project
from mysite.models import Message
from .forms import *
from xml.dom.minidom import *
import pars
from PIL import Image

# Create your views here.

#def basic_one(request):
#	view = "basic_one"
#	html = "<html><body>This is %s view</html></body>" % view
#	return HttpResponse(html)

def about_us(request):
	text_content = pars.parse('description')
	image_content = pars.parse('images')
	information_content = pars.parse('information')
	return render_to_response('about.html', {'data': text_content.nodeValue, 'picture': image_content.nodeValue, 'info': information_content.nodeValue})

def projects(request):
	text_content = pars.parse('description')
	image_content = pars.parse('images')
	projects = Project.objects.all()
	return render_to_response('projects.html', {'projects': projects, 'data': text_content.nodeValue, 'picture': image_content.nodeValue})
	

def send_message(request):
	text_content = pars.parse('description')
	image_content = pars.parse('images')
	errors = []
	form = {}
	if request.POST:
		form['title'] = request.POST.get('message_title')
		form['name'] = request.POST.get('your_name')
		form['email'] = request.POST.get('guest_mail')
		form['message'] = request.POST.get('message_text')
		if not form['name']:
			errors.append('Заполните имя')
			return render(request, 'message.html', {'data': text_content.nodeValue, 'picture': image_content.nodeValue, 'errors': errors, 'form':form})
		if '@' not in form['email']:
			errors.append('Введите корректный e-mail')
			return render(request, 'message.html', {'data': text_content.nodeValue, 'picture': image_content.nodeValue, 'errors': errors, 'form':form})
		if not form['message']:
			errors.append('Введите сообщение')
			return render(request, 'message.html', {'data': text_content.nodeValue, 'picture': image_content.nodeValue, 'errors': errors, 'form':form})
		if not form['title']:
			errors.append('Заполните заголовок')
			return render(request, 'message.html', {'data': text_content.nodeValue, 'picture': image_content.nodeValue, 'errors': errors, 'form':form})
		else:
			#if request.method == 'POST':
			#form = FiledForm(request.POST)
			#print(form)
			#if form.is_valid():
				#print("form.is_valid")
				#add = form.save(commit=False)
				#add.save()
			# ... сохранение данных в базу
				new_entry = Message(e_mail=form['email'], message_title=form['title'], author_name=form['name'], message_text=form['message'])
				new_entry.save()
		return HttpResponse('Спасибо за ваше сообщение!')
	return render(request, 'message.html', {'data': text_content.nodeValue, 'picture': image_content.nodeValue, 'errors': errors, 'form':form})