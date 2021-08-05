from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

month_responces = {
    "january" : "month of January",
    "february" : "month of February"
}

def index(request):
    months = list(month_responces.keys())
    response = ""
    for month in months:
        path = reverse("string_month", args = [month])
        response += f"<li><a href=\"{path}\">{month.capitalize()}<a/></li>"
    response_data = f"<ul>{response}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    try: 
        return HttpResponseRedirect(reverse("string_month", args=[list(month_responces.keys())[month-1]]))
    except:
        return HttpResponseNotFound("This month is not supported")

def monthly_challenge(request, month):
    try:
        return HttpResponse(render_to_string("challenges/challenge.html"))
    except:
        return HttpResponseNotFound("<h1>This month is not supported<h1>")