from django.contrib import admin
from django.urls import path, include
from clima import views  # Certifique-se de que o views está importado corretamente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Página inicial
    path('clima/', include('clima.urls')),  # URLs do app clima
]
