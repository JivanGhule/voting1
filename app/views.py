from django.shortcuts import render,redirect,HttpResponseRedirect
from app.models import Data,UserRegistartion
from matplotlib import pyplot as plt
from django.http import HttpResponse
from datetime import datetime
from django.urls import reverse
from app.pdf import html2pdf

# from django.http import HttpResponse
# from django.views.generic import View

# from app.utils import render_to_pdf #created in step 4

# Create your views here.

global name,adhar_number,UID
name=""
adhar_number=""
UID=""

global login
login=False
def Home(request):
    #ms=['Edge','Firefox','Chrome','Opera','Safari']
    if request.method=="POST":
        name=request.POST.get('name')
        browser=request.POST.get('browser')
        print("=>>>",name,browser)  
        # d=Data(name=name,browser=browser) 
        # d.save()
        
        if Data.objects.filter(name=name).exists():
            msg="Already Voted"
        else:
            d=Data(name=name,browser=browser) 
            d.save()
            msg="Successfully Voted"
        
        show=Data.objects.all()
        # context={
        #     'show':show
        # }
        N = []  
        B = []  
        for i in show:
            N.append(i.name)
            B.append(i.browser)
        ms=['Edge','Firefox','Chrome','Opera','Safari']
        
        print("++++++++++++++++++")
        
        Edge=Data.objects.filter(browser="Edge").count()
        print(Edge,"<<<=====","Edge")
        
        Firefox=Data.objects.filter(browser="Firefox").count()
        print(Firefox,"<<<=====","Firefox")
        
        Chrome=Data.objects.filter(browser="Chrome").count()
        print(Chrome,"<<<=====","Chrome")
        
        Opera=Data.objects.filter(browser="Opera").count()
        print(Opera,"<<<=====","Opera")
        
        Safari=Data.objects.filter(browser="Safari").count()
        print(Safari,"<<<=====","Safari")
        
        v=[Edge,Firefox,Chrome,Opera,Safari]
        win=max([Edge,Firefox,Chrome,Opera,Safari])   
        l=[]  
        if win==Edge:
            l.append("Edge")
        if win==Firefox:
            l.append("Firefox")
        if win==Chrome:
            l.append("Chrome")
        if win==Opera:
            l.append("Opera")
        if win==Safari:
            l.append("Safari")
        
        print(l)
            
        
        return render(request,'index.html',{'Edge':Edge,'Firefox':Firefox,'Chrome':Chrome,'Opera':Opera,'Safari':Safari,'win':win,'l':l,'msg':msg,'ms':ms,'v':v,'login':login})
        
    return render(request,'index.html',{'login':login})

login = False
def Registration(request):
    if request.method=="POST":
        global name,adhar_number,UID
        name=request.POST.get('name')
        adhar_number=request.POST.get('adhar_number')
        mobile_number=request.POST.get('mobile_number')
        address=request.POST.get('address')
        age=request.POST.get('age')
        UID=str(mobile_number[:3]+name[:3]+adhar_number[:3])
        
        msg1=''
        #user = UserRegistartion.objects.filter(adhar_number=adhar_number,mobile_number=mobile_number).exists()
        user=UserRegistartion.objects.filter(adhar_number=adhar_number).exists()
        if len(str(mobile_number))==10 and len(str(adhar_number))==12 and int(age)>=18:
            
            if user:
                msg1="Already Registered"
                return render(request,'registration.html',{'msg1':msg1})
            else:
                d=UserRegistartion(name=name,adhar_number=adhar_number,mobile_number=mobile_number,address=address,age=age,UID=UID) 
                d.save()
                
                # global n,a,u
                # n=name
                # a=adhar_number
                # u=UID
                #kwargs={'name':name,'adhar_number':adhar_number,'UID':UID}
                #return redirect(request, 'pdf', {'name':name,'adhar_number':adhar_number,'UID':UID})
                # return HttpResponseRedirect(reverse('pdf', kwargs={'name':name,'adhar_number':adhar_number,'UID':UID}))
                return render(request,'pdf.html',{'name':name,'adhar_number':adhar_number,'UID':UID})
        else:
            msg1="Something Wrong Please Check Mobile, Adhar Number or Age Once"
            return render(request,'registration.html',{'msg1':msg1})
            
        
        
    return render(request,'registration.html')
print("Login B-O==>",login)
def Login(request):
    if request.method=="POST":
        global name,adhar_number,UID
        name=request.POST.get('name')
        adhar_number=request.POST.get('adhar_number')
        UID=request.POST.get('UID')
        user=UserRegistartion.objects.filter(name=name,adhar_number=adhar_number,UID=UID).exists()
        if user:
            global login
            login = True
            print("Login I==>",login)
            return render(request,'vote.html',{'login':login,'name':name})
        else:
            msg2="Something Went Wrong!!!"
            return render(request,'login.html',{'msg2':msg2})

    return render(request,'login.html')
print("Login A-O==>",login)
# homepage=False
def Vote(request):
    # return render(request,'vote.html')
    if login:
        if request.method=="POST":
            name=request.POST.get('name')
            
            if Data.objects.filter(name=name).exists():
                msg="Already Voted"
                return render(request,'vote.html',{"msg":msg})
            else:
                msg="Successfully Voted"
                return render(request,'vote.html',{"msg":msg})
        # return HttpResponse("Success")
    else:
        # return HttpResponse("<strong>Login Please <a href="">Login Here</a></strong>")
        return render(request,'demo.html')
    
    # return render(request,'vote.html')

def Result(request):
    Date = datetime(2023, 1, 17)
    # today's datetime
    today = datetime.now()
    
    dt=today > Date
    print(Date,today)
    
    Edge=Data.objects.filter(browser="Edge").count()
    Firefox=Data.objects.filter(browser="Firefox").count()
    Chrome=Data.objects.filter(browser="Chrome").count()
    Opera=Data.objects.filter(browser="Opera").count()
    Safari=Data.objects.filter(browser="Safari").count()
    ms=['Edge','Firefox','Chrome','Opera','Safari']
    v=[Edge,Firefox,Chrome,Opera,Safari]
    win=max([Edge,Firefox,Chrome,Opera,Safari])   
    l=[]  
    if win==Edge:
        l.append("Edge")
    if win==Firefox:
        l.append("Firefox")
    if win==Chrome:
        l.append("Chrome")
    if win==Opera:
        l.append("Opera")
    if win==Safari:
        l.append("Safari")
    return render(request,'result.html',{'dt':dt,'Edge':Edge,'Firefox':Firefox,'Chrome':Chrome,'Opera':Opera,'Safari':Safari,'win':win,'l':l,'ms':ms,'v':v})





# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#              'today': datetime.date.today(), 
#              'amount': 39.99,
#         }
#         pdf = render_to_pdf('pdf/voter_id.html',data)
#    return HttpResponse(pdf, content_type='application/pdf')
global data
data={
    "name":name,
    "adhar_number":adhar_number,
    "UID":UID
}
def pdf(request):
    #n,a,u
    global pdf
    pdf=html2pdf("pdf.html",data)#pdf.html
    #return render(request,'pdf.html')
    return HttpResponse(pdf,content_type="application/pdf")

    # # data = {'name':n,'adhar_number':a,'UID':u}
    # pdf = html2pdf('pdf.html',{'name':n,'adhar_number':a,'UID':u})
    # return HttpResponse(pdf, content_type='application/pdf')

def download_id(request):
    if request.method=="POST":
        name=request.POST.get('name')
        adhar_number=request.POST.get('adhar_number')
        print(name,adhar_number)
        user=UserRegistartion.objects.filter(adhar_number=adhar_number,name=name).exists()
        # print("++++++++++++++++")
        # print(user)
        if user:
            data=UserRegistartion.objects.all()
            for i in data:
                if name==i.name:
                    print(i.UID)
                    print("===============")
                    context={
                            "name":i.name,
                            "adhar_number":i.adhar_number,
                            "UID":i.UID
                    }
                    return render(request,'pdf.html',context)
            
        else:
            print("Else")
    return render(request,'download_id.html')

def logout(request):
    return render(request,'index.html')