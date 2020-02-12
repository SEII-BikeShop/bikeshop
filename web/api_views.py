from rest_framework import viewsets
from . import models
from . import serializers


class BicycleViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Bicycle.objects.all()
        serializer_class = serializers.BicycleSerializer


class BicycletubeusageViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Bicycletubeusage.objects.all()
        serializer_class = serializers.BicycletubeusageSerializer


class BikepartsViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Bikeparts.objects.all()
        serializer_class = serializers.BikepartsSerializer


class BiketubesViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Biketubes.objects.all()
        serializer_class = serializers.BiketubesSerializer


class CityViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.City.objects.all()
        serializer_class = serializers.CitySerializer


class CommonsizesViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Commonsizes.objects.all()
        serializer_class = serializers.CommonsizesSerializer


class ComponentViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Component.objects.all()
        serializer_class = serializers.ComponentSerializer


class ComponentnameViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Componentname.objects.all()
        serializer_class = serializers.ComponentnameSerializer


class CustomerViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Customer.objects.all()
        serializer_class = serializers.CustomerSerializer


class EmployeeViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Employee.objects.all()
        serializer_class = serializers.EmployeeSerializer


class CustomertransactionViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Customertransaction.objects.all()
        serializer_class = serializers.CustomertransactionSerializer


class GroupcomponentsViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Groupcomponents.objects.all()
        serializer_class = serializers.GroupcomponentsSerializer


class GroupoViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Groupo.objects.all()
        serializer_class = serializers.GroupoSerializer


class LetterstyleViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Letterstyle.objects.all()
        serializer_class = serializers.LetterstyleSerializer


class ManufacturerViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Manufacturer.objects.all()
        serializer_class = serializers.ManufacturerSerializer


class ManufacturertransactionViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Manufacturertransaction.objects.all()
        serializer_class = serializers.ManufacturertransactionSerializer


class ModelsizeViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Modelsize.objects.all()
        serializer_class = serializers.ModelsizeSerializer


class ModeltypeViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Modeltype.objects.all()
        serializer_class = serializers.ModeltypeSerializer


class PaintViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Paint.objects.all()
        serializer_class = serializers.PaintSerializer


class PreferenceViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Preference.objects.all()
        serializer_class = serializers.PreferenceSerializer


class PurchaseitemViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Purchaseitem.objects.all()
        serializer_class = serializers.PurchaseitemSerializer


class PurchaseorderViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Purchaseorder.objects.all()
        serializer_class = serializers.PurchaseorderSerializer


class RetailstoreViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Retailstore.objects.all()
        serializer_class = serializers.RetailstoreSerializer


class RevisionhistoryViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Revisionhistory.objects.all()
        serializer_class = serializers.RevisionhistorySerializer


class SamplenameViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Samplename.objects.all()
        serializer_class = serializers.SamplenameSerializer


class SamplestreetViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Samplestreet.objects.all()
        serializer_class = serializers.SamplestreetSerializer


class StatetaxrateViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Statetaxrate.objects.all()
        serializer_class = serializers.StatetaxrateSerializer


class TempdatemadeViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Tempdatemade.objects.all()
        serializer_class = serializers.TempdatemadeSerializer


class TubematerialViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Tubematerial.objects.all()
        serializer_class = serializers.TubematerialSerializer


class WorkareaViewset(viewsets.ModelViewSet):
    class Meta:
        queryset = models.Workarea.objects.all()
        serializer_class = serializers.WorkareaSerializer
