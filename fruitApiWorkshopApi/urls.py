from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from workshopApi import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("doc", views.show_doc, name="doc"),
    path("userManagement", views.userManagement, name="userManagement"),
    path("api/createUser/", views.create_user, name="user_creation"),
    path("api/getUser/<str:id>", views.get_user, name="user_view"),
    path("api/createFruit/", views.create_fruit, name="create_fruit"),
    path("api/getFruit/<str:name>", views.get_fruit, name="fruit_view"),
    path("api/deleteFruit/<str:name>", views.delete_fruit, name="fruit_delete"),
    path("api/editFruit/<str:name>", views.update_fruit, name="fruit_edit"),
    path("api/indexFruit/", views.get_fruits, name="fruit_index"),
    path("api/createColor/", views.create_color, name="create_color"),
    path("api/getColor/<str:name>", views.get_color, name="color_view"),
    path("api/deleteColor/<str:name>", views.delete_color, name="color_delete"),
    path("api/editColor/<str:name>", views.update_color, name="color_edit"),
    path("api/indexColor/", views.get_colors, name="color_index"),
    path("api/createSeason/", views.create_season, name="create_season"),
    path("api/getSeason/<str:name>", views.get_season, name="season_view"),
    path("api/deleteSeason/<str:name>", views.delete_season, name="season_delete"),
    path("api/editSeason/<str:name>", views.update_season, name="season_edit"),
    path("api/indexSeason/", views.get_seasons, name="season_index"),
]
