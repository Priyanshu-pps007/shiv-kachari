from django.shortcuts import render



def home(request):
    return render(request,'webapp/index.html')


def gallery(request):
    return render(request,'webapp/gallery.html')
# Create your views here.
def maps(request):
    return render(request,'webapp/map.html')
def about(request):
    return render(request,'webapp/about.html')