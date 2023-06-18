from django.http import HttpResponse
from django.shortcuts import redirect, render
import datetime

# Create your views here.
from .models import User,Task

def openLoginForm(request):
    if 'user_id' in request.session:
        return redirect('/dashboard')
    return render(request,"login.html")

def openTaskForm(request):
    if 'user_id' in request.session:
        return render(request,"task-form.html")
    else:
        return redirect('/')

def saveTask(request):
    if 'user_id' in request.session:
        user=User.objects.get(id=request.session['user_id'])
        t=Task()
        t.title=request.POST['title']
        t.description=request.POST['description']
        t.createdOn=request.POST['created-on']
        t.user=user
        t.save()
        return redirect('/tasks-list')
    else:
        return redirect('/')

def markTaskAsCompleted(request,id):
    t=Task.objects.get(id=id)
    t.completionStatus=True
    t.completionDate=datetime.datetime.now()
    t.save()
    return redirect('/tasks-list')

def getAllTasks(request):
    if 'user_id' in request.session:
        user=User.objects.get(id=request.session['user_id'])
        tasks=user.task_set.all()
        return render(request,"all-tasks.html",{'tasks':tasks})
    else:
        return redirect('/')

def openDashboard(request):
    if 'user_id' in request.session:
        userid=request.session['user_id']
        user=User.objects.get(id=userid)
        return render(request,"dashboard.html",{'user':user})
    else:
        return redirect('/')
    
def logout(request):
    del request.session['user_id']
    return redirect("/")

def openUserForm(request):
    return render(request,"user-form.html")

def saveUser(request):
    u=User()
    u.name=request.POST['name']
    u.phone=request.POST['phone']
    u.password=request.POST['password']
    u.email=request.POST['email']
    u.save()
    return redirect("/")

def login(request):
    phone=request.POST['phone']
    password=request.POST['password']
    user=User.objects.filter(phone=phone,password=password)
    if user:
        data=user.values()
        request.session['user_id']=data[0]['id']
        return redirect('/dashboard')
    else:
        return render(request,"login.html",
        {'error':'Invalid phone or password'})