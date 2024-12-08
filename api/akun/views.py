# from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def akun_list(request):
    return JsonResponse({'message': 'List akun'})

def akun_edit(request):
    return JsonResponse({'message': 'Edit akun'})

def akun_delete(request):
    return JsonResponse({'message': 'Delete akun'})

def akun_create(request):
    return JsonResponse({'message': 'Create akun'})
