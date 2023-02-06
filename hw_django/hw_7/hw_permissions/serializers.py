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
        print(adv)
        print(len(adv))
        if len(adv) > 9 and self.context['request'].method == 'POST':
            raise ValidationError('You dont have permissions to have 10 or more adv at the same time')
        return data
