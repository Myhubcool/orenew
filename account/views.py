from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import rtlrmodel , usermodel
from .models import all
#CUSTOMER SIGN-IN FUNCTION
def customer_signin(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user=User.objects.get(username = request.POST['username'])
                return render(request, 'account/customer_signin.html', {'error': 'User-id is not valid!'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                if request.POST['Name'] and request.POST['username'] and  request.POST['password1'] and request.POST['password2'] and  request.POST['email1']:
                            info=usermodel()
                            info.username =                     request.POST['Name']
                            info.userid   =                     request.POST['username']
                            info.userpassword =                 request.POST['password1']
                            info.userconfirmpassword =          request.POST['password2']
                            info.useremail =                    request.POST['email1']
                            info.save()
                            auth.login(request, user)
                            return redirect('home')
                else:
                     return render(request, 'account/customer_signin.html',{'error':'Please fill all fields!'})
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'account/customer_signin.html',{'error':'password does not matched!'})
    else:
        return render(request,'account/customer_signin.html')
#RETIALER SIGN-IN FUNCTION
def retailer_signin(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user=User.objects.get(username = request.POST['username'])
                return render(request, 'account/retailer_signin.html', {'error': 'User-id is not valid!'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                if request.POST['Name'] and request.POST['username'] and  request.POST['password1'] and request.POST['password2'] and  request.POST['email2'] and request.POST['city'] and request.POST['shopphno'] and request.POST['shopaddress'] and  request.FILES['shopprofilephoto']:
                      if request.POST['password1'] == request.POST['password2']:
                            info=rtlrmodel()
                            info.rtlrname =                     request.POST['Name']
                            info.rtlrid   =                     request.POST['username']
                            info.rtlrpassword =                 request.POST['password1']
                            info.rtlrconfirmpassword =          request.POST['password2']
                            info.rtlruseremail =                request.POST['email2']
                            info.rtlrshopcity=                  request.POST['city']
                            info.rtlrshopno=                    request.POST['shopphno']
                            info.rtlrpcolony =                  request.POST['colony']
                            info.rtlrshopname=                  request.POST['shopname']
                            info.rtlrshopaddress=               request.POST['shopaddress']
                            info.rtlrstate=                     request.POST['state']
                            info.rtlrdistrict=                  request.POST['district']
                            info.rtlrpincode=                   request.POST['pinno']
                            info.rtlrphoto=                     request.FILES['shopprofilephoto']
                            info.save()
                            auth.login(request, user)
                            return redirect('home')
                      else:
                            return render(request, 'account/retailer_signin.html',{'error':'Password does not matched!'})
                else:
                     return render(request, 'account/retailer_signin.html',{'error':'Please fill all fields!'})
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'account/retailer_signin.html',{'error':'password does not matched!'})
    else:
        return render(request,'account/retailer_signin.html')
#VERIFY FUNCTION FOR CHOICE CUSTOMER AND MACHANIC
def verify(request):
    return render(request,'account/verify.html')
def loginreq(request):
    return render(request, 'account/loginreq.html',{'error':'Sorry you have to login first !'})

#LOGIN FUNCTION
def login(request):
    if request.method == 'POST':
        if request.POST['userid']!='':
            user=auth.authenticate(username=request.POST['userid'],password=request.POST['passwordd'])
            if user is not None:
                auth.login(request,user)
                return redirect('home')
            else:
                return render(request, 'account/login.html',{'error':'User-Id or password is incorrect!'})
        else:
            return render(request, 'account/login.html', {'error': 'Please fill all details!'})
    else:
        return render(request,'account/login.html')
#LOGOUT FUNCTION
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('homee')
    else:
        return render(request,'account/logout.html')
#CUSTOMER-PROFILE FUNCTION
def userprofile(request):
    U_model=usermodel.objects
    return render(request,'account/userprofile.html',{'U_model':U_model})
#MACHANIC-PROFILE FUNCTION
def machanicprofile(request):
    R_model = rtlrmodel.objects
    return render(request,'account/machanicprofile.html',{'R_model':R_model})
#ADD Fun AIO
def filled(request):
    rmach = rtlrmodel.objects
    if request.method == 'POST':
        if request.POST['x']=='a':
            x='z'
            fun=request.POST['fusernane']
            fuid=request.POST['fusernameid']
            fm=request.POST['fmob']
            fc=request.POST['fcity']
            sdd=request.POST['fshopadd']
            fst=request.POST['fstate']
            fdt=request.POST['fdistrict']
            fcy=request.POST['fcolony']
            fpn=request.POST['fpincode']
            fsn=request.POST['shopname']
            return render(request, 'account/fill.html',{'fsn':fsn,'fst':fst,'fdt':fdt,'fcy':fcy,'fpn':fpn,'x':x,'fun':fun,'fm':fm,'fc':fc,'rmach':rmach,'sdd':sdd,'fuid':fuid})
        elif request.POST['x']=='z':
          pksheck = all.objects.all()
          for ck in pksheck:
              if ck.acompanyname==request.POST['companyname'] and ck.auid==request.POST['userid']:
                go='1'
                return render(request, 'account/congratulation.html',{'errorr':'This detail is already you filled','go':go})
          else:
            if request.POST['companyname'] is not None:
                srt=all()
                srt.acompanyname=request.POST['companyname']
                srt.aname=request.POST['username']
                srt.amob = request.POST['phoneno']
                srt.ascity = request.POST['city']
                srt.auid=request.POST['userid']
                srt.aaddress = request.POST['address']
                srt.aprice = request.POST['price']
                srt.asstate=request.POST['state']
                srt.ascolony=request.POST['colony']
                srt.aspinno=request.POST['pinno']
                srt.asdistrict=request.POST['district']
                srt.asshopname=request.POST['shopname']
                srt.save()
                return render(request, 'account/congratulation.html',{'send':request.POST['companyname']})
    else:
        return render(request,'account/fill.html',{'rmach':rmach})

def congratulation(request):
    return render(request, 'account/congratulation.html')

def home(request):
    if request.method=='POST':
        return render(request,'account/mnframe.html')
    else:
        rmach=rtlrmodel.objects
        suser=usermodel.objects
        return render(request,'account/home.html',{'suser':suser,'rmach':rmach})

def homee(request):
    return render(request,'account/homee.html')

def mnframe(request):
    if request.method=='POST':
        database=all.objects
        search=request.POST['Search']
        location=request.POST['Location']
        return render(request, 'account/mnframe.html',{'database':database,'search':search,'location':location})

def tservice(request):
    return render(request,'account/tservice.html')


