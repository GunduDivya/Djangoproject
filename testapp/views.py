from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home_view(request):
    return render(request,'TESTAPP/home.html')
@login_required
def java_view(request):
    return render(request,'TESTAPP/java.html')
@login_required
def python_view(request):
    return render(request,'TESTAPP/python.html')
def logout_view(request):
    return render(request,'TESTAPP/logout.html')
from testapp.forms import singupform
def singup_view(request):
    form=singupform()
    return render(request,'TESTAPP/singup.html',{'form':form})
from django.http import HttpResponseRedirect
def sign_view(request):
    form=singupform()
    if request.method=='POST':
        form=singupform(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login/')
    return render(request,'TESTAPP/singup.html',{'form':form})