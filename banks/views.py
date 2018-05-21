from .models import Bank
from rest_framework import viewsets
from .serializers import BankSerializer
from fyle.responses import send_200, send_201, send_400


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return send_201(serializer.data)
        else:
            return send_400(serializer.data)

    def list(self, request):
        _params = request.query_params

        if 'ifsc' in _params:
            self._ifsc = _params.get('ifsc', '')
            queryset = Bank.objects.filter(ifsc__icontains=self._ifsc)

        elif 'all' in _params:
            queryset = Bank.objects.all()

        elif 'bank_name' in _params and 'city' in _params:
            self._bank_name = _params.get('bank_name', '')
            self._city = _params.get('city', '')
            queryset = Bank.objects.filter(bank_name__icontains=self._bank_name, city__icontains=self._city)

        else:
            error = {'error': 'correct params not passed'}
            return send_400(error)

        serializer = self.get_serializer(queryset, many=True)
        return send_200(serializer.data)
