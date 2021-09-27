from .models import*
from django import forms
class ToDoform(forms.ModelForm):
	class Meta:
		model=ToDoList
		fields=[
			'name',
			]