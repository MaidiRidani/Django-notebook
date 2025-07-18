from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge_bynumber(request, month):
    return HttpResponse(month)
    

def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "eat something like fruit"
    elif month == 'february':
        challenge_text = "don't eat this day"
    elif month == 'march':
        challenge_text = "eat brief today"
    else:
        return HttpResponseNotFound("month not valid")
    return HttpResponse(challenge_text)