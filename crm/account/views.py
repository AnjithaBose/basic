from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .models import *
from .forms import *
# Create your views here.

class ContactView(View):
    def get(self,request):
        user=request.user
        c=Contact.objects.filter(user=request.user)
        return render(request,'account/index.html',{'x':c,'user':user})

class AddContact(View):
    def get(self,request):
        form=AddContactForm()
        return render(request,'account/addcontact.html',{'form':form})
        
    def post(self,request):
        form=AddContactForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.user=request.user
            f.save()
        return redirect('home')

class EditContact(View):
    def get(self,request,id):
        c=Contact.objects.get(id=id)
        form=AddContactForm(instance=c)
        return render(request,'account/editcontact.html',{'form':form})

    def post(self,request,id):
        c=Contact.objects.get(id=id)
        form=AddContactForm(request.POST,instance=c)
        if form.is_valid():
            form.save()
            return redirect('home')
class DeleteContact(View):
    def get(self,request,id):
        c=Contact.objects.get(id=id)
        c.delete()
        return redirect('home')


    

             
           
