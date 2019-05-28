from django.urls import path
from .C_API import api_GetSpecies, api_getStatus, api_getListRoute
# from . import views

urlpatterns = [
    path('danh-sach-ten-cay-xanh/', api_GetSpecies.getTenCX, name="Ds Tên Cây Xanh"),
    path('danh-sach-trang-thai-cay-xanh/', api_getStatus.getListStatusTree, name="Ds Trạng Thái Cây xanh"),
    path('danh-sach-tuyen-duong/', api_getListRoute.getListRoute, name="Ds tuyến đường")

]
