from django.shortcuts import render
from django.db import connections
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getTenCX(request):
    refcur = connections['DoThi'].cursor()
    refcur.execute("select MaTenCX, TenCX from sde.TenCX ")
    row = dict()
    row = refcur.fetchall()
    print(row)
    return JsonResponse(row, safe=False)
