from django.shortcuts import render


def main_view(request):
    return render(request, 'index.html', )


def departure_view(request, str):
    return render(request, 'departure/departure..html')


def tour_view(request, id):
    return render(request, 'tour/tour.html')