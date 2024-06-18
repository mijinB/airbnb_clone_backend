from django.contrib import admin
from .models import House

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):

    #filed 묶기 (price, pets_allowed는 같은 열에 있게 됨)
    fields = (
        "name",
        "address",
        ("price", "pets_allowed"),
    )
    #리스트에서 column으로 보여주기
    list_display = (
        "name",
        "price",
        "address",
        "pets_allowed",
    )
    #리스트 오른쪽 필터 생성
    list_filter = (
        "price",
        "pets_allowed",
    )
    #리스트 상단에서 검색 가능
    search_fields = ("address",)
    #name, address를 누르면 상세 페이지로 이동
    list_display_links = ("name", "address")
    #상세 페이지로 이동하지 않아도 pets_allowed 수정 가능
    list_editable = ("pets_allowed",)