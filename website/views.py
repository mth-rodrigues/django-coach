from django.shortcuts import render

# Create your views here.
def Coach(request):
    return render(request,'index.html')