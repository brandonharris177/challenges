from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

month_responses = {
    "january" : "Challenge for January",
    "february" : "Challenge for February"
}

def index(request):
    months = list(month_responses.keys())
    print(months)
    return render(request, "challenges/index.html", {
        "month_list": months,
        })

def monthly_challenge_by_number(request, month):
    try: 
        return HttpResponseRedirect(reverse("string_month", args=[list(month_responses.keys())[month-1]]))
    except:
        return HttpResponseNotFound("This month is not supported")

def monthly_challenge(request, month):
    try:
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": month_responses[month]
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported<h1>")