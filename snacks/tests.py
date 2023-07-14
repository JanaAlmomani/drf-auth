from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Snack


# Create your tests here.

class SnackTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_thing = Snack.objects.create(title='chips', purchaser=testuser1, description="test desc ...")
        test_thing.save()

    def setUp(self):
        self.client.login(username="testuser1", password="pass")

    def snacks_model(self):
        snack = Snack.objects.get(id=1)
        actual_purchaser= str(Snack.purchaser)
        actual_title = str(Snack.title)
        actual_description = str(Snack.description)
        self.assertEqual(actual_purchaser,"testuser1")
        self.assertEqual(actual_title,"chips")
        self.assertEqual(actual_description,"test desc ...")

    def test_get_snacks_list(self):
        url = reverse("snacks_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snacks = response.data
        self.assertEqual(len(snacks), 1)
        self.assertEqual(snacks[0]["title"], "chips")

    def test_get_snack_by_id(self):
        url = reverse("snack_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snack = response.data
        self.assertEqual(snack["title"], "chips")

    def test_update_snack(self):
        url = reverse("snack_detail", args=(1,))
        data = {
            "purchaser": 1,
            "title": "cookies",
            "description": "test test  test .....................",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snack = Snack.objects.get(id=1)
        self.assertEqual(snack.title, data["title"])
        self.assertEqual(snack.purchaser.id, data["purchaser"])
        self.assertEqual(snack.description, data["description"])

    def test_delete_snack(self):
        url = reverse("snack_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        things = Snack.objects.all()
        self.assertEqual(len(things), 0)

    def test_authentication_required(self):
        self.client.logout()
        url = reverse("snacks_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        