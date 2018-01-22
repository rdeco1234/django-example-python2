# -*- coding:utf-8 -*-

from django import forms
from django.core.mail import send_mail
from django.conf import settings

class MyForm(forms.Form):
#	name = forms.CharField()
#	email = forms.EmailField()
#	message = forms.CharField(widget=forms.Textarea)
	your_name = forms.CharField(
	label='name',
	max_length=20,
	required=True,
	widget=forms.TextInput()
    )

	def send_email(self):
		subject = self.cleaned_data['name']
		message = self.cleaned_data['message']
		from_email = settings.EMAIL_HOST_USER
		to = [settings.EMAIL_HOST_USER]

		send_mail(subject, message, from_email, to)


class PersonForm(forms.Form):
	word = forms.CharField(max_length=250)

EMPTY_CHOICES = (
    ('', '-'*10),
)

GENDER_CHOICES = (
    ('man', 'man'),
    ('woman', 'woman')
)

FOOD_CHOICES = (
    ('apple', 'apple'),
    ('beef', 'beef'),
    ('bread', 'bread'),

)


class SampleForm(forms.Form):
    age = forms.IntegerField(
        label='age',
        min_value=0,
        max_value=200,
        required=True,
    )

    birthday = forms.DateField(
        label='birthday',
        required=True,
        input_formats=[
            '%Y-%m-%d',  # 2010-01-01
            '%Y/%m/%d',  # 2010/01/01
        ]
    )

    send_message = forms.BooleanField(
        label='submit',
        required=False,
    )

    gender_r = forms.ChoiceField(
        label='gender',
        widget=forms.RadioSelect,
        choices=GENDER_CHOICES,
        required=True,
    )

    gender_s = forms.ChoiceField(
        label='gender',
        widget=forms.Select,
        choices=EMPTY_CHOICES + GENDER_CHOICES,
        required=False,
    )

    food_s = forms.ChoiceField(
        label='food',
        widget=forms.SelectMultiple,
        choices=FOOD_CHOICES,
        required=True,
    )

    food_c = forms.ChoiceField(
        label='food',
        widget=forms.CheckboxSelectMultiple,
        choices=FOOD_CHOICES,
        required=True,
    )

