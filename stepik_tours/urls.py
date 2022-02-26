from django.urls import path
from tours.views import main_view, departure_view, tour_view, custom_handler400, custom_handler403, custom_handler404, \
    custom_handler500

handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', main_view, name='main'),
    path("departure/<str:departure_id>/", departure_view, name='departure'),
    path("tour/<int:tour_id>", tour_view, name='tour'),
]
