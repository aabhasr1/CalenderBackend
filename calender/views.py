from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
import datetime

from .decorators import validate_request_data
from .models import Event
from .serializers import EventSerializer


# Create your views here.

class ListEventsView(generics.ListAPIView):
    """
        GET events/
        POST events/
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @validate_request_data
    def post(self, request, *args, **kwargs):
        a_event = Event.objects.create(
            id=request.data["id"],
            title=request.data["title"],
            date=request.data["date"],
            fav=request.data["fav"],
            active=request.data["active"],
            startField=request.data["startField"],
            endField=request.data["endField"]
        )
        return Response(
            data=EventSerializer(a_event).data,
            status=status.HTTP_201_CREATED
        )


class ListEventsForDateView(generics.RetrieveAPIView):
    """
    GET events/:date/
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request, *args, **kwargs):
        if 'day' in kwargs:
            date_str = '{}-{}-{}'.format(kwargs["year"], kwargs["month"], kwargs["day"])  # The date - 2017 Dec 29
            format_str = '%Y-%m-%d'  # The format
            case = 1
        else:
            date_str = '{}-{}'.format(kwargs["year"], kwargs["month"])  # The date - 2017 Dec 29
            format_str = '%Y-%m'  # The format
            case = 2
        try:
            if case == 1:
                date = datetime.datetime.strptime(date_str, format_str)
                queryset = self.queryset.filter(date=date.date())
            else:
                date = datetime.datetime.strptime(date_str, format_str)
                queryset = self.queryset.filter(date__year=date.year,
                                                date__month=date.month)
            return Response(EventSerializer(queryset, many=True).data)
        except Event.DoesNotExist:
            return self.Response404(date_str)

    def Response404(self, date):
        return Response(
            data={
                "message": "Events for date: {} does not exist".format(date)
            },
            status=status.HTTP_404_NOT_FOUND
        )


class EventsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET events/:id/
    PUT events/:id/
    DELETE events/:id/
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_event = self.queryset.get(id=kwargs["id"])
            return Response(EventSerializer(a_event).data)
        except Event.DoesNotExist:
            return self.Response404(**kwargs)

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            a_event = self.queryset.get(id=kwargs["id"])
            serializer = EventSerializer()
            updated_song = serializer.update(a_event, request.data)
            return Response(EventSerializer(updated_song).data)
        except Event.DoesNotExist:
            return self.Response404(**kwargs)

    def delete(self, request, *args, **kwargs):
        try:
            a_event = self.queryset.get(id=kwargs["id"])
            a_event.delete()
            return Response(data="success",
                            status=status.HTTP_204_NO_CONTENT)
        except Event.DoesNotExist:
            return self.Response404(**kwargs)

    def Response404(self, **kwargs):
        return Response(
            data={
                "message": "Event with id: {} does not exist".format(kwargs["id"])
            },
            status=status.HTTP_404_NOT_FOUND
        )
