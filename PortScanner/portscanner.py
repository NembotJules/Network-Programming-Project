
import socket
import threading
from queue import Queue

#computer Ipv4 adress 192.168.8.123
target =  '192.168.8.123'
queue = Queue()
open_ports = []


def portscan(port): 
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        return True 
    except: 
        return False


def fill_queue(port_list): 
    for port in port_list: 
        queue.put(port)

def worker(): 
    while not queue.empty():
       port = queue.get()
       if portscan(port): 
         print(f"Port{port} is open.")
         open_ports.append(str(port))


port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

for t in range(1000): 
    thread = threading.Thread(target = worker)
    thread_list.append(thread)

for thread in thread_list: 
    thread.start()
   

for thread in thread_list: 
    thread.join()
    

print("Open ports are:  ", open_ports )

