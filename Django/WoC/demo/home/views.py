from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from datetime import datetime
from home.models import Event, Part
import  random
from dotenv import load_dotenv
import os
load_dotenv()
# Create your views here.
def index(request):
    context = {
        'variable': "django"
    }
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return HttpResponse("In the about page")

def services(request):
    return HttpResponse("In the services page")

def EventRegistration(request):
    if request.method == "POST":
        host_email = request.POST.get("host_email")
        password = request.POST.get('password')
        eventname = request.POST.get('eventname')
        location = request.POST.get('location')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        deadDate = request.POST.get('deadDate')
        dec = request.POST.get('dec')

        if startDate > endDate or deadDate>startDate:
            context = {'message' : 'Invalid data inserted'}
            return render(request, 'Event Registration.html', context)

        event = Event(host_email=host_email, password=password, eventname=eventname, location=location, startDate=startDate, endDate=endDate, deadDate=deadDate, dec=dec, nop=0)
        # print(host_email)
        event.save()
        # temp = sign(user_email=host_email, user_password=password)
        # temp.save()
        send_mail(
           'Your event :',
            'Here is the confirmation message.\n Good Luck !',
            os.environ.get("EMAIL_HOST_USER"),
            [host_email],
            fail_silently=False,
        )
        return render(request, 'Event Registration.html')
        # return render(request, 'Event Registration.html')
    return render(request, 'Event Registration.html')
    # return HttpResponse("In event registration")

def ParticipantRegistration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        contactnumber = request.POST.get('contactnumber')
        part_email = request.POST.get("part_email")
        password = request.POST.get('password')
        eventName = request.POST.get('eventName')
        number = request.POST.get('number')
        reg_type = request.POST.get('reg_type')

        if Part.objects.all().filter(part_email=part_email, password=password, eventName=eventName):
            context = {'message' : "You have already participated in the event !"}
            return render(request, 'Participant Registration.html', context)

        if reg_type == "Individual":
            number = 1
        
        if reg_type == "Group" and number == 1:
            temp = 'You have entered invalid number of people. Enter the number of people greater than 1'
            context = {'message' : temp}
            # print(part_email)
            return render(request, 'Participant Registration.html', context)    
        
        if Event.objects.all().filter(eventname = eventName):
            event = Part(name=name, contactnumber=contactnumber, part_email=part_email, password=password, eventName=eventName, reg_type=reg_type, number=number)
            event.save(contactnumber,contactnumber)
            
            for i in Event.objects.all().filter(eventname = eventName):
                i.nop = i.nop + number
                i.save()
        
        else:
            temp = 'Entered event name does not exists !!'
            context = {'message' : temp}
            # print(part_email)
            return render(request, 'Participant Registration.html', context)    

        # print(part_email)
        return render(request, 'Participant Registration.html', context)
    return render(request, 'Participant Registration.html')

def ContactUs(request):
    return HttpResponse("ContactUs")

def SignUp(request):
    return render(request, 'SignUp.html')

def EventDetails(request):
    event_list = Event.objects.all().filter(deadDate__gte = datetime.now())
    return render(request, 'Event Details.html', {'event_list':event_list})
    
    # return render(request, 'Event Details.html')

def SignUp(request):
    if request.method == "POST": 
        user_email = request.POST.get('user_email')
        user_password = request.POST.get('user_password')

        # if request.POST.get('person') == 'Host':
        if Event.objects.all().filter(host_email=user_email).exists() :#and Event.objects.get(host_email=user_email).password == user_password:
            context = {'event_list': Event.objects.all().filter(host_email=user_email),'allowed':'yes'}
            # print(context)
            # context1 = {}
            print(context)
            return render(request,'SignUp.html',context)  
        else:
            context = {'messages':"Username or password is incorrect !"}
            return render(request, 'SignUp.html', context)
        # else:
        #     if  Participant_Registration.objects.all().filter(email=hostid).exists() and Participant_Registration.objects.get(email=hostid).password == password:
        #         context = {'part_list': Participant_Registration.objects.all().filter(email=hostid)}
        #         return render(request, 'loginpage.html',context) 
        #     else:
        #         context = {'messages':"Username or password is incorrect !"}
        #         return render(request, 'loginpage.html', context)

        return render(request,"SignUp.html")
    else:
        return render(request,"SignUp.html",{'allowed':'no'})

def ParticipantList(request):
    if request.method == "POST": 
        user_event = request.POST.get('user_event')

        if Event.objects.all().filter(eventname=user_event).exists():
            part_list = Part.objects.all().filter(eventName=user_event)
            context = {'part_list':part_list, 'allowed':'no'}
            return render(request, 'Participant List.html', context)
        
        else:
            context = {'message' : "Wrong Event Id Evtered !! Go back and ReEnter Event Id"}
            return render(request, 'Participant List.html', context)
