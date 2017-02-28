from django.http import HttpResponse, HttpResponseRedirect, Http404
#from .models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import User
from django.views import generic
from random import randint
# from django.urls import reverse
from twilio.rest import TwilioRestClient


def index(request):
    return render(request, 'validation/index.html')

def login(request):
    return render(request, 'validation/retrieval.html')

def loginpage(request):
    return render(request, 'validation/loginpage.html')

def retrieval(request):
    pnumber = int(request.POST.get('PhoneNumber') )
    print "Phone retrieved from form: "
    print pnumber
    try:
        tempuser = User.objects.get(phone=pnumber)
        tempphone = tempuser.phone
        if pnumber == tempphone:
            print "Number confirmed!"

            randompin = ''
            for i in range(4):
                randompin += `randint(0,9)`
            print randompin

            request.session['username'] = tempuser.username
            request.session['classname'] = tempuser.classname
            request.session['phone'] =   tempphone
            request.session['pin'] =  randompin

            text = "Your verification PIN: "
            text+= `randompin`
            ACCOUNT_SID = "AC689b9870c4d29eba070ffccd0b133bf6"
            AUTH_TOKEN = "0688615be0d3415f952e6cb8ea0148f8"
            client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
            client.messages.create(
                to=pnumber,
                from_="2139081961",
                body=text,
            )

            print "TEXT SENT"

            return render(request, 'validation/confirmpin.html')

    except User.DoesNotExist:
        return render(request, 'validation/retrieval.html', {
            'error_message' : "Phone does not exist in database!",
        })
    except User.MultipleObjectsReturned:
        return render(request, 'validation/retrieval.html', {
            'error_message' : "Multiple users found with this phone number!",
        })

def confirmpin(request):
    PINinput = int( request.POST.get('PINinput') )
    print "PIN retrieved from form: "
    print PINinput

    try:
        if request.session.has_key('username'):
          uname = request.session['username']
        if request.session.has_key('classname'):
          cname = request.session['classname']
        if request.session.has_key('phone'):
          pnumber = request.session['phone']

        if request.session.has_key('pin'):
            pin = int(request.session['pin'])

            if pin == PINinput:#checking
                print "PIN MATCH!"
                newuser = User.objects.create(
                     username = uname,
                     classname = cname,
                     phone = pnumber,
                )
                print "Created new USER!"
                request.session.flush()
                return render(request, 'validation/loginpage.html',{
                    'username': uname,
                    'classname': cname,
                    'phone': pnumber,
                })

            else:
                return render(request, 'validation/confirmpin.html', {
                    'error_message' : "PIN does not match!",
                })
        else:
            return render(request, 'validation/confirmpin.html', {
                'error_message' : "Something went wrong- no PIN in session!",
            })

    except KeyError:
        print "KeyError caught!"
        return render(request, 'validation/confirmpin.html', {
            'error_message' : "Something went wrong!",
        })

def verify(request):

    if request.method == 'POST':
        uname = request.POST.get('Name')
        pnumber = int(request.POST.get('PhoneNumber'))
        cname = request.POST.get('ClassName')
        # print uname
        # print pnumber
        # print cname
        try:
            test = User.objects.get(phone=pnumber)
            return render(request, 'validation/index.html', {
                'error_message' : "Another user already has this phone number!",
            })

        except User.DoesNotExist:
            print "Phone Number valid!"

        randompin = ''
        for i in range(4):
            randompin += `randint(0,9)`
        print randompin

        request.session['username'] = uname
        request.session['classname'] = cname
        request.session['phone'] =  pnumber
        request.session['pin'] = randompin

        text = "Your verification PIN: "
        text+= `randompin`

        ACCOUNT_SID = "AC689b9870c4d29eba070ffccd0b133bf6"
        AUTH_TOKEN = "0688615be0d3415f952e6cb8ea0148f8"
        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
        client.messages.create(
            to=pnumber,
            from_="2139081961",
            body=text,
        )

        print "TEXT SENT"

    return render(request, 'validation/confirmpin.html')
