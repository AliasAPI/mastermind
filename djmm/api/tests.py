from django.test import TestCase
from .models import Backtest
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


# Create your tests here.

class ModelTestCase(TestCase):
    """This class defines the test suite for the backtest model"""

    def setUp(self):
        """Define the test client and other variables"""
        user = User.objects.create(username="nerd")
        self.backtest_name = "Write good tests"
        self.backtest_startcash = 1234.56
        self.backtest_duration = 233
        self.backtest_startquote = 1.33
        self.backtest_position = 1
        self.backtest_broker = "tradier"
        self.backtest_select_r = "no"
        self.backtest_diversify = "yes"
        self.backtest_hold = "no"
        self.backtest_margin = "yes"
        self.backtest_swing = "yes"
        self.backtest_positions = 1
        self.backtest_quantity = 20
        self.backtest_sharebuffer = 111
        self.backtest_profitlimitpercent = 10000
        self.backtest_stoplosspercentage = 1
        self.backtest_buystop_percentage = 100
        self.backtest_sellstoppercentage = 1
        self.backtest_trailingpercentage = 1
        self.backtest_buffer_test = 1

        self.backtest = Backtest(
        name=self.backtest_name,
        startcash=self.backtest_startcash,
        duration=self.backtest_duration,
        startquote=self.backtest_startquote,
        position=self.backtest_position,
        broker=self.backtest_broker,
        select_r=self.backtest_select_r,
        diversify=self.backtest_diversify,
        hold=self.backtest_hold,
        margin=self.backtest_margin,
        swing=self.backtest_swing,
        positions=self.backtest_positions,
        quantity=self.backtest_quantity,
        sharebuffer=self.backtest_sharebuffer,
        profitlimitpercent=self.backtest_profitlimitpercent,
        stoplosspercentage=self.backtest_stoplosspercentage,
        buystop_percentage=self.backtest_buystop_percentage,
        sellstoppercentage=self.backtest_sellstoppercentage,
        trailingpercentage=self.backtest_trailingpercentage,
        buffer_test=self.backtest_buffer_test,
        owner=user)


    def test_model_can_create_a_backtest(self):
        """Test whether the backtest model can create a backtest."""
        old_count = Backtest.objects.count()
        self.backtest.save()
        new_count = Backtest.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.backtest_data = {
        "name": "Server 1",
        "startcash": 1234.56,
        "duration": 233,
        "startquote": 1.33,
        "position": 1,
        "broker": "tradier",
        "select_r": "no",
        "diversify": "yes",
        "hold": "no",
        "margin": "yes",
        "swing": "yes",
        "positions": 1,
        "quantity": 20,
        "sharebuffer": 111,
        "profitlimitpercent": 10000,
        "stoplosspercentage": 1,
        "buystop_percentage": 100,
        "sellstoppercentage": 1,
        "trailingpercentage": 1,
        "buffer_test": 1,
        "owner": user.id}
        self.response = self.client.post(
            reverse('create'),
            self.backtest_data,
            format="json")

    def test_api_can_create_a_backtest(self):
        """Test the API has backtest creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get('/backtest/', kwargs={'pk': 3}, format="json")
        # self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_api_can_get_a_backtest(self):
        """Test to make sure the API can get a backtest"""
        backtest = Backtest.objects.get(id=1)
        response = self.client.get(
            '/backtest/',
            kwargs={'pk': backtest.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, backtest)


    def test_api_can_update_backtest(self):
        """Test to make sure the API can update a backtest"""
        backtest = Backtest.objects.get()
        change_backtest = {
        "name": "A new name",
        "startcash": 1234.56,
        "duration": 233,
        "startquote": 1.33,
        "position": 1,
        "broker": "tradier",
        "select_r": "no",
        "diversify": "yes",
        "hold": "no",
        "margin": "yes",
        "swing": "yes",
        "positions": 1,
        "quantity": 20,
        "sharebuffer": 111,
        "profitlimitpercent": 10000,
        "stoplosspercentage": 1,
        "buystop_percentage": 100,
        "sellstoppercentage": 1,
        "trailingpercentage": 1,
        "buffer_test": 1}
        res = self.client.put(
            reverse('details', kwargs={'pk': backtest.id}),
            change_backtest, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_api_can_delete_backtest(self):
        """Test to make sure the API can delete a backtest"""
        backtest = Backtest.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': backtest.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
