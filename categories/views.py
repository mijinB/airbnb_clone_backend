from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


@api_view(["GET", "POST"])
def categories(request):

    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(
            all_categories,
            many=True,
        )
        return Response(
            {
                "ok": True,
                "categories": serializer.data,
            },
        )
    elif request.method == "POST":
        # POST일 경우에는 그냥 첫번째 인자에 넣으면 안되고, data=뒷부분에 넣어야 한다.
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                {
                    "created": True,
                },
            )
        else:
            return Response(serializer.errors)


@api_view()
def category(request, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)
