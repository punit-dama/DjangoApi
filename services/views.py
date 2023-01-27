from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Order_details
from .serializers import Order_detailsSerializer, StatusSerializer


class OrdersView(APIView):

    def get(self, request, id):
        result = Order_details.objects.get(order_id=id)
        if id:  
            serializer = Order_detailsSerializer(result) 

            return Response({"Details":serializer.data}, status=200)  
        result = Order_details.objects.all()
        serializer = Order_detailsSerializer(result)
        return Response({"Details":serializer.data}, status=200)

    def post(self, request):
        serializer = Order_detailsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"order_id": serializer.data.get('order_id'),'order_amount': serializer.data.get('order_amount'), 'payment_url':"http://127.0.0.1:8000/payment/"+str(serializer.data.get('order_id'))},status = status.HTTP_200_OK)  
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class StatusView(APIView):
    def get(self, request, id):
        result = Order_details.objects.get(order_id=id)
        if id:  
            serializer = StatusSerializer(result) 

            return Response({"Details":serializer.data}, status=200)

        result = Order_details.objects.all()
        serializer = StatusSerializer(result)
        return Response({"Details":serializer.data}, status=200)
           
    

     
    