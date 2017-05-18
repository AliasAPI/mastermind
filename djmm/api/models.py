from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


class Backtest(models.Model):
    """This class represents the backtest model."""

    # id int(10)
    # rank int(11)
    rank = models.SmallIntegerField(blank=True, null=True)
    # godprofit int(11)
    godprofit = models.SmallIntegerField(blank=True, null=True)
    # setprofit int(11)
    setprofit = models.SmallIntegerField(blank=True, null=True)
    # startcash decimal(10,2)
    startcash = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    # godresult decimal(10,2)
    godresult = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # startdate datetime
    startdate = models.DateField(null=False, blank=False)
    #duration int(5)
    duration = models.SmallIntegerField(blank=False, null=False)
    # startquote decimal(10,2)
    startquote = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    # position int(3)
    position = models.SmallIntegerField(blank=False, null=False)
    # broker varchar(10)
    broker = models.CharField(max_length=10, blank=False, null=False, unique=False)
    # select_r varchar(10)
    select_r = models.CharField(max_length=3, blank=False, null=False, unique=False)
    # symbols varchar(600)
    symbols = models.TextField(default='', blank=True)
    # diversify varchar(3)
    diversify = models.CharField(max_length=3, blank=False, unique=False)
    # hold varchar(3)
    hold = models.CharField(max_length=3, blank=False, unique=False)
    # margin varchar(3)
    margin = models.CharField(max_length=3, blank=False, unique=False)
    # swing varchar(3)
    swing = models.CharField(max_length=3, blank=False, null=False, unique=False)
    # positions int(3)
    positions = models.SmallIntegerField(blank=False, null=False)
    # quantity int(3)
    quantity = models.SmallIntegerField(blank=False, null=False)
    # sharebuffer int(11)
    sharebuffer = models.SmallIntegerField(blank=False, null=False)
    # transactions int(11)
    transactions = models.SmallIntegerField(blank=True, null=True)
    # profitlimitpercent int(3)
    profitlimitpercent = models.SmallIntegerField(blank=False, null=False)
    # stoplosspercentage int(3)
    stoplosspercentage = models.SmallIntegerField(blank=False, null=False)
    # buystop_percentage int(3)
    buystop_percentage = models.SmallIntegerField(blank=False, null=False)
    # sellstoppercentage int(3)
    sellstoppercentage = models.SmallIntegerField(blank=False, null=False)
    # trailingpercentage int(3)
    trailingpercentage  = models.SmallIntegerField(blank=False, null=False)
    # buffer_test int(3)
    buffer_test = models.SmallIntegerField(blank=False, null=False)

    # name User authorized to write to this test
    name = models.CharField(max_length=255, blank=False, unique=False)
    owner = models.ForeignKey(
        'auth.User',
    related_name='backtest',
    on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    # date_assigned Update right after the test parameters are returned to the test server
    # date_assigned = models.DateTimeField(auto_now=True)
    date_assigned = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


# This receiver handles token creation immediately a new user is created.
# Note that the receiver is NOT indented inside the Bucketlist model class.
# It's a common mistake to indent it inside the class.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
