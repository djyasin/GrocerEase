import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from app.models import User, List, Tag, ListItem
from app.serializers import ItemSerializer, ListSerializer, TagSerializer

class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {"tag": "Bulk Shopping"}
        response = self.client.post("/grocerease/create_tag/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)