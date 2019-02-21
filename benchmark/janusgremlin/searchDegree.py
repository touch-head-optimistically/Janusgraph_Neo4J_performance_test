import random
import time
import threading
import datetime

from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection


class delVertex():
    def __init__(self):
        graph = Graph()
        ip_pools = ['192.168.50.5', '192.168.50.6', '192.168.50.7']
        # ip_pools = ['192.168.50.5']
        request_ip = random.sample(ip_pools, 1)[0]
        self.g = graph.traversal().withRemote(DriverRemoteConnection('ws://' + request_ip + ':8182/gremlin', 'g'))

    def run(self):
        # self.g.addV().property("name", "wine").property("attr_name", "color").property("attr_value", 'red').next()
        # vf = self.g.V(606256)
        # vt = self.g.V(712744)
        # self.g.addE(vf, 'like', vt).next()
        # self.g.V(606256).as_('to').V(712744).addE("Likes").to('to').toList()
        # self.g.withSideEffect('t', vt).V(vf).addE('friend').to('t').next()
        self.g.V().has('username', 'wine').toList()


def runEdgeTest():
    d = delVertex()
    return d.run()


tasks_number = 1
thread_list = []  # 线程存放列表
# time1 = time.now()
for i in range(tasks_number):
    t = threading.Thread(target=runEdgeTest)
    t.setDaemon(True)
    thread_list.append(t)
print('start...',datetime.datetime.now().time())
for t in thread_list:
    t.start()

for t in thread_list:
    t.join()

print('end...',datetime.datetime.now().time())
# print('Running timex: %s Seconds' % (time.now() - time1))
