import os
import re

global filename
filename = 'CP_Audit_Health_Check.txt'

def dir_wroking_2(namedir, command_name):
    for root, dirs, files in os.walk(namedir):
        for file in files:
            if re.fullmatch(filename, file):
                print("vyzyvai parse file func i peredai dir")






dir_wroking_2("C:\_python", "uname -a")