from django import forms
from .models import Message

class FiledForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ('e_mail', 'message_title', 'author_name', 'message_text',)