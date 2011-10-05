# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from mixed.models import PageBase, PageWithBodyText, PageWithLink
from easymode.tree.xml.serializers import RecursiveXmlSerializer

def index(request):
    context = {
        'all': PageBase.objects.all(),
        'body':PageWithBodyText.objects.all(),
        'link':PageWithLink.objects.all(),
    }
    return render_to_response('index.html', context)

def feed(request):
    ser = RecursiveXmlSerializer()
    return HttpResponse(ser.serialize(PageBase.objects.all()), mimetype='text/xml')