from rest_framework.response import Response
from rest_framework.views import status


def validate_request_data(fn):
    def decorated(*args, **kwargs):
        # args[0] == GenericView Object
        title = args[0].request.data.get("title", "")
        date = args[0].request.data.get("date", "")
        fav = args[0].request.data.get("fav", "")
        active = args[0].request.data.get("active", "")
        startDate = args[0].request.data.get("startDate", "")
        endDate = args[0].request.data.get("endDate", "")
        if not title and not date and not fav and not active and not startDate and not endDate:
            return Response(
                data={
                    "message": "All Fields are required to add a event"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)

    return decorated
