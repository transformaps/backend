# -*- coding: utf-8 -*-
# Serializers define the API representation.

from rest_framework_gis.serializers import GeoFeatureModelSerializer
from maps.models import Map, Feature


class MapSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Map
        geo_field = 'bbox'
        fields = ('name', 'bbox', 'public', 'editable')


class FeatureSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Feature
        geo_field = 'geo'
        fields = ('geo', 'map', 'id')
