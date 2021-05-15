from django.http import JsonResponse
from django.shortcuts import render

from .models import Compliment


# MARK: - Actions

def index(request):
    context = {'compliment': __get_new_compliment()}
    return render(request, 'compliments.html', context)


def get_new_compliment(request):
    if not request.is_ajax or request.method != 'GET':
        response = {'result': False, 'error': 'Request is not ajax or GET'}
        return JsonResponse(response, status=400)

    old_compliment_text = request.GET.get("old_compliment_text")
    new_compliment = __get_new_compliment(old_compliment_text)

    if not new_compliment:
        response = {'result': False, 'error': 'Cannot get new compliment'}
        return JsonResponse(response, status=500)

    response = {'result': True, 'new_compliment': new_compliment.text}
    return JsonResponse(response, status=200)


# MARK: - Helpers

def __get_new_compliment(old_compliment_text=None):
    while True:
        new_compliment = Compliment.get_random()

        if not new_compliment:
            break

        if new_compliment.text != old_compliment_text or Compliment.objects.count() == 1:
            return new_compliment
