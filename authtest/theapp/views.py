from django.shortcuts import render,redirect
import random
from twilio.rest import Client

otp=random.randint(1111,9999)
auth_token="900062764324071aa543c688b0d2ea4c"
auth_id="AC9ae150dd36651e026e92d90da90a935f"

client=Client(auth_id,auth_token)


def homepage(request):
    if request.method=='POST':
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        msg=client.messages.create(
            body=f" I.S.A.S:  www.mbuguanganag.tech hello {name} your outh is {otp}",
            from_="+18596517429",
            to=phone
        )
        
        return redirect('auth')
    return render(request,'theapp/hello.html')
def authentic(request):
    if request.method=='POST':
        otpno=request.POST.get("otpno")
        atb=int(otp) and int(otpno)
        if atb==True:
             return redirect('login')
    return render(request,'theapp/authenti.html')
def login(request):
    return render(request,'theapp/login.html')

