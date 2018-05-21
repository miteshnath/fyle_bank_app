from rest_framework import routers

from .views import BankViewSet

bank_router = routers.SimpleRouter(trailing_slash=False)
bank_router.register(r'banks', BankViewSet, base_name='bank')
