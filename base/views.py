
from django.shortcuts import render, redirect
from centres import models
from beneficiary import models as bm
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request,'base/home.html')


def contact_us(request):
    return render(request,'base/contact_us.html')

def employee(request):
    return render(request,'employee.html')

def logout(request):
    del request.session["userid"]
    return redirect("login")


def centres(request):
    slist=models.Centres.objects.all()
    paginator=Paginator(slist,8,orphans=2)
    pn=request.GET.get('page') 
    page=paginator.get_page(pn)
    return render(request,'base/centres.html',{"Page":page}) 



def login(request):
    request.session.clear()
    print(request.POST)
    msg=""
    if request.POST:
        users=models.Employee.objects.filter(id=request.POST['userid'],password=request.POST['password'])
        if users:
            request.session['userid'] = users[0].id
            request.session['username'] = users[0].name
            request.session['usertype'] = "employee"
            return redirect("centres/employee_home")
        else:
            msg="Invalid Login Details"
    
        

    return render(request,'base/login.html',{"msg":msg})


def findslot(request):
    context={"status":False,"centre":None,"date":"","covishield":[50,50,50],"covaxin":[50,50,50]}
    if request.method=="POST":
        context["status"]=True
        context["centre"]=models.Centres.objects.filter(id=int(request.POST['centreid'].split(")")[0])).first()
        context["date"]=request.POST["date"]
        for x in bm.SlotBook.objects.filter(slot_date=request.POST["date"]).all():
            if x.slot_time=="8:00-10:00":
                context[x.dose_name][0]-=1
            elif x.slot_time=="12:00-2:00":
                context[x.dose_name][1]-=1
            elif x.slot_time=="3:00-5:00":
                context[x.dose_name][2]-=1
            
    context["slist"]=models.Centres.objects.all()
    return render(request,'base/findslot.html',context)