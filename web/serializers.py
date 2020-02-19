from rest_framework import serializers
from . import models

class BicycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bicycle
        fields = "__all__"


class BicycletubeusageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bicycletubeusage
        fields = "__all__"
        
        
class BikepartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bikeparts
        fields = "__all__"


class BiketubesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Biketubes
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = "__all__"


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Component
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = "__all__"


class CustomertransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customertransaction
        fields = "__all__"


class GroupcomponentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Groupcomponents
        fields = "__all__"


class GroupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Groupo
        fields = "__all__"


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = "__all__"


class ManufacturertransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manufacturertransaction
        fields = "__all__"


class PaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paint
        fields = "__all__"


class PurchaseitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Purchaseitem
        fields = "__all__"


class PurchaseorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Purchaseorder
        fields = "__all__"


class RetailstoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Retailstore
        fields = "__all__"


class RevisionhistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Revisionhistory
        fields = "__all__"


class SamplenameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Samplename
        fields = "__all__"


class SamplestreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Samplestreet
        fields = "__all__"


class TubematerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tubematerial
        fields = "__all__"
