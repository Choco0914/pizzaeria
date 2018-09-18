from django.contrib import admin
from django.urls import path, re_path, include

app_name = 'pizzas'

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'', include(('pizzas.urls', 'pizzas'),
        namespace = 'pizzas')),
]
