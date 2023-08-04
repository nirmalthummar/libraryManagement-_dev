from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app_admin_view(request):
    
    template='<h1>This is html</h1>'
    return HttpResponse(template)
