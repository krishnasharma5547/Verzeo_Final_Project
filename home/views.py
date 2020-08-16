from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def project(request):
    return render(request,'project.html')

def publication(request):
    return render(request,'publication.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        print(name, email, phone)
        ins = Contact(name = name, email = email, phone = phone)
        ins.save()
        print('datat has been submitted')
    
    return render(request,'contact.html')

def whitebrickhome(request):
    return render(request, 'whitebrickhome.html')

def XSECELTIC(request):
    return render(request,'XSECELTIC.html')

def nordic(request):
    return render(request, 'nordic.html')

def classic(request):
    return render(request,'classic.html')

def kitchenpu(request):
    return render(request,'kitchenpu.html')
    
def composition(request):
    return render(request,'composition.html')

def natural(request):
    return render(request,'natural.html')

def kitchen(request):
    return render(request,'kitchen.html')

def minimalist(request):
    return render(request,'minimalist.html')

def mixing(request):
    return render(request,'mixing.html')

def modelrust(request):
    return render(request,'modelrust.html')

def whitwonwhite(request):
    return render(request,'whitwonwhite.html')

def XSapartments(request):
    return render(request,'XSapartments.html')

def bluish(request):
    return render(request,'bluish.html')