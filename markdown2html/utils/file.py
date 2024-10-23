
import os

class File:
    @staticmethod
    def read_file(file: str) -> str:
        with open(file, 'r', encoding='utf-8') as pf:
            return pf.read()

    @staticmethod
    def write_file(file: str, content: str) -> str:
        if os.path.exists(file):
            print(f"File {file} already exists.")
            return ''
        with open(file, 'w', encoding='utf-8') as pf:
            pf.write(content)
