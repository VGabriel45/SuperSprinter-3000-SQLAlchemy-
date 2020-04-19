import csv
import os

DATA_FILE_PATH = os.getenv(
    'DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'User Story',
               'Acceptance Criteria', 'Busines Value', 'Estimation', 'Status']
STATUSES = ['Not yet', 'planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story():
    return []

