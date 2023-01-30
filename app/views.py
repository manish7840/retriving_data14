from django.shortcuts import render

# Create your views here.

from app.models import *

def display_topics(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)
    QSW=Webpage.objects.filter(topic_name='cricket')
    QSW=Webpage.objects.exclude(topic_name='cricket')
    QSW=Webpage.objects.all()[:5:]
    QSW=Webpage.objects.filter(url__startswith='https')
    
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)

def display_access(request):
    QSA=AccessRecords.objects.all().order_by('date')
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date='1998-08-10')    
    QSA=AccessRecords.objects.filter(date__gt='1998-08-10')    
    QSA=AccessRecords.objects.filter(date__gte='1998-08-10') 
    QSA=AccessRecords.objects.filter(date__lte='1998-08-10')
    QSA=AccessRecords.objects.all()