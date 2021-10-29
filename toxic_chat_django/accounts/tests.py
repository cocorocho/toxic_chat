from django.test import TestCase, Client
from .models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class TestAccounts(TestCase):
    def setUp(self):
        pass

    def test_register(self):
        url = "/register/"
        client = Client()
        data = {
            "username": "janedoe",
            "password": "123456"
        }
        response = client.post(path=url, data=data)
        self.assertEqual(response.status_code, 200)

        data["username"] = "123712731723"
        response = client.post(path=url, data=data)
        self.assertEqual(response.status_code, 400)

        data["username"] = "_11"
        self.assertEqual(response.status_code, 400)

    def test_login(self):
        url = "/login/"
        client = Client()
        user = User.objects.create(username="janedoe")
        user.set_password("123456")
        user.save()
        data = {
            "username": "janedoe",
            "password": "123456"
        }
        response = client.post(url, data=data)
        user_token = Token.objects.get(user_id=user.id).key
        response_token = response.data["token"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_token, response_token)

        data["password"] = "81283182"
        response = client.post(url, data=data)
        self.assertEqual(response.status_code, 401)

    def test_logout(self):
        url = "/logout/"
        user = User.objects.create(username="janedoe")
        user.set_password("123456")
        user.save()
        token = Token.objects.create(user_id=user.id).key
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertRaises(
            Token.DoesNotExist,
            Token.objects.get,
            user_id=user.id
        )
        