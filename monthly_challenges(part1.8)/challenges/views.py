from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat something like fruit",
    "february": "Don't eat this day",
    "march": "Eat briefly today",
    "april": "Try a new healthy recipe",
    "may": "Go for a walk every morning",
    "june": "Drink 2 liters of water daily",
    "july": "No sugary snacks for a week",
    "august": "Cook your own meals all week",
    "september": "Eat more vegetables",
    "october": "Avoid fast food",
    "november": "Practice mindful eating",
    "december": "Reflect on your eating habits"
}


def monthly_challenge_bynumber(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("this month is not supported")

    redirect_month = months[month-1]
    month_reverse = reverse("month-url", args=[redirect_month])
    return HttpResponseRedirect(month_reverse)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        respondata = f"<h1>{challenge_text}</h1>"
        return HttpResponse(respondata)
    except KeyError:
        return HttpResponseNotFound("<h1>this month is not supported</h1>")