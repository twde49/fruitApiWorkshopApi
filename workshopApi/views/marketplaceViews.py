from django.core.mail import send_mail
from rest_framework.decorators import api_view

from workshopApi.api.serializers import *
from workshopApi.utils import *


# view for create a new platform
@api_view(["POST"])
def create_new_platform(request):
    serializer = PlatformSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    send_mail(
        "Your api key",
        "Hello, here are your api " + serializer.data["adminKey"],
        "fruit@admin.com",
        ["thibaut.stachnick@mail-esd.com"],
    )
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view for client creation
@api_view(["POST"])
def create_client(request):
    if not check_admin_route(request):
        return JsonResponse("please provide an Admin key for that", safe=False)
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view to see how many requests the user can do
@api_view(["POST"])
def get_number_of_available_requests(request):
    if not check_admin_route(request):
        return JsonResponse("please provide an Admin key for that", safe=False)
    client = get_client_from_admin_key_and_mail(request)
    response = {
        "availableRequests": client.nbOfAvailableRequests,
        "usedRequests": client.nbUsedRequests,
        "remainingRequests": client.nbOfAvailableRequests - client.nbUsedRequests,
    }
    return JsonResponse(response, safe=False)


# view to revoke and remove api key OR revoke and replace the api key
@api_view(["POST"])
def revoke_key(request):
    if not check_admin_route(request):
        return JsonResponse("please provide an Admin key for that", safe=False)
    must_be_removed = get_body_from_post_request(request, "mustBeRemoved")

    if not get_body_from_post_request(request, "adminKey"):
        return JsonResponse("please provide an Admin key for that", safe=False)
    elif not get_body_from_post_request(request, "email"):
        return JsonResponse("please provide an email for that", safe=False)
    client = get_client_from_admin_key_and_mail(request)
    have_remaining_requests = check_if_client_got_remaining_requests(client)
    if not have_remaining_requests:
        return JsonResponse(
            "You don't have any request available, you can't revoke anything for now",
            safe=False,
        )
    elif client.apiKey is None:
        return JsonResponse(
            "You don't have an active API key, please generate another one", safe=False
        )
    else:
        if must_be_removed:
            client.apiKey = None
            client.save()
            return JsonResponse("Your api key access have been removed", safe=False)
        else:
            response = generate_new_apiKey(client)
            return JsonResponse(response, status=status.HTTP_201_CREATED, safe=False)


# view for generate a new api key from admin for a client
@api_view(["POST"])
def generate_new_api_key_for_client(request):
    if not check_admin_route(request):
        return JsonResponse("please provide an Admin key for that", safe=False)
    client = get_client_from_admin_key_and_mail(request)
    if isinstance(client, JsonResponse):
        return client
    if client is not None:
        response = generate_new_apiKey(client)
        return JsonResponse(
            {"your new key has been generated": response["raw_api_key"]}, safe=False
        )
    return JsonResponse(
        "It look like the client you're looking for can't be found", safe=False
    )


# view to add bought requests for a client
@api_view(["POST"])
def add_requests_to_client(request):
    if not check_admin_route(request):
        return JsonResponse("please provide an Admin key for that", safe=False)
    requests_to_add = get_body_from_post_request(request, "nbOfRequestsToAdd")
    if not requests_to_add:
        return JsonResponse(
            "you must define how many requests to add with 'nbOfRequestsToAdd'",
            safe=False,
        )
    else:
        client = get_client_from_admin_key_and_mail(request)
        client.nbOfAvailableRequests += requests_to_add
        client.active = True
        client.save()
        return JsonResponse(
            "Your requests have been added you have now "
            + str(client.nbOfAvailableRequests),
            safe=False,
        )
