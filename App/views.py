from django.shortcuts import render

# Create your views here.
def Condition(request):
    d={'a':20,'b':30,'c':15}
    return render(request,'Condition.html',d)