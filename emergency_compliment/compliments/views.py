import random

from django.http import JsonResponse
from django.shortcuts import render

from .models import Compliment


# MARK: - Actions

def index(request):
    context = {'compliment': __get_new_compliment()}
    __set_bg_color(request.session)
    return render(request, 'index.html', context)


def get_new_compliment(request):
    if not request.is_ajax or request.method != 'GET':
        response = {'result': False, 'error': 'Request is not ajax or GET'}
        return JsonResponse(response, status=400)

    old_compliment_text = request.GET.get("old_compliment_text")
    new_compliment = __get_new_compliment(old_compliment_text)

    if not new_compliment:
        response = {'result': False, 'error': 'Cannot get new compliment'}
        return JsonResponse(response, status=500)

    __set_bg_color(request.session)
    response = {
        'result': True,
        'new_compliment': new_compliment.text,
        # FIX: For some reason JS reads 'bg_color' from session as old value
        #      So we send it back for further config in JS
        'bg_color': request.session.get('bg_color'),
    }
    return JsonResponse(response, status=200)


# MARK: - Helpers

def __get_new_compliment(old_compliment_text=None):
    while True:
        new_compliment = Compliment.get_random()

        if not new_compliment:
            break

        if new_compliment.text != old_compliment_text or Compliment.objects.count() == 1:
            return new_compliment


def __set_bg_color(session):
    BG_COLORS = ['#F2ED53', '#E5B156', '#B4CF4E']
    current_bg_color = session.get('bg_color')

    if not current_bg_color:
        session['bg_color'] = BG_COLORS[0]
        return

    session['bg_color'] = random.choice(
        [color for color in BG_COLORS if color != current_bg_color]
    )
