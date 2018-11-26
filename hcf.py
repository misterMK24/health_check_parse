import os
import re


global filename
filename = 'CPaudit_HealthCheck.txt'

def parse_file(command_name):
    index = 0
    result_string = []
    with open(filename, 'r') as file:
        for line in file:
            match_command = re.match(r'={3}\s' + command_name + r'\s[=]{3}', line)
            if match_command or index == 1:
                index = 1
                if re.match(r'={3}\s{1}[^=]+[=]{3}', line) and not match_command:
                    break
                result_string.append(line)
    return result_string


def to_file(result_string, gw_name):
    with open('C:\\results\\python_parse.txt', 'a+') as file:
        file.write(gw_name + "\n")
        for string in result_string:
            file.write(string)


def dir_working(namedir, command_name):
    if re.findall(r'[/]{1}', namedir):
        namedir_true = (re.sub(r'[/]', r'\\', namedir))
    for gw_name in os.listdir(namedir):
        # is this a dir?
        check_dir = namedir_true + "\\" + gw_name
        if os.path.isdir(check_dir):  # re.search(r'[.]{1}\w+', dir) is None:
            os.chdir(check_dir)  # переходим в директорию
            current_dir = os.listdir(check_dir)  # поиск CPaudit_HealthCheck.txt
            if current_dir:  # если директория не пуста
                for in_dir in current_dir:
                    if re.fullmatch(r'\b[Ff]w[_-]{1}\S+[^\.tar]', in_dir):
                        print("OK")
                    if re.search(filename, in_dir) is not None:  # если искомый файл существует, то парсим
                        result_string = parse_file(command_name)
                        to_file(result_string, gw_name)

def dir_working_2(namedir, command_name):
    if re.findall(r'[/]{1}', namedir):
        namedir_true = (re.sub(r'[/]', r'\\', namedir))
    for root, dirs, files in os.walk(namedir):
        for file in files:
            if re.fullmatch(filename, file):
                os.chdir(root)
                result_string = parse_file_2(command_name)
                to_file_2(result_string)

def to_file_2(result_string):                                                # , gw_name):
    with open('C:\\results\\python_parse.txt', 'a+') as file:
        # file.write(gw_name + "\n")
        for string in result_string:
            file.write(string)


def parse_file_2(command_name):
    index = 0
    result_string = []
    with open(filename, 'r') as file:
        for line in file:
            match_command = re.match(r'={3}\s' + command_name + r'\s[=]{3}', line)
            if match_command or index == 1:
                index = 1
                if re.match(r'={3}\s{1}[^=]+[=]{3}', line) and not match_command:
                    break
                result_string.append(line)
    return result_string