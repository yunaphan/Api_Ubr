from django.urls import path
from .C_API import api_GetSpecies, api_getStatus
# from . import views

urlpatterns = [
    path('getListSpecies/', api_GetSpecies.getTenCX, name="Lấy Tên Cây Xanh"),
    path('getListStatus/', api_getStatus.getListStatusTree, name="Lấy Trạng Thái Cây xanh")
]
