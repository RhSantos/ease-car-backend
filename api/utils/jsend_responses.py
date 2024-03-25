from rest_framework.response import Response


def success_response(data):
    return Response({"status": "success", "data": data})


def fail_response(errors):
    return Response({"status": "fail", "data": errors})


def error_response(message):
    return Response({"status": "error", "message": message})
