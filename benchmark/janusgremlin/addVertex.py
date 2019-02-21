import random
import time
import threading

from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection


class AddTest():
    def __init__(self):
        graph = Graph()
        ip_pools = ['192.168.50.5', '192.168.50.6', '192.168.50.7']
        request_ip = random.sample(ip_pools, 1)[0]
        self.g = graph.traversal().withRemote(DriverRemoteConnection('ws://' + request_ip + ':8182/gremlin', 'g'))

    def addV(self):
        self.g.addV().property("username", "wine").next()
        #self.g.addV().label().property("name", "wine").next()

def run_test():
    a = AddTest()
    return a.addV()


tasks_number = 1
thread_list = []  # 线程存放列表
time1 = time.clock()

for i in range(tasks_number):
    t = threading.Thread(target=run_test)
    t.setDaemon(True)
    thread_list.append(t)

for t in thread_list:
    t.start()

for t in thread_list:
    t.join()

time3 = time.clock()

print('Running time: %s Seconds' % (time3 - time1))

# try:
#     i = 0
#     # 开启线程数目
#     tasks_number = 500
#     time1 = time.clock()
#     while i < tasks_number:
#         t = threading.Thread(target=run_test)
#         t.start()
#         i += 1
#     time2 = time.clock()
#     times = time2 - time1
#     print(time2)
#     print(times / tasks_number)
#     print('Running time: %s Seconds' % (times))
# except Exception as e:
#     print(e)
# t.join()
