from random import randint
import threading

from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.traversal import T

graph = Graph()
g = graph.traversal().withRemote(DriverRemoteConnection('ws://192.168.50.5:8182/gremlin','g'))


# AddNode
class AddNode():
    def addBasic(self):
        # basic
        mv1 = g.addV('Movie').property("tagline", "movie1").property("title", "The Matrix{random}").property("released", '1999').next()
        act1 = g.addV('Actor').property("name", "xxx1").property("gender","female").property("age","20").next()
        act2 = g.addV('Actor').property("name", "xxx2").property("gender","male").property("age","20").next()
        cop1 = g.addV('Company').property("name", "yyy1").property("date","2019年02月13日").next()
        cop2 = g.addV('Company').property("name", "yyy2").property("date","2019年02月13日").next()
        b1 =  g.addV('Boxoffice').property("total", "123,000").next()
        movetype1 = g.addV('Movietype').property("movietype", "horrible").next()

        g.withSideEffect('t', act1).V(mv1).addE('INVITE').to('t').next()
        g.withSideEffect('t', act2).V(mv1).addE('INVITE').to('t').next()
        g.withSideEffect('t', mv1).V(cop1).addE('INVEST').to('t').next()
        g.withSideEffect('t', mv1).V(cop2).addE('INVEST').to('t').next()
        g.withSideEffect('t', b1).V(mv1).addE('EARN').to('t').next()
        g.withSideEffect('t', movetype1).V(mv1).addE('MOVIETYPE').to('t').next()

    # 相同company
    def addSameCompany(self):
        randNameNum=randint(1,1000000)
        randActNum=randint(1,1000)
        randCopNum=randint(1,1000)

        cop1=g.V(16496) #yyy1 company
        cop2=g.V(41136) #yyy2 company
        movetype1 = g.V(41096) #horrible

        mv1 = g.addV('Movie').property("tagline", "movie1").property("title", "The Matrix"+str(randNameNum)).property("released", '1999').next()
        act1 = g.addV('Actor').property("name", "xxx"+str(randActNum)).property("gender","female").property("age","20").next()
        act2 = g.addV('Actor').property("name", "xxx"+str(randActNum)).property("gender","male").property("age","20").next()
        b1 =  g.addV('Boxoffice').property("total", "123,000").next()

        g.withSideEffect('t', act1).V(mv1).addE('INVITE').to('t').next()
        g.withSideEffect('t', act2).V(mv1).addE('INVITE').to('t').next()
        g.withSideEffect('t', mv1).V(cop1.next()).addE('INVEST').to('t').next()
        g.withSideEffect('t', mv1).V(cop2.next()).addE('INVEST').to('t').next()
        g.withSideEffect('t', b1).V(mv1).addE('EARN').to('t').next()
        g.withSideEffect('t', movetype1.next()).V(mv1).addE('MOVIETYPE').to('t').next()

    # 相同actor
    def addSameActor(self):
        randNameNum=randint(1,1000000)
        randActNum=randint(1,1000)
        randCopNum=randint(1,1000)

        act1=g.V(28808)
        act2=g.V(32904)
        movetype1 = g.V(41096) #horrible

        mv1 = g.addV('Movie').property("tagline", "movie1").property("title", "The Matrix"+str(randNameNum)).property("released", '1999').next()
        cop1 = g.addV('Company').property("name", "yyy"+str(randCopNum)).property("date","2019年02月13日").next()
        cop2 = g.addV('Company').property("name", "yyy"+str(randCopNum)).property("date","2019年02月13日").next()
        b1 =  g.addV('Boxoffice').property("total", "123,000").next()

        g.withSideEffect('t', act1.next()).V(mv1).addE('INVITE').to('t').next()
        g.withSideEffect('t', act2.next()).V(mv1).addE('INVITE').to('t').next()
        g.withSideEffect('t', mv1).V(cop1).addE('INVEST').to('t').next()
        g.withSideEffect('t', mv1).V(cop2).addE('INVEST').to('t').next()
        g.withSideEffect('t', b1).V(mv1).addE('EARN').to('t').next()
        g.withSideEffect('t', movetype1.next()).V(mv1).addE('MOVIETYPE').to('t').next()

def gogogo(addType, times):
    A = AddNode()
    if addType=="basic" :
        x=0
        while x<times:
            x+=1
            A.addBasic()
    elif addType=="cop":
        x=0
        while x<times:
            x+=1
            A.addSameCompany()
    elif addType=="act":
        x=0
        while x<times:
            x+=1
            A.addSameActor()

if __name__ == "__main__":
    thread_number = 1000
    threads = []
    i=0
    while i < thread_number:
        t = threading.Thread(target=gogogo(addType='cop',times=1000))
        t.start()
        threads.append(t)
        i+=1
