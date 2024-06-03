import requests
from django.conf import settings
from core.general.utils.helpers import AsaasResourceUrl


def make_asaas_api_call(request_data: dict, api_resource:AsaasResourceUrl):

    response = requests.post(
        url=settings.ASAAS_API_URL + str(api_resource),
        json=request_data,
        headers={
            "access_token": settings.ASAAS_API_KEY,
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
    )

    return response
