from django.urls import path
from .views import homepage, estate_detail_page
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

    

urlpatterns = [
    path('',homepage.as_view(),name='home'),
    path("<slug:slug>/", estate_detail_page.as_view(), name="detail"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]