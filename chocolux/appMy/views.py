from django.shortcuts import render

# Create your views here.
def İndex(request):
    return render(request,'index.html')
def About(request):
    return render(request,'about.html')
def Contact(request):
    return render(request,'contact.html')
def Chocolate(request):
    return render(request,'chocolate.html')
def Testimonial(request):
    return render(request,'testimonial.html')