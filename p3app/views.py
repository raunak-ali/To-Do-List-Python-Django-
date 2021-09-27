from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import*
from .models import*
from .forms import*

# Create your views here.
def home_views(request):
	return render(request,'p/home.html',{})
def list_views(request,id):
	ls=ToDoList.objects.get(id=id)
	print("here")
	if request.method == "POST":
		print(request.POST)
		print("happening")
		if request.POST.get("save"):
			print("a")
			for item in ls.item_set.all():
				print("b")
				if request.POST.get("c" +str(item.id)) == "clicked":
					print("c")
					item.complete = True
					print("happened")
				else:
					print("d")
					item.complete = False
				item.save()
		elif request.POST.get("newItem"):
			print("e")
			txt=request.POST.get("new")
			if len(txt) > 2 :
				ls.item_set.create(text=txt,complete=False)
			else:
				print("noes")
		else:
			print("problem")
	else:
		print("bitch")
			
	return render(request,'p/list.html',{'ls':ls})
def views(request):
		l = ToDoList.objects.all()
		return render(request, "p/view.html", {"lists":l})
		
def create_views(request):
	if request.method == "POST":
		form = ToDoform(request.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()
			
			return HttpResponseRedirect("/%i" %t.id)

	else:
		form = ToDoform()

	return render(request, "p/forms.html", {"form": form})
	