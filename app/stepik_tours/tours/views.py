
from django.conf import settings
from django.shortcuts import render
from django.views import View
import random
from .data import *


class MainView(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'tours/index.html', {
                    'title': title, 'subtitle': subtitle, 'description': description,
                    'departures': departures, 'tours': dict(random.sample(tours.items(), 6))})


class DepartureView(View):
    def get(self, request, departure, *args, **kwargs):
        count_city = 0
        price_min = 1000000
        price_max = 0
        day_min = 1000000
        day_max = 0
        city = departures.setdefault(departure)
        tours_city = {}
        for tour_id, tour in tours.items():
            if tour.setdefault('departure') == departure:
                tours_city.update({tour_id: tour})
                count_city += 1
                if tour.setdefault('price') < price_min:
                    price_min = tour.setdefault('price')
                if tour.setdefault('price') > price_max:
                    price_max = tour.setdefault('price')
                if tour.setdefault('nights') < day_min:
                    day_min = tour.setdefault('nights')
                if tour.setdefault('nights') > day_max:
                    day_max = tour.setdefault('nights')

        return render(request, 'tours/departure.html', {
                    'title': title, 'subtitle': subtitle, 'description': description,
                    'departures': departures, 'tour': tours, 'tours_city': tours_city,
                    'count_city': count_city, 'day_min': day_min, 'day_max': day_max,
                    'price_min': price_min, 'price_max': price_max, 'city': city})


class TourView(View):

    def get(self, request, id, *args, **kwargs):
        tour = tours[id]
        keyname = tour.setdefault('departure')
        city = departures.setdefault(keyname)

        return render(request, 'tours/tour.html', {
                    'title': title, 'subtitle': subtitle, 'description': description,
                    'departures': departures, 'tour': tour, 'city': city})
