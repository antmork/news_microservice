from rest_framework import serializers
from NewsApp.models import News

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model= News
        fields= '__all__'
