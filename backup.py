import shutil
import os
import datetime


def backup_files(source, destination):
    today = datetime.date.today()
    backup_files =os.path.join(destination, f"backup_{today}.tar.gz")
    shutil.make_archive(backup_files, 'gztar', source)


source = "C:/Users/neetu/OneDrive/Documents/Python-workshop-practice"
destination = "C:/Users/neetu/OneDrive/Documents/Python-workshop-practice/backup"

backup_files(source, destination)




