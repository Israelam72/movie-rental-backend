from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PlansSerializer
from .models import Plans

# Create your views here.


@api_view(['GET'])
def get_plans(request):
    plans = Plans.objects.all()
    serializer = PlansSerializer(plans, many=True)
    return Response(serializer.data)
