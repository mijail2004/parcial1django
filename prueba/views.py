from django.shortcuts import render
from django.http import JsonResponse


def hola(request):
    return JsonResponse({"mensaje": "Hola desde Django"})
