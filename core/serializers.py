from core.models import *
from rest_framework import serializers

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class BucketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketList
        fields = '__all__'

class FewPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = FewPoint
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CoverImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverImage
        fields = '__all__'
