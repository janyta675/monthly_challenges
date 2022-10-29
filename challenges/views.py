from django.http.response import HttpResponse,HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges={
    "january":"eat no meat for the entire month",
    "february":"walk for at-least 20 mins everyday ",
    "march":None,
    "april":"eat no meat for the entire month",
    "may":"walk for at-least 20 mins everyday ",
    "june":"learn django for 20 mins everyday",
    "july":"eat no meat for the entire month",
    "august":"walk for at-least 20 mins everyday ",
    "september":"learn django for 20 mins everyday",
    "october":"eat no meat for the entire month",
    "november":"walk for at-least 20 mins everyday ",
    "december":"learn django for 20 mins everyday"
    }

def index(request):
    months=list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{"months":months})

def monthly_challenge_by_number(request,month):
    months=list(monthly_challenges.keys())
    if month>len(months):
        return HttpResponseNotFound("invalid Month")
    redirect_month=months[month-1]
    month_path=reverse('monthly_challenges', args=[redirect_month])
    return HttpResponseRedirect(month_path)

def monthly_challenge(request, month):
    try:
        challenge_text=monthly_challenges[month]
        return render(request,'challenges/challenge.html',{
            "challenge_text":challenge_text,"month":month})
        # response_data=render_to_string('challenges/challenge.html')
    except:
        # response_data=render_to_string('404.html')
        # return HttpResponseNotFound(response_data)
        # raise the error we don't return it
        raise Http404()