from django.urls import path
from .views import get_crypto_data, RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('crypto-data/', get_crypto_data, name="crypto-data"),
]
