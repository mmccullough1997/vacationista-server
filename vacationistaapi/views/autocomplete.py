import os
import requests
from rest_framework.views import APIView
from rest_framework.response import Response

class AutocompleteAPIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
      location = kwargs.get('param')
      geoapify_token = os.getenv('GEOAPIFY_API_TOKEN')
      url = "https://api.geoapify.com/v1/geocode/autocomplete"
      params = {
          "text": location,
          "apiKey": geoapify_token,
          "limit": 10,
      }
      response = requests.get(url, params=params)
      data = response.json()
      return Response(data)
