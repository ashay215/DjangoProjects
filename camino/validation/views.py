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

def loginpage(request):
    return render(request, 'validation/loginpage.html')

def confirmpin(request):
    print "CONFIRM PIN HERE!"
    # if request.method == 'POST':
    PINinput = int( request.POST.get('PINinput') )
    print "PIN retrieved from form: "
    print PINinput
    tempuser = get_object_or_404(User.objects.filter(temp=True))

    if tempuser.pin == PINinput:#checking if it is the most recent one
        print "PIN MATCH!"
        tempuser.temp = False
        tempuser.save()#marking in database as registered
        return render(request, 'validation/loginpage.html')

    else:
        return render(request, 'validation/confirmpin.html', {
            'error_message' : "PIN does not match!",
        })
        # try:
        #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # except (KeyError, Choice.DoesNotExist):
        #     # Redisplay the question voting form.
        #     return render(request, 'polls/detail.html', {
        #         'question': question,
        #         'error_message': "You didn't select a choice.",
        #     })



def verify(request):
    if request.method == 'POST':
        uname = request.POST.get('Name')
        pnumber = request.POST.get('PhoneNumber')
        cname = request.POST.get('ClassName')

        print "EEEEEEEEEEEEEEEE"
        print uname
        print pnumber
        print cname

        randompin = ''
        for i in range(4):
            randompin += `randint(0,9)`
        print randompin

        #do if blank then render with errormessage
        #trycatch
        newuser = User.objects.create(
             username = uname,
             classname = cname,
             phone = pnumber,
             pin = randompin,
             temp =True,
        )
        print "Created new User entry!"
        text = "Your verification PIN:"
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
