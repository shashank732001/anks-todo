from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):


	if request.method =='POST':
		form = ListForm(request.POST) or None
		if form.is_valid():
			form.save()
			all_items=List.objects.all
			messages.success(request,('Item has been successfully added to the list!'))
			return render(request,'home.html',{'all_items': all_items})

	else:	

		all_items=List.objects.all
		return render(request,'home.html',{'all_items': all_items})
	

def about(request):
	my_name='Shashank k shetty'
	context = {'name':my_name}
	return render(request,'about.html',context)


def delete(request,list_id):
	item =List.objects.get(pk=list_id)
	item.delete()
	messages.success(request,('Item has been successfully deleted from the list!'))
	return redirect('home')

def cross_off(request,list_id):
	item =List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('home')

def uncross(request,list_id):
	item =List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('home')

def edit(request,list_id):
	if request.method =='POST':
		item=List.objects.get(pk=list_id)
		form = ListForm(request.POST,instance=item) or None
		if form.is_valid():
			form.save()
			all_items=List.objects.all
			messages.success(request,('Item has been successfully Edited!'))
			return redirect('home')
			

	else:	

		item=List.objects.get(pk=list_id)
		return render(request,'edit.html',{'item': item})	



# Create your views here.S
