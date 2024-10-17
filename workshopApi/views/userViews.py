from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from rest_framework import status
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import TemplateHTMLRenderer

from workshopApi.api.serializers import UserRegistrationSerializer, UserSerializer
from workshopApi.auth import forms
from workshopApi.models import CustomUser


# route for logout, access with /logout
def logout_user(request):
    logout(request)
    return redirect("login")


# define the login page inside the app
def login_page(request):
    form = forms.LoginForm()
    message = ""
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
            else:
                message = "Invalid credentials."
    return render(request, "login.html", context={"form": form, "message": message})


# View for the user management page rendering, access with /userManagement
@login_required
@renderer_classes([TemplateHTMLRenderer])
def userManagement(request):
    template = loader.get_template("manageUser.html")
    context = {
        "users": CustomUser.objects.all(),
    }
    return HttpResponse(template.render(context, request))


# Create a new user by using this api call, access with /api/createUser
@login_required
@api_view(["POST"])
def create_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        response = {
            "status": status.HTTP_201_CREATED,
            "data": serializer.data,
            "message": "User created successfully",
        }
        return JsonResponse(response)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get information about the user you want, access with /api/getUser/{userId}
@login_required
@api_view(["GET"])
def get_user(userId):
    user = get_object_or_404(CustomUser, id=userId)
    user_serialized = UserSerializer(user)
    return JsonResponse(user_serialized.data, status=status.HTTP_200_OK)


# you can deactivate a user, by this you must be admin
@staff_member_required
@login_required
@api_view(["PUT"])
def deactivate_user(userId):
    user = get_object_or_404(CustomUser, id=userId)
    if user is not None:
        user.is_active = False
        user.save()
        return JsonResponse("User deactivated", status=status.HTTP_200_OK, safe=False)
    else:
        return JsonResponse("User not found", status=status.HTTP_404_NOT_FOUND)


# you can activate a user, by this you must be admin
@staff_member_required
@login_required
@api_view(["PUT"])
def activate_user(userId):
    user = get_object_or_404(CustomUser, id=userId)
    if user is not None:
        user.is_active = True
        user.save()
        return JsonResponse("User deactivated", status=status.HTTP_200_OK, safe=False)
    else:
        return JsonResponse("User not found", status=status.HTTP_404_NOT_FOUND)
