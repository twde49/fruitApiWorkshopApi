import hashlib
import json
import os

from django.http import JsonResponse

from workshopApi.models import Client, Platform
from workshopApi.views.marketplaceViews import check_if_client_got_remaining_requests


def RequestInterceptor(get_response):
    def middleware(request):
        if request.path.startswith("/api/"):

            try:
                data = json.loads(request.body.decode("utf-8"))
            except json.JSONDecodeError:
                return JsonResponse("Invalid JSON data", safe=False)

            api_key = data.get("apiKey")
            admin_key = data.get("adminKey")
            owner_key = data.get("ownerKey")

            if api_key:
                try:
                    hash_key = hashlib.sha256(api_key.encode("utf-8"))
                    client = Client.objects.get(apiKey=hash_key.hexdigest())
                except Client.DoesNotExist:
                    return JsonResponse(
                        "Your API key doesn't seem to be active", safe=False
                    )

                hasAvailableRequests = check_if_client_got_remaining_requests(client)
                if not hasAvailableRequests:
                    return JsonResponse(
                        "It seems like you don't have requests anymore", safe=False
                    )

                client.nbUsedRequests += 1
                client.nbOfAvailableRequests -= 1
                client.save()

            elif admin_key:
                if not Platform.objects.filter(adminKey=admin_key).exists():
                    return JsonResponse(
                        "There is no platform with this key", safe=False
                    )
            elif owner_key:
                if owner_key == os.getenv("OWNER_KEY"):
                    return get_response(request)
            else:
                return JsonResponse("No valid key provided", safe=False)

            return get_response(request)
        return get_response(request)

    return middleware
