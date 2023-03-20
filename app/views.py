from django.shortcuts import render

# Create your views here.


def image(request):
    return render(request,'image_insertion.html')
