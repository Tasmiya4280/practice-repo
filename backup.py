import shutil
import datetime
import os


def backup_files(source, destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination ,f"backup_{today}")
    shutil.make_archive(backup_file_name,'gztar',source)

source = "/home/tasmiya/PycharmProjects/PythonProject/.venv/practice"
destination = "/home/tasmiya/PycharmProjects/PythonProject/.venv/practice/backup"
backup_files(source, destination)