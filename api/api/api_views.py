from rest_framework import viewsets
from rest_framework import pagination
from . import models
from . import serializers


class BicycleViewset(viewsets.ModelViewSet):
    queryset = models.Bicycle.objects.all()
    serializer_class = serializers.BicycleSerializer
    pagination_class=pagination.LimitOffsetPagination

class BicycletubeusageViewset(viewsets.ModelViewSet):
    queryset = models.Bicycletubeusage.objects.all()
    serializer_class = serializers.BicycletubeusageSerializer


class BikepartsViewset(viewsets.ModelViewSet):
    queryset = models.Bikeparts.objects.all()
    serializer_class = serializers.BikepartsSerializer


class BiketubesViewset(viewsets.ModelViewSet):
    queryset = models.Biketubes.objects.all()
    serializer_class = serializers.BiketubesSerializer


class CityViewset(viewsets.ModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


class ComponentViewset(viewsets.ModelViewSet):
    queryset = models.Component.objects.all()
    serializer_class = serializers.ComponentSerializer


class CustomerViewset(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class CustomertransactionViewset(viewsets.ModelViewSet):
    queryset = models.Customertransaction.objects.all()
    serializer_class = serializers.CustomertransactionSerializer


class GroupcomponentsViewset(viewsets.ModelViewSet):
    queryset = models.Groupcomponents.objects.all()
    serializer_class = serializers.GroupcomponentsSerializer


class GroupoViewset(viewsets.ModelViewSet):
    queryset = models.Groupo.objects.all()
    serializer_class = serializers.GroupoSerializer


class ManufacturerViewset(viewsets.ModelViewSet):
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer


class ManufacturertransactionViewset(viewsets.ModelViewSet):
    queryset = models.Manufacturertransaction.objects.all()
    serializer_class = serializers.ManufacturertransactionSerializer


class PaintViewset(viewsets.ModelViewSet):
    queryset = models.Paint.objects.all()
    serializer_class = serializers.PaintSerializer


class PurchaseitemViewset(viewsets.ModelViewSet):
    queryset = models.Purchaseitem.objects.all()
    serializer_class = serializers.PurchaseitemSerializer


class PurchaseorderViewset(viewsets.ModelViewSet):
    queryset = models.Purchaseorder.objects.all()
    serializer_class = serializers.PurchaseorderSerializer


class RetailstoreViewset(viewsets.ModelViewSet):
    queryset = models.Retailstore.objects.all()
    serializer_class = serializers.RetailstoreSerializer


class RevisionhistoryViewset(viewsets.ModelViewSet):
    queryset = models.Revisionhistory.objects.all()
    serializer_class = serializers.RevisionhistorySerializer


class SamplenameViewset(viewsets.ModelViewSet):
    queryset = models.Samplename.objects.all()
    serializer_class = serializers.SamplenameSerializer


class SamplestreetViewset(viewsets.ModelViewSet):
    queryset = models.Samplestreet.objects.all()
    serializer_class = serializers.SamplestreetSerializer


class TubematerialViewset(viewsets.ModelViewSet):
    queryset = models.Tubematerial.objects.all()
    serializer_class = serializers.TubematerialSerializer
