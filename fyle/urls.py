from django.conf.urls import url, include
from django.conf import settings

from banks.urls import bank_router

urlpatterns = [
    url(settings.API_BASE_URL, include(bank_router.urls)),
]