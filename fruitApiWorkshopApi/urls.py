
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from workshopApi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('doc',views.show_doc,name='doc'),
    path('api/createUser/',views.create_user,name='user_creation'),
    path('api/getUser/<str:id>',views.get_user,name='user_view'),
]