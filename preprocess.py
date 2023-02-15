import os

def edit_file(text_path):
    with open(text_path, 'a', encoding='utf-8') as f:
        f.write('hello diaa')