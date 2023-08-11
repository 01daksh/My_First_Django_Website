from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Contact
# Create your views here.

def index(request):
    context = {
        'variable':"This is string"
    }
    return render(request, 'index.html', context)
    # return HttpResponse('Hello World!')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, phone=phone, desc = desc)
        contact.save()
        print(name, email, phone, desc, contact)

    return render(request, 'contacts.html')

def help(request):
    context = {
        'insert' : 'This is the added line'
    }
    return render(request, 'help.html', context=context)