import os
from django.shortcuts import render

def directory_files(request):
    directory_path = '/Users/user/record'
    file_list = []

    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        file_list = os.listdir(directory_path)

    return render(request, 'post_list.html', {'file_list': file_list})
