from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Event
from .serializer import EventSerializer


def success_response(id):
    return {
        'result': 'success',
        'id': id,
    }


def error_response():
    return {
        'result': 'error',
        'error_code': 'wrong_data'
    }


class EventViewAll(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        events = Event.objects.filter(author=request.user.id)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        event = request.data
        event['author'] = request.user.id
        serializer = EventSerializer(data=event)
        if serializer.is_valid(raise_exception=True):
            event_in_base = serializer.save()
            return Response(success_response(event_in_base.id))
        return Response(error_response())


class EventView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        event = get_object_or_404(Event, id=id, author=request.user.id)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def delete(self, request, id):
        event = get_object_or_404(Event, id=id, author=request.user.id)
        event.delete()
        return Response(success_response(id), status=204)

    def put(self, request, id):
        event_in_base = get_object_or_404(Event, id=id, author=request.user.id)
        data = request.data
        serializer = EventSerializer(event_in_base, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            event_in_base = serializer.save()
            return Response(success_response(event_in_base.id))
        return Response(error_response())
