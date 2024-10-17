from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from workshopApi.views import (
    docViews,
    userViews,
    fruitViews,
    colorViews,
    seasonViews,
    marketplaceViews,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("doc/", docViews.show_doc, name="doc"),
    path("userManagement/", userViews.userManagement, name="userManagement"),
    path("login/", userViews.login_page, name="login"),
    path("logout/", userViews.logout_user, name="logout"),
    path("api/createUser/", userViews.create_user, name="user_creation"),
    path("api/getUser/<str:userId>", userViews.get_user, name="user_view"),
    path(
        "api/deactivateUser/<str:userId>",
        userViews.deactivate_user,
        name="deactivate_user",
    ),
    path(
        "api/activateUser/<str:userId>", userViews.activate_user, name="activate_user"
    ),
    path("api/createFruit/", fruitViews.create_fruit, name="create_fruit"),
    path("api/getFruit/<str:name>", fruitViews.get_fruit, name="fruit_view"),
    path("api/deleteFruit/<str:name>", fruitViews.delete_fruit, name="fruit_delete"),
    path("api/editFruit/<str:name>", fruitViews.update_fruit, name="fruit_edit"),
    path("api/indexFruit/", fruitViews.get_fruits, name="fruit_index"),
    path("api/createColor/", colorViews.create_color, name="create_color"),
    path("api/getColor/<str:name>", colorViews.get_color, name="color_view"),
    path("api/deleteColor/<str:name>", colorViews.delete_color, name="color_delete"),
    path("api/editColor/<str:name>", colorViews.update_color, name="color_edit"),
    path("api/indexColor/", colorViews.get_colors, name="color_index"),
    path("api/createSeason/", seasonViews.create_season, name="create_season"),
    path("api/getSeason/<str:name>", seasonViews.get_season, name="season_view"),
    path(
        "api/deleteSeason/<str:name>", seasonViews.delete_season, name="season_delete"
    ),
    path("api/editSeason/<str:name>", seasonViews.update_season, name="season_edit"),
    path("api/indexSeason/", seasonViews.get_seasons, name="season_index"),
    path(
        "api/createPlatform/",
        marketplaceViews.create_new_platform,
        name="create_new_platform",
    ),
    path("api/createClient/", marketplaceViews.create_client, name="create_new_client"),
    path(
        "api/getRequests/",
        marketplaceViews.get_number_of_available_requests,
        name="get_remaining_requests",
    ),
    path("api/revokeKey/", marketplaceViews.revoke_key, name="revoke_key"),
    path(
        "api/generateNewApiKey/",
        marketplaceViews.generate_new_api_key_for_client,
        name="generate_new_api_key_for_client",
    ),
    path(
        "api/addRequests/",
        marketplaceViews.add_requests_to_client,
        name="add_requests_to_client",
    ),
]
