from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'myObj':'text from the server side'}
    return render(request, 'tracker/index.htm',context=context)

def process_request(request):
    a = request.GET['ticket_number']
