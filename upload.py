import os

from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()
    folder_path = os.path.join("/home/luyahan/aliyun/", 'node')
    
    ali.upload_folder(folder_path)