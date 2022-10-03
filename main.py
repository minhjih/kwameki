from PySide6.QtWidgets import *
from demo import Ui_Widget
import os
import subprocess

#subprocess.call(["cd"], cwd="C:\\Users\\jhcho\\kwameki\\", shell= True)

class initialize(object):
    def __init__(self):
        self.dir = os.popen("dir").read().split('\n')
        self.dir = self.dir[5:]
        self.all_file_name = []
        for i in range(len(self.dir)-5):
            self.not_dir = self.dir[i].split()[3]
            if(self.not_dir!="<DIR>"):
                a = self.dir[i].split()[4]
                self.all_file_name.append(a)#all_file_name은 file name을 받아옴

def set_date(date):
    changed_date = ""
    date_array = date.split('')
    changed_date += date_array[0] + ' ' + date_array[1] + date_array[2] + '/' + date_array[4] + '\n' + date_array[3]

class file(object):
    def __init__(self):
        self.index_version = 0
        self.file_name = ""  # 파일명
        self.file_token = ""  # 토큰
        self.file_author = ""  # 공동 편집자의 이름, 이메일, 최근 수정일자
        self.edit = ""  # 최근 수정내용
        self.date = ""  # 최근 해당 파일 수정 일자

class united_file(object):
    def __init__(self):
        self.index = 0
        self.file_name = ""
        self.file_version = []

    def file_modify(self):#file version 정보를 받아와 버젼별 파일 저장
        i = -1
        j = 0
        for text in os.popen("git log -p "+ self.file_name).read().replace('\n','').split():#대충 정보 넣는거임
            if(text == 'commit'):
                i += 1
                self.file_version.append(file())
                j = 0
            elif(text != "commit" and text != "Author:" and text != "Date:" and text != "+0900"):
                if(j == 0):
                    self.file_version[i].token = text
                elif(j==1 or j==2):
                    self.file_version[i].file_author += text + ' '
                elif(j>2 and j<8):
                    self.file_version[i].date += text + ' '
                    self.file_version[i].date = set_date(self.file_version[i].date)
                else:
                    self.file_version[i].edit += text + ' '
                j += 1
        for i, file in enumerate(self.file_version):
            file.index_version = len(self.file_version) - i


init = initialize()#all_file_name 받아옴
bundle_of_united_fileclass = []#file_class 받아올 장소

for i in range(len(init.all_file_name)):#i 개의 all_file_name을 받아올 장소
    bundle_of_united_fileclass.append(united_file())#file의 갯수만큼 file클래스 생성
    bundle_of_united_fileclass[i].file_name = init.all_file_name[i]#file 클래스에 이름 넣기
    bundle_of_united_fileclass[i].index = i
    bundle_of_united_fileclass[i].file_modify()

'''class branch(object):
    def __init__(self):
        self.name = ""  # branch name
        self.token = ""

    def file_
'''


class MyApp(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def main(self):
        self.set(bundle_of_united_fileclass)
        pass

app = QApplication()
win = MyApp()
win.show()
app.exec()