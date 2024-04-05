from rest_framework.response import Response
from rest_framework import status

def success_response(data=None, status=status.HTTP_200_OK):
    return Response({"status": "success", "data": data}, status = status)


def fail_response(errors, status = status.HTTP_400_BAD_REQUEST):
    return Response({"status": "fail", "data": errors}, status = status)


def error_response(message, status = status.HTTP_404_NOT_FOUND):
    return Response({"status": "error", "message": message}, status = status)
