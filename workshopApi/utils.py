import hashlib
import json
import string
from random import random

from django.http import JsonResponse
from rest_framework import status

from workshopApi.api.serializers import base64_encode
from workshopApi.models import Client, Platform


def check_if_client_got_remaining_requests(client: Client):
    if client is not None:
        if client.nbOfAvailableRequests > 0:
            return True
        elif client.nbOfAvailableRequests == 0:
            client.active = False
            client.save()
            return False


def check_api_key_for_client(client: Client, apiKey):
    if client is not None:
        return client.apiKey == hashlib.sha256(apiKey.encode("utf-8")).hexdigest()


def generate_new_apiKey(client: Client):
    raw_api_key = "".join(random.choices(string.ascii_lowercase, k=50))
    response = {
        "raw_api_key": raw_api_key,
    }
    hash_object = hashlib.sha256(raw_api_key.encode("utf-8"))
    response["hashed_api_key"] = hash_object.hexdigest()
    client.apiKey = response["hashed_api_key"]
    response["user_email"] = client.email
    client.save()
    return response


def get_body_from_post_request(request, key):
    try:
        return json.loads(request.body.decode("utf-8"))[str(key)]
    except KeyError:
        return None
    except ValueError:
        return None


def get_client_from_admin_key_and_mail(request):
    data = json.loads(request.body.decode("utf-8"))
    try:
        platform = Platform.objects.get(adminKey=base64_encode(data.get("adminKey")))
    except Platform.DoesNotExist:
        return JsonResponse(
            "Platform not found", status=status.HTTP_404_NOT_FOUND, safe=False
        )

    try:
        client = Client.objects.get(email=data.get("email"), platform=platform)
    except Client.DoesNotExist:
        return JsonResponse(
            "client not found",
            status=status.HTTP_400_BAD_REQUEST,
            safe=False,
        )
    return client


def check_admin_route(request):
    return get_body_from_post_request(request, "adminKey")
