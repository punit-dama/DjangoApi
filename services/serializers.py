from rest_framework import serializers
from . models import Order_details


class Order_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_details
        fields = ("order_id", "order_amount","status")


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_details
        fields = ("order_id", "status")
