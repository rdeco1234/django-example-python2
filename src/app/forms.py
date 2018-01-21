from django import forms

class MyForm(forms.Form):
     name = forms.CharField()
     email = forms.EmailField()
     body = forms.CharField() 

#	def send_email(self):
#		subject = self.cleaned_data['name']
#		message = self.cleaned_data['message']
#		from_email = settings.EMAIL_HOST_USER
#		to = [settings.EMAIL_HOST_USER]
#
#		send_mail(subject, message, from_email, to)

