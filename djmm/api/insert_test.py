from .parameters import CreateTestParameters
from .models import Backtest
from django.contrib.auth.models import User


p = CreateTestParameters()

test_parameters = {
    # rank
    # godprofit
    # setprofit
    'startcash' : p.startcash,

    # godresult
    # startdate
    'duration' : p.duration,
    'startquote' : p.startquote,
    'position' : p.position,
    'broker' : p.broker,
    'select_r' : p.select_r,
    # symbols
    'diversify' : p.diversify,
    'hold' : p.hold,
    'margin' : p.margin,
    'swing' : p.swing,
    'positions' : p.positions,
    'quantity' : p.quantity,
    'sharebuffer' : p.sharebuffer,
    # transactions
    'profitlimitpercent' : p.profitlimitpercent,
    'stoplosspercentage' : p.stoplosspercentage,
    'buystop_percentage' : p.buystop_percentage,
    'sellstoppercentage' : p.sellstoppercentage,
    'trailingpercentage' : p.trailingpercentage,
    'buffer_test' : p.buffer_test}

# print(test_parameters)

# u = User.objects.all().values_list('username', flat=True)
# print(owner)

# user = User.objects.create(username="root")
user = User.objects.get(username="root")
# print(user)

bt = Backtest(owner=user, **test_parameters)
bt.save()

# print(Backtest.objects.all())
