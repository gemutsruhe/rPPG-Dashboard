import os
import csv
import json
import sqlite3
from django.shortcuts import render
from django.http import JsonResponse
from .models import UserInfo

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def directory_files(request):
    directory_path = '/Users/user/Documents/record'
    file_list = []

    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        file_list = [file for file in os.listdir(directory_path) if not file.startswith('.')]

    return render(request, 'blog/post_list.html', {'directory_files': file_list})

def get_bvp_data(request, timestamp):
    directory_path = '/Users/user/Documents/record/' + timestamp
    print(directory_path)
    csv_file_path = os.path.join(directory_path, 'rawBvp.csv')
    csv_data = []
    if os.path.exists(csv_file_path):
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_data = list(csv_reader)
    return JsonResponse(csv_data, safe=False)

def read_file_and_save_to_db(request, timestamp):
    data = load_data_from_json(timestamp)
    print(data)
    if data is not {}:
        add_data_to_database(timestamp, data)
        return JsonResponse(timestamp, safe=False)

def load_data_from_json(file):
    try :
        with open('/Users/user/Documents/record/' + file + "/userInfo.json", 'r') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def add_data_to_database(timestamp, data):

    user_info = UserInfo(timestamp=timestamp,
                         userName=data['userName'],
                         userSex=data['userSex'],
                         userAge=data['userAge']
                         )
    user_info.save()

def get_data_by_name(request, user_name):
    try:
        user_infos = UserInfo.objects.filter(userName=user_name)
        timestamp_list = [user_info.timestamp for user_info in user_infos]
        return JsonResponse(timestamp_list, safe=False)
    except UserInfo.DoesNotExist:
        pass

def get_data_by_sex(request, user_sex):
    try:
        user_info = UserInfo.objects.filter(userSex=user_sex)
    except UserInfo.DoesNotExist:
        pass

def get_data_by_age(request, user_age_small, user_age_big):
    try:
        user_info = UserInfo.objects.filter(age__gte=user_age_small, age__lte=user_age_big)
    except UserInfo.DoesNotExist:
        pass