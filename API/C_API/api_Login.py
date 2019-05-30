from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.db import connections
# from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


class login:
    @csrf_exempt
    def token_login(request):
        # data = request.POST.get('data')
        p_username = request.POST.get('username')
        p_password = request.POST.get('password')
        return JsonResponse(p_username, safe=False)
        row = status_row = dict()
        if p_username and p_password:
            refcur = connections['AccountsSys'].cursor()
            refcur.execute("select remember_token from users where username = %s and password = %s and enabled = 1",
                           (p_username, p_password))
            row['token'] = refcur.fetchall()
            if (row['token']):
                row['success'] = status.HTTP_200_OK
                return JsonResponse(row, safe=False)
            else:
                row['error'] = status.HTTP_401_UNAUTHORIZED
                return JsonResponse({'error': row['error']}, safe=False)
        else:
            row['error'] = status.HTTP_400_BAD_REQUEST
            return JsonResponse(row, safe=False)
