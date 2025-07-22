from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseRedirect


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
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except KeyError:
        return HttpResponseNotFound("this month is not supported")
    return HttpResponse(challenge_text)