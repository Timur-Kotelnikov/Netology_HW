from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Adv


class AdvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adv
        fields = '__all__'
        read_only_fields = ['user', ]

    def validate(self, data):
        adv = Adv.objects.filter(user=self.context["request"].user, status=True)
        if len(adv) > 10:
            raise ValidationError('Oops')
        return data
