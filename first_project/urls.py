from django.urls import path
from app import views

urlpatterns = [
path('', views.home_view, name='home'),
path('current_time/', views.time_view, name='time'),
path('workdir/', views.workdir_view, name='workdir'),
# path('admin/',views.admin.site.urls),
]

