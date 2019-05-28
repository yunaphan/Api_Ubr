from django.shortcuts import render
from django.db import connections
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getListStatusTree(request):
    refcur = connections['DoThi'].cursor()
    refcur.execute("select MaTinhTrang, TinhTrang, GhiChu from sde.TrangThaiCX ")
    row = dict()
    row = refcur.fetchall()
    return JsonResponse(row, safe=False)
