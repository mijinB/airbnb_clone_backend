from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
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
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            # 사용자한테서 받은 data 밖에 없으므로 create 메서드 실행
            new_category = serializer.save()
            return Response(
                CategorySerializer(new_category).data,
            )
        else:
            return Response(serializer.errors)


@api_view(["GET", "PUT"])
def category(request, pk):
    # 사용자가 요청한 (pk가 일치하는)category가 없을경우, 예외처리
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise NotFound

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CategorySerializer(
            category,
            data=request.data,
            # 들어오는 data가 완벽한 형태가 아닐 수도 있다는 것을 알려줌 (=사용자한테서 받지 못한 data는 현재 data로 유지해야 한다는 것)
            partial=True,
        )
        if serializer.is_valid():
            # DB에서 가져온 data와 사용자한테서 받은 data로 serializer를 만든다는 것을 알기 때문에 create 메서드를 실행하지않고 update 메서드를 실행한다.
            updated_category = serializer.save()
            return Response(
                CategorySerializer(updated_category).data,
            )
        else:
            return Response(serializer.errors)
