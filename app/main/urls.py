from django.urls import path

from .views import EventViewAll, EventView


urlpatterns = [
    path('event/', EventViewAll.as_view(), name='event_all'),
    path('event/<int:id>/', EventView.as_view(), name='event_single'),
]
