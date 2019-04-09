import socket
import subprocess
import struct
import json
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('192.168.1.5', 8020))
phone.listen(5)
print('start....')
while True:
    conf,message = phone.accept()
    print(conf)
    print(message)
    while True:
        try:
            data = conf.recv(1024)
            if not data:
                break
            data_tr = data.decode('utf-8')
            print(data_tr)
            #  stdin,stdout, stderr： 分别指示要执行的程序标准输入、标准输出、标准错误输出文件的句柄
            re = subprocess.Popen(data_tr, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            r1 = re.stdout.read()
            r2 = re.stderr.read()
            # 真正内容的长度
            r_size = len(r1) + len(r2)
            # head头字典的格式
            head_dict = {'data_size': r_size}
            # 用json转换
            head_json = json.dumps(head_dict)
            head_content = head_json.encode('utf-8')
            # 发送报头的长度
            head_size = len(head_content)
            conf.send(struct.pack('i', head_size))
            # 发送报头
            conf.send(head_content)
            # 发送真正的内容
            conf.send(r1)
            conf.send(r2)
        except Exception:
            break
    conf.close()
phone.close()


