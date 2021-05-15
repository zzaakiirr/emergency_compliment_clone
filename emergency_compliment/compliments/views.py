from django.http import HttpResponse

from .models import Compliment


def index(request):
    compliment = Compliment.get_random()
    return HttpResponse(f'{compliment.text}')
