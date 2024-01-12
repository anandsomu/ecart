from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Item
from .api.serializers import ItemSerializer, ItemsTotalPriceSerializer


class YourAppTests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Obtain JWT token for the user
        self.token = self.get_jwt_token()

        # Create some items for testing
        self.item1 = Item.objects.create(name='Item 1', description='Description 1')
        self.item2 = Item.objects.create(name='Item 2', description='Description 2')

    def get_jwt_token(self):
        # Obtain a JWT token for the test user
        response = self.client.post('/api/v1/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['access']

    def test_item_list(self):
        # Ensure that the item list endpoint returns a 200 status code
        url = '/api/v1/items/'
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.get(url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure that the serialized data matches the expected data
        expected_data = ItemSerializer(Item.objects.all(), many=True).data
        self.assertEqual(response.data, expected_data)

    def test_item_price_sum(self):
        # Ensure that the item price sum endpoint returns a 200 status code
        url = '/api/v1/items/price/'
        headers = {'Authorization': f'Bearer {self.token}'}
        data = {'items': [self.item1.id, self.item2.id]}
        response = self.client.post(url, data, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure that the serialized data matches the expected data
        expected_data = ItemsTotalPriceSerializer({'items': [self.item1, self.item2]}).calculate_total()
        self.assertEqual(response.data, expected_data)
