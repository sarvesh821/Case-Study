from django.http import HttpResponse
from django.shortcuts import render

def Choose_role(request):
    return render(request,'choose.html')
