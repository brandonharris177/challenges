from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

month_responces = {
    "january" : "month of January",
    "february" : "month of February"
}

def monthly_challenge_by_number(request, month):
    try: 
        return HttpResponseRedirect("/challenges/" + list(month_responces.keys())[month-1])
    except:
        return HttpResponseNotFound("This month is not supported")

def monthly_challenge(request, month):
    try:
        return HttpResponse(month_responces[month])
    except:
        return HttpResponseNotFound("This month is not supported")