from django.shortcuts import render

def index(request):
    """피자 관리 홈페이지"""
    return render(request, 'pizzas/index.html')
