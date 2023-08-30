from django.urls import path
from . import views

urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('', views.directory_files, name='directory_files'),
    path('get_bvp_data/<str:timestamp>/', views.get_bvp_data, name='get_bvp_data'),
    path('get_json_data/<str:timestamp>/', views.read_file_and_save_to_db, name='get_json_data')
]
