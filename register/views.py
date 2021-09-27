from django.shortcuts import render,redirect
from .forms import*

def register(request):
	form=RegisterForm(request.POST)
	if request.method =="POST":
		form=RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/home")
	else:
		print("nopey")
	return render(request,"register/register.html",{"form":form})


# Create your views here.
