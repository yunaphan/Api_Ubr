from django.urls import path
from .C_API import api_GetSpecies, api_getStatus, api_getListRoute, api_Login
# from . import views

urlpatterns = [
    path('danh-sach-ten-cay-xanh/', api_GetSpecies.getTenCX, name="Ds Tên Cây Xanh"),
    path('danh-sach-trang-thai-cay-xanh/', api_getStatus.TrangThai.getListStatusTree, name="Ds Trạng Thái Cây xanh"),
    path('trang-thai-cay-xanh/', api_getStatus.TrangThai.stastusDetail, name="chi tiết trang thái cây xanh"),
    path('them-trang-thai-cay-xanh/', api_getStatus.TrangThai.createStatus, name="thêm trạng thái cây xanh"),
    path('xoa-trang-thai/', api_getStatus.TrangThai.deleteStatus, name="Xóa trạng thái"),
    path('danh-sach-tuyen-duong/', api_getListRoute.TuyenDuong.getListRoute, name="Ds tuyến đường"),
    path('user-token/', api_Login.login.token_login, name="token của user")

]
