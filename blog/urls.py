from django.urls import path
from . import views

urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('', views.directory_files, name='directory_files'),
    path('get_measured_bvp_data/<str:timestamp>/', views.get_bvp_data, name='get_bvp_data'),
    path('get_predicted_bvp_data/<str:timestamp>/', views.get_bvp_data, name='get_bvp_data'),
    path('get_json_data/<str:timestamp>/', views.read_file_and_save_to_db, name='get_json_data'),
    path('get_data/all/all/', views.get_data_all, name='get_data_all'),
    path('get_data/name/<str:user_name>/', views.get_data_by_name, name='get_data_by_name'),
    path('get_data/sex/<str:user_sex>/', views.get_data_by_sex, name='get_data_by_sex'),
    path('get_data/age/<str:user_age_min>/<str:user_age_max>/', views.get_data_by_age, name='get_data_by_age')
]
