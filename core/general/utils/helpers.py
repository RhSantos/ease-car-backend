import json
from enum import Enum


class AsaasResourceUrl(Enum):
    CUSTOMER = "customers/"
    SUBSCRIPTION = "subscriptions/"
    SUB_ACCOUNT = "accounts/"

    def __str__(self) -> str:
        return self.value


def format_multipart_form_data_field(data, field: str):
    temp_data = data.copy()
    if temp_data.get(field):
        try:
            data_field = json.loads(temp_data.get(field))
            if data_field:
                for key, value in data_field.items():
                    temp_data[f"{field}.{key}"] = value

            temp_data[field] = None
        except:
            return None

    return temp_data
