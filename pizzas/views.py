from django.shortcuts import render

from .models import Pizza

def index(request):
    """피자 관리 홈페이지"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """pizzz 종류를 나타낸다."""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas' : pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def topping(request, pizza_id):
    """pizza종류에 따른 토핑을 나타낸다."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza':pizza, 'toppings': toppings}
    return render(request, 'pizzas/topping.html', context)
