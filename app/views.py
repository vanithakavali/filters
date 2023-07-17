from django.shortcuts import render
import datetime
# Create your views here.
def built_in_filters(request):
    dt=datetime.datetime.now()
    d={'data':'I loVe My cOunTry','dt':dt,'c':1}
    return render(request,'built_in_filters.html',d)