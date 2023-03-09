#encoding=utf-8

from os import system
import os

input_output_folder = "./io_files/"

def tc_int(i):
    try:
        return int(i)
    except:
        return i

def load_std_input_file(file_name, pre_processing = None):
    io_records = []
    f = open(input_output_folder + file_name)
    for ln in f.readlines():
        if (pre_processing == None):
            io_records.append([part.strip() for part in ln.split(" ")])
        else:
            io_records.append([pre_processing(part.strip()) for part in ln.split(" ")])
    return io_records
    
ccc_params = []

def replace_input(file_name):
    global ccc_params
    ccc_params.extend(open(input_output_folder + file_name).readlines())

def input():
    global ccc_params
    if (len(ccc_params) > 0):
        return ccc_params.pop(0).strip()
    return None

import datetime
start_time = None

def start_ccc():
    global start_time
    start_time = datetime.datetime.now()

def end_ccc():
    global start_time
    s = str(datetime.datetime.now() - start_time)
    s = "\033[1;37;40m%s\033[0m" % ("TIME USAGE : " + s)
    print(s)

class Input():
    def __init__(self, iofile, testcase_name = "") -> None:
        self.io_file_name = iofile
        self.testcase_name = testcase_name
        if iofile:
            self.io_file = open(self.io_file_name)
            if len(testcase_name) == 0:
                self.io_file_lines = self.io_file.readlines()
            else:
                self.io_file_lines = self.__select_group(testcase_name)

    def __select_group(self, testcase_name):
        group_lines = []
        in_group = False
        for ln in self.io_file.readlines():
            if ln.startswith("[["):
                if ln.lower().find(testcase_name.lower()) >= 0:
                    in_group = True
            elif ln.endswith("]]"):
                in_group = False
                break
            elif in_group:
                group_lines.append(ln)
        return group_lines

    def input(self):
        while True:
            ln = self.io_file_lines.pop(0).strip()
            if not ln.startswith(("[[]", "]]")):
                break
        return ln

"""
-------------------------------------------
字体色     |       背景色     |      颜色描述
-------------------------------------------
30        |        40       |       黑色
31        |        41       |       红色
32        |        42       |       绿色
33        |        43       |       黃色
34        |        44       |       蓝色
35        |        45       |       紫红色
36        |        46       |       青蓝色
37        |        47       |       白色
-------------------------------------------
-------------------------------
显示方式     |      效果
-------------------------------
0           |     终端默认设置
1           |     高亮显示
4           |     使用下划线
5           |     闪烁
7           |     反白显示
8           |     不可见
-------------------------------
"""
class Output():
    debug_fmt = "\033[1;37;40m%-3s\033[0m"
    def __init__(self) -> None:
        self.indexing = {}
        start_ccc()

    def get_prefix(self, index):
        if len(index) > 0:
            if not index in self.indexing:
                self.indexing[index] = 0
            self.indexing[index] += 1
            return Output.debug_fmt % self.indexing[index]
        else:
            return Output.debug_fmt % " > "

    def output(self, s, end = False, highlight=False, index=""):
        s = str(s)
        if highlight:
            s = Output.debug_fmt % s
        else:
            s = s.replace("<[", "\033[1;37;40m")
            s = s.replace("]>", "\033[0m")
            s = s.replace("<{", "\033[0;34;43m")
            s = s.replace("}>", "\033[0m")
        for ln in s.splitlines():
            print(self.get_prefix(index) + ln)
        if end:
            end_ccc()

def make_io(iofile_name, testcase=""):
    import os.path
    pn, fn = tuple(os.path.split(iofile_name))
    f, ext = tuple(fn.split("."))
    log_filename = f + ".log"
    return Input(os.path.join(pn, input_output_folder, log_filename), testcase).input, \
        Output().output

def make_o():
    return Output().output

if (__name__ == "__main__"):
    start_ccc()

    print (load_std_input_file("ccc13s3_1.log"))
    print (load_std_input_file("ccc13s3_1.log", pre_processing = tc_int))

    replace_input("ccc13s3_1.log")
    print(input())
    print(input())
    print(input())
    print(input())
    print(input())

    end_ccc()