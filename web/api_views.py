from rest_framework import viewsets
from . import models
from . import serializers


class BicycleViewset(viewsets.ModelViewSet):
    queryset = models.Bicycle.objects.all()
    serializer_class = serializers.BicycleSerializer


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


class CommonsizesViewset(viewsets.ModelViewSet):
    queryset = models.Commonsizes.objects.all()
    serializer_class = serializers.CommonsizesSerializer


class ComponentViewset(viewsets.ModelViewSet):
    queryset = models.Component.objects.all()
    serializer_class = serializers.ComponentSerializer


class ComponentnameViewset(viewsets.ModelViewSet):
    queryset = models.Componentname.objects.all()
    serializer_class = serializers.ComponentnameSerializer


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


class LetterstyleViewset(viewsets.ModelViewSet):
    queryset = models.Letterstyle.objects.all()
    serializer_class = serializers.LetterstyleSerializer


class ManufacturerViewset(viewsets.ModelViewSet):
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer


class ManufacturertransactionViewset(viewsets.ModelViewSet):
    queryset = models.Manufacturertransaction.objects.all()
    serializer_class = serializers.ManufacturertransactionSerializer


class ModelsizeViewset(viewsets.ModelViewSet):
    queryset = models.Modelsize.objects.all()
    serializer_class = serializers.ModelsizeSerializer


class ModeltypeViewset(viewsets.ModelViewSet):
    queryset = models.Modeltype.objects.all()
    serializer_class = serializers.ModeltypeSerializer


class PaintViewset(viewsets.ModelViewSet):
    queryset = models.Paint.objects.all()
    serializer_class = serializers.PaintSerializer


class PreferenceViewset(viewsets.ModelViewSet):
    queryset = models.Preference.objects.all()
    serializer_class = serializers.PreferenceSerializer


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


class StatetaxrateViewset(viewsets.ModelViewSet):
    queryset = models.Statetaxrate.objects.all()
    serializer_class = serializers.StatetaxrateSerializer


class TempdatemadeViewset(viewsets.ModelViewSet):
    queryset = models.Tempdatemade.objects.all()
    serializer_class = serializers.TempdatemadeSerializer


class TubematerialViewset(viewsets.ModelViewSet):
    queryset = models.Tubematerial.objects.all()
    serializer_class = serializers.TubematerialSerializer


class WorkareaViewset(viewsets.ModelViewSet):
    queryset = models.Workarea.objects.all()
    serializer_class = serializers.WorkareaSerializer
