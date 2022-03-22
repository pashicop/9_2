from pprint import pprint
import pathlib
from pathlib import Path
import os

import requests

HEADERS = {"Authorization": "OAuth AQAAAAAWTeeYAADLW0-rjvA3UE1bqNEUIgDXDu4"}


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path):
        """Метод загруджает файл file_path на яндекс диск"""
        response = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload",
                                params={"path": os.path.basename(file_path), "overwrite": "true"},
                                headers=HEADERS
                                )
        response.raise_for_status()
        data = response.json()
        # pprint(data)
        href = data["href"]
        with open(file_path, "rb") as f:
            put_response = requests.put(href, files={"file": f}, headers=HEADERS)
            put_response.raise_for_status()
            # pprint(put_response.text)
        return 'Файл успешно загружен'


if __name__ == '__main__':
    uploader = YaUploader('AQAAAAAWTeeYAADLW0-rjvA3UE1bqNEUIgDXDu4')
    dir_path = Path.home()
    f_path = Path(dir_path, "Downloads", "1.docx")
    print(f_path)
    result = uploader.upload(f_path)
    print(result)
