from django.shortcuts import render
from centres import models
from .models import SlotBook,Certificate

# Create your views here.
def slot_book(request,centerid,slot,vaccine,date):
    slotno=0
    if int(slot)==1:slot="8:00-11:00"
    elif int(slot)==2:slot="12:00-2:00"
    elif int(slot)==3:slot="3:00-5:00"
    Centre=models.Centres.objects.filter(id=centerid).first()
    if request.method=='POST':
        print(request.POST)
        fc=request.POST
        fm=SlotBook(name=fc['name'],center_id=centerid,age=fc['age'],dose_name=vaccine,gender=fc['gender'],contacts=fc['phone'],id_proof_type=fc['id_proof'],id_proof_number=fc['id_proof_number'],slot_date=date,slot_time=slot)
        fm.save()
        slotno=SlotBook.objects.all().last();
    return render(request,"slot_book.html",{"centre":Centre,"date":date,"vaccine":vaccine,"slot":slot,"sb":slotno})


def slot_status(request):
    print(request.POST)
    msg=""
    sb=None
    status=False
    Centre=None
    if request.POST:
        if request.POST["by"]=="slotno":
            sb=SlotBook.objects.filter(id=request.POST['slotno'],slot_date=request.POST['date'],id_proof_number=request.POST['id_proof_number'])        
        elif request.POST["by"]=="phone":
            sb=SlotBook.objects.filter(contacts=request.POST['slotno'],slot_date=request.POST['date'],id_proof_number=request.POST['id_proof_number'])
        if sb:
            sb=sb[0]
            status=True
            Centre=models.Centres.objects.filter(id=sb.center_id).first()
        else:
            msg="Slot Not Found"
    return render(request,"slot_status.html",{"status":status,"msg":msg,"sb":sb,"centre":Centre})


def certificate(request):

    print(request.POST)
    context={"status":False,"msg":None,"user":None,"slot":None,"centre":None}
    if request.POST:
        if request.POST["by"]=="slotno":
            context["slot"]=SlotBook.objects.filter(id=request.POST['slotno'],slot_date=request.POST['date'],id_proof_number=request.POST['id_proof_number'])        
        elif request.POST["by"]=="phone":
            context["slot"]=SlotBook.objects.filter(contacts=request.POST['slotno'],slot_date=request.POST['date'],id_proof_number=request.POST['id_proof_number'])
        
        if context["slot"]:
            context["slot"]=context["slot"].first()
            certificate = Certificate.objects.filter(slotno=context["slot"].id)
            if certificate:
                cer=certificate.first()
                context["status"]=True
                context["center"]=models.Centres.objects.get(id=cer.centerid)
                context["user"] = models.Employee.objects.get(id=cer.employeeid)
            else:
                context["msg"]="Certificate Not Found"
    return render(request,"certificate.html",context)



def home(request):
    if request.session.get("username")==None:
        return redirect("/")
    
    return render(request,"beneficiary.html",{"username":request.session["username"]})

