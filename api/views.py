from django.http import JsonResponse
from django.views import View

# Create your views here.
class RequestHeaderParserAPIView(View):

    def get(self, request, *args, **kwargs):

        data = {
            "ipaddress": request.environ['REMOTE_ADDR'],
            "language": request.environ['HTTP_ACCEPT_LANGUAGE'],
            "software": request.environ['HTTP_USER_AGENT']
        }

        return JsonResponse(data, safe=False)
