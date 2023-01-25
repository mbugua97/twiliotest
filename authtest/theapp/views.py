from django.shortcuts import render,redirect
import random
from twilio.rest import Client

otp=random.randint(1111,9999)
auth_token="c49fb1f396e3a9fa7b7e644acd6b312f"
auth_id="AC9ae150dd36651e026e92d90da90a935f"

client=Client(auth_id,auth_token)


def homepage(request):
    if request.method=='POST':
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        msg=client.messages.create(
            body=f"hello {name} your outh is {otp}",
            from_="+18596517429",
            to="+254794432871"
        )
        
        return redirect('auth')
    return render(request,'theapp/hello.html')
def authentic(request):
    if request.method=='POST':
        otpno=request.POST.get("otpno")
        if otp!=otpno:
             return redirect('login')
    return render(request,'theapp/authenti.html')
def login(request):
    return render(request,'theapp/login.html')

