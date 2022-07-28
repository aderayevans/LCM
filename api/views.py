from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Champion
from api.serializers import ChampionSerializer

# Create your views here.

class ListCreateChampionView(ListCreateAPIView):
    model = Champion
    serializer_class = ChampionSerializer

    # List all
    def get_queryset(self):
        return Champion.objects.all()

    def post(self, request, *args, **kwargs):
        print(request.method)
        serializer = ChampionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.create()
            return JsonResponse({'message': 'Create a new Champion successful!',}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'message': 'Create a new Champion unsuccessful!'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteChampionView(RetrieveUpdateDestroyAPIView):
    model = Champion
    serializer_class = ChampionSerializer

    def get(self, request, *args, **kwargs):
        champion = get_object_or_404(Champion, id=kwargs.get('pk'))

        serializer = ChampionSerializer(instance=champion)
            
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        champion = get_object_or_404(Champion, id=kwargs.get('pk'))
        serializer = ChampionSerializer(instance=champion, data=request.data)

        if serializer.is_valid():
            serializer.update()
            return JsonResponse({'message': 'Update Champion successful!'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'message': 'Update Champion unsuccessful!'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        champion = get_object_or_404(Champion, id=kwargs.get('pk'))
        champion.delete()

        return JsonResponse({'message': 'Delete Champion successful!'}, status=status.HTTP_200_OK)