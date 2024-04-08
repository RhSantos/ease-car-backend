from rest_framework import status
from rest_framework.response import Response


def success_response(key="object", data=None, status=status.HTTP_200_OK):
    return Response(
        {"status": "success", "data": ({key: data} if data else None)}, status=status
    )


def fail_response(errors, status=status.HTTP_400_BAD_REQUEST):
    return Response({"status": "fail", "data": errors}, status=status)


def error_response(message, status=status.HTTP_404_NOT_FOUND):
    return Response({"status": "error", "message": message}, status=status)
