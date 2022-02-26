from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError
from random import sample
from tours.data import tours, subtitle, description, departures
from tours.services import tours_by_departure


def main_view(request):
    tours_random = {k: tours[k] for k in sample(range(1, len(tours) + 1), k=6)}
    return render(request, 'index.html', context={
        'subtitle': subtitle, 'description': description,
        'tours_random': tours_random,
    })


def departure_view(request, departure_id):
    departure = departures.get(departure_id)
    tour = tours_by_departure(tours, departure_id)
    return render(request, 'departure/departure.html', context={
        'departure': departure, 'tour': tour,
    })


def tour_view(request, tour_id):
    tour = tours.get(tour_id)
    return render(request, 'tour/tour.html', context={
        'tour': tour,
    })


def custom_handler400(request, exception):
    return HttpResponseBadRequest('Неверный запрос!')


def custom_handler403(request, exception):
    return HttpResponseForbidden('Доступ запрещен!')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
