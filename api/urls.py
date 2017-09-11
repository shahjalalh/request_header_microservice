from django.conf.urls import url
from .views import RequestHeaderParserAPIView

urlpatterns = [

    url(r'^whoami/', RequestHeaderParserAPIView.as_view()),

]
