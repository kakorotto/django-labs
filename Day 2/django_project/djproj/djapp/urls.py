from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('details/<st_id>', views.show, name='show'),
    path('del/<st_id>', views.del_St, name='del'),
    
]
