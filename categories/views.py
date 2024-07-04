from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Category


# Django serialization framework 사용해서 만드는 방법
# custom을 위한 많은 기능을 제공하지 않는다.


def categories(request):
    all_categories = Category.objects.all()
    return JsonResponse(
        {
            "ok": True,
            "categories": serializers.serialize("json", all_categories),
        },
    )
