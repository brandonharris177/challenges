from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

month_responces = {
    "january" : "month of January",
    "february" : "month of February"
}

def monthly_challenge(request, month):
    if month in month_responces:
        return HttpResponse(month_responces[month])
    return HttpResponseNotFound("This month is not supported")