from django.contrib import admin
from django.urls import path, include
'''
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('capturas/', include('capturas.urls')),
    path('perguntas/', include('perguntas.urls')),
    path('usuarios/', include('usuarios.urls')),   


'''

urlpatterns = [    
    
    path('admin/', admin.site.urls),
]
