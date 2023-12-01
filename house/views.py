from django.shortcuts import render
from .serializers import Estateserializer, Bookingserializer
from .models import Estate
from .models import Booking
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView 
from rest_framework.permissions import IsAuthenticated



class homepage(ListCreateAPIView):
    queryset =Estate.objects.all()
    serializer_class =Estateserializer


class estate_detail_page(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Estate.objects.all()
    serializer_class = Estateserializer
    lookup_field = "slug"


# class homepage(ListCreateAPIView):
#     queryset = Booking.objects.get()
#     bookhouse = Bookingserializer 


# class estate_detail_page(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Booking.objects.get()
#     bookhouse = Bookingserializer
#     lookup_field = "slug"
    

# @api_view (["GET" , "POST"])
# def homepage(request):
#     if request.method == "GET":
#         estate= Estate.objects.all()
#         serializer= Estateserializer(estate, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = Estateserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response("all available houses")
#         else:
#             return Response('Available houses')
            
# @api_view(["GET" ,"PUT" ,"DELETE"]) 
# def estate_detail_page(request, input_slug):
#     if request.method == "GET":
#         current_estate = Estate.objects.get(slug=input_slug)
#         serialized_estate = Estateserializer(current_estate)
#         return Response(serialized_estate.data)
#     elif request.method =="PUT":
#         current_estate = Estate.objects.get(slug=input_slug) 
#         serialized_news = Estateserializer(current_estate, data=request.data, partial=True)
#         if serialized_estate.is_valid():
#             serialized_estate.save()
#             return Response("This is the house")
        #  else:
            #  return Response('Something went wrong')