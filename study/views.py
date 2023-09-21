import time

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def server_ping(request):
    result = {"success": True, "timestamp": time.time()}
    data = request.data
    if data:
        result = {**result, **data}
    return Response(result)
