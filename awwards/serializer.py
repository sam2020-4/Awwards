from rest_framework import serializers
from .models import Projects

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('project_title', 'project_image', 'project_description','pub_date','Author','link','country')

