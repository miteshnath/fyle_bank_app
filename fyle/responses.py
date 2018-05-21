from rest_framework.response import Response
from rest_framework import status


def __send(data, status):
    return Response(data, status)


def send_201(data):
    return __send(data, status.HTTP_201_CREATED)


def send_200(data):
    return __send(data, status.HTTP_200_OK)


def send_204():
    return Response(status=status.HTTP_204_NO_CONTENT)


def send_400(data):
    return __send(data, status.HTTP_400_BAD_REQUEST)
