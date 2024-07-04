from django.shortcuts import render
from django.http import JsonResponse
from .models import Category


# Django REST framework 없이 만드는 방법


def categories(request):
    all_categories = Category.objects.all()
    return JsonResponse(
        {
            "ok": True,
            "categories": all_categories,
        },
    )
