import json
from .models import UserInfo

def load_data_from_json(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        return data

def add_data_to_database(data):
    for entry in data:
        user_info = UserInfo(
            timestamp = entry['timestamp'],
            name=entry['name'],
            sex=entry['sex'],
            age=entry['age']
        )
        user_info.save()

