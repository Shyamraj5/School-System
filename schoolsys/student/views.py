from django.shortcuts import render,redirect
from django.views import View
from.models import studentModel
from.forms import studentModelForm
# Create your views here.
class Home(View):
    def get(self,request,*args, **kwargs):
        res=studentModel.objects.all()
       
        return render(request,"home.html",{"form":res})
class addstudent(View):
    def get(self,request,*args, **kwargs):
        obj=studentModelForm()
        return render(request,"studentlist.html",{"form":obj})
    def post(self,request,*args, **kwargs):
        form=studentModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")   
        else:
            return render(request,"studentlist.html")  