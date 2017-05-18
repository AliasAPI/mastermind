from rest_framework import serializers
from .models import Backtest

class BacktestSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map the serializer's fields with the model fields."""
        model = Backtest
        fields = ('id',
                  'rank',
                  'godprofit',
                  'setprofit',
                  'startcash',
                  'godresult',
                  'startdate',
                  'duration',
                  'startquote',
                  'position',
                  'broker',
                  'select_r',
                  'symbols',
                  'diversify',
                  'hold',
                  'margin',
                  'swing',
                  'positions',
                  'quantity',
                  'sharebuffer',
                  'transactions',
                  'profitlimitpercent',
                  'stoplosspercentage',
                  'buystop_percentage',
                  'sellstoppercentage',
                  'trailingpercentage',
                  'buffer_test',

                  'name',
                  'owner',
                  'date_created',
                  'date_assigned',
                  'date_modified')
        read_only_fields = ('date_created', 'date_modified')
