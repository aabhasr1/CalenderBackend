from django.urls import path, re_path
from .views import ListEventsView, EventsDetailView, ListEventsForDateView

urlpatterns = [
    path('events/', ListEventsView.as_view(), name="event-all"),
    path('events/<int:id>/', EventsDetailView.as_view(), name="event-id"),
    re_path('events/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})/', ListEventsForDateView.as_view(),
            name="event-date"),
    re_path('events/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})/', ListEventsForDateView.as_view(),
            name="event-date")
]
