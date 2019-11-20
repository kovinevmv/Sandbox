import json

COOKIES_PATH = './cookies.txt'

def parse_cookies():
    with open(COOKIES_PATH, 'r') as f:
        data = json.loads(f.read())
    cookies = {}
    for cookie in data:
        cookies[cookie['name']] = cookie['value']
    return cookies


def is_exclude_path(path):
    exclude_paths = ['node_modules', 'public/files', '.git', 'inc', 'lib', 'vendor', 'cache', 'data/index']
    for exclude_path in exclude_paths:
        if exclude_path in path:
            return True
    return False

def is_exclude_file(file):
    exclude_files = ['png', 'jpg', 'jpeg', 'docx', 'pdf']
    for exclude_file in exclude_files:
        if exclude_file in file:
            return True
    return False  