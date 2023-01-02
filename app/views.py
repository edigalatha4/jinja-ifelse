from django.shortcuts import render

# Create your views here.
def ifelse(request):
    d={'a':180,'b':250}
    return render(request,'ifelse.html',d)
