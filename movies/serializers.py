from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg

class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        return round(rate, 1) if rate is not None else None

    def validate_release_date(self, value):
        if value.year < 1999:
            raise serializers.ValidationError('O ano de lançamento não pode ser inferior a 1999.')
        return value

    def validate_title(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('O titulo não pode ter mais que 200 caracteres.')
        return value
