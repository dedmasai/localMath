from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def process_get_view(request:HttpRequest)->HttpResponse:
    context={
    }
    return render(request, "requestdataapp/request_querry_params.html", context=context)