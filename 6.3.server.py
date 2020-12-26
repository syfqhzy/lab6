import math
import socket
import sys
import time
import errno
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
    s_sock.send(str.encode('\n===ONLINE CALCULATOR FOR PYTHON==='))
    while True:
        data = s_sock.recv(2048)
        data = data.decode("utf-8")

#process/calculation
        try:
            operation, value = data.split(":")
            opt = str(operation)
            num = float(value)

            if opt[0] == 'L':
                opt = 'Logarithmic'
                ans = math.log10(num)
            elif opt[0] == 'S':
                opt = 'Square Root'
                ans = math.sqrt(num)
            elif opt[0] == 'E':
                opt = 'Exponential'
                ans = math.exp(num)
            else:
                answer = ('ERROR')

            sendAns = (str(opt)+ '['+ str(num) + ']= ' + str(ans))
            print ('\nCalculation successfully Done!')
        except:
            print ('Connection Terminated')
            sendAns = ('Connection Terminated')

        if not data:
            break

        s_sock.send(str.encode(str(sendAns)))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')

    except Exception as e:
                print("an exception occurred!")
                print(e)
                sys.exit(1)
    finally:
     	   s.close()

