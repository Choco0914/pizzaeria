"""pizzas의 URL 패턴을 정의한다."""

from django.urls import re_path

from . import views

urlpatterns = [
    #홈페이지
    re_path(r'^$', views.index, name='index'),

    # 피자 종류
    re_path(r'^pizzas/$', views.pizzas, name='pizzas'),
    # 피자에대한 토핑종류
    re_path(r'^pizzas/(?P<pizza_id>\d+)/$', views.topping, name='topping')
]
