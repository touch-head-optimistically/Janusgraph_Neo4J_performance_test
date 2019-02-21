1步邻居：
g.V().hasLabel('Boxoffice').has('total','123,000').in('EARN').count() 24920ms

MATCH (n1:Boxoffice {total:'123,000'})<-[r:EARN]-(n2) RETURN count(n2) 1629ms

2步邻居
g.V().hasLabel('Boxoffice').has('total','123,000').in('EARN').out('INVITE').count() 26524ms

MATCH (n1:Boxoffice {total:'123,000'})<-[r:EARN]-(n2)
MATCH (n2)-[x:INVITE]->(n3)
RETURN count(n3),count(n2)4443ms

3步邻居：
g.V().hasLabel('Boxoffice').has('total','123,000').in('EARN').out('INVITE').in('INVITE').count() 125726ms

MATCH (n1:Boxoffice {total:'123,000'})<-[r:EARN]-(n2)
MATCH (n2)-[r2:INVITE]->(n3)
MATCH (n3)<-[r2:INVITE]-(n4)
RETURN count(n4),count(n2),count(n3) 9057ms

4步邻居：
g.V().hasLabel('Boxoffice').has('total','123,000').in('EARN').out('INVITE').in('INVITE').out('MOVIETYPE').count() 96867ms  

MATCH (n1:Boxoffice {total:'123,000'})<-[r:EARN]-(n2)
MATCH (n2)-[r2:INVITE]->(n3)
MATCH (n3)<-[r2:INVITE]-(n4)
MATCH (n4)-[r3:MOVIETYPE]->(n5)
RETURN count(n2), count(n3), count(n4), count(n5)
11897ms


neo4j

2.37GB
文件节点1,033,103
总结点 4,132,415
总关系6,198,618



janusgraph
文件节点 1,043,516
总结点 4
总关系


 g.V().hasLabel('Boxoffice').has('total','123,001').in('EARN').groupCount().by('title').profile() 9614ms