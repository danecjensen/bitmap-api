```python
from django.test import TestCase
from .models import Command
from .serializers import CommandSerializer
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .views import ListCreateCommands

# tests for views
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_command(name="", payload=""):
        if name != "" and payload != "":
            Command.objects.create(name=name, payload=payload)

    def setUp(self):
        # add test data
        self.create_command("test1", "payload1")
        self.create_command("test2", "payload2")
        self.create_command("test3", "payload3")
        self.create_command("test4", "payload4")

class GetAllCommandsTest(BaseViewTest):

    def test_get_all_commands(self):
        """
        This test ensures that all commands added in the setUp method
        exist when we make a GET request to the commands/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("commands-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Command.objects.all()
        serialized = CommandSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
```