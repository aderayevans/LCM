import json
from django.test import TestCase
from django.urls import reverse

from .models import Champion
from .serializers import ChampionSerializer

from rest_framework.test import APITestCase
# Create your tests here.

class ChampionApiCreateTest(APITestCase):

    # @classmethod
    # def setUpTestData(cls):
    # databases = {'default'}
    def setUp(self):
        self.first_champion = Champion.objects.create(name='Aatrox', sex='man', clan='Demons')
        self.second_champion = Champion.objects.create(name='Yasuo', sex='man', clan='Ionia')

        self.invalid_champion_pk = 3

        self.valid_post = {
            "name": "Jinx",
            "sex": "woman",
            "clan": "Zaun"
        }
        self.invalid_post = {
            "name": "",
            "sex": "woman",
            "clan": "Zaun"
        }

    def test_create_champions(self):
        # get API response 
        response = self.client.get(reverse('champions'))

        # get data from DB
        champion = Champion.objects.all()
        # convert it to JSON
        serializer = ChampionSerializer(champion, many=True)
        # check the status 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
        # check data row number
        self.assertEqual(Champion.objects.count(), 2)

    def test_create_a_champion_in_detail(self):
        response = self.client.get(reverse('champion-detail', kwargs={'pk': self.first_champion.pk}))
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['name'], 'Aatrox')
        self.assertEqual(data['sex'], 'man')
        self.assertEqual(data['clan'], 'Demons')

    def test_valid_update_post(self):
        response = self.client.put(
            reverse('champion-detail', kwargs={'pk': self.second_champion.pk}), 
            json.dumps(self.valid_post), 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        
    def test_invalid_update_post(self):
        response = self.client.put(
            reverse('champion-detail', kwargs={'pk': self.second_champion.pk}), 
            json.dumps(self.invalid_post), 
            content_type='application/json'
        )
        self.assertNotEqual(response.status_code, 200)

    def test_delete_invalid_id(self):
        response = self.client.delete(reverse('champion-detail', kwargs={'pk': self.invalid_champion_pk}))
        self.assertNotEqual(response.status_code, 200)

    def test_delete_valid_id(self):
        response = self.client.delete(reverse('champion-detail', kwargs={'pk': self.second_champion.pk}))
        self.assertEqual(response.status_code, 200)