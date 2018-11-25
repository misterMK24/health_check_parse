import os
import re

global filename
filename = 'CPaudit_HealthCheck.txt'

def dir_wroking_2(namedir, command_name):
    if re.findall(r'[/]{1}', namedir):
        namedir_true = (re.sub(r'[/]', r'\\', namedir))     # меняем / на \\ в указанном пути для корректной обработки
    for each_entry in os.listdir(namedir):
        if os.path.isdir(namedir + "\\" + each_entry):
            print("true")
        elif re.fullmatch(filename, each_entry):
            print("match cp_audit_health_check!")
        else:
            print("no way")


dir_wroking_2("C:\_python", "CP_Audit_Health_Check.txt")