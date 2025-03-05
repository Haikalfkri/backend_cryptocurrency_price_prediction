from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

import requests

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer

User = get_user_model()

# Authentications
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "role": user.role.name,
                })
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# get crypto data from coingecko api
def get_crypto_data(request):
    coin = request.GET.get('coin')
    url = f"https://api.coingecko.com/api/v3/coins/{coin}"

    try:
        response = requests.get(url)
        data = response.json()

        btc_data = {
            "Price (USD)": data["market_data"]["current_price"]["usd"],
            "Market Cap (USD)": data["market_data"]["market_cap"]["usd"],
            "24h Volume (USD)": data["market_data"]["total_volume"]["usd"],
            "FDV (USD)": data["market_data"]["fully_diluted_valuation"]["usd"],
            "Total Supply": data["market_data"]["total_supply"],
            "Max Supply": data["market_data"]["max_supply"],
            "Circulating Supply": data["market_data"]["circulating_supply"],
            "Market Cap Change Percentage (24h)": data["market_data"]["market_cap_change_percentage_24h"],
        }

        return JsonResponse(btc_data)
    except:
        return JsonResponse({"error": "An error occurred."})