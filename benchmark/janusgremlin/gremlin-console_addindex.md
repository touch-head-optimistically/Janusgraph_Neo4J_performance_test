:remote connect tinkerpop.server conf/remote.yaml session
graph = JanusGraphFactory.open('conf/janusgraph-cassandra-solr.properties')

:remote console


mgmt = graph.openManagement()

graph.getOpenTransactions()
mgmt.getOpenInstances()
mgmt.forceCloseInstance('c0a8320514454-node71')

graph.io(graphml()).readGraph('/ssd/xx/janusgraph/performance_test/zhwiki-20110127-pages-meta-current.graphml')


graph.io(graphml()).readGraph('/ssd/xx/janusgraph/learn-gremlin-jupyter-notebook/data/air-routes.graphml')



write_request_timeout_in_ms: 20000



size = graph.getOpenTransactions().size();
for(i=0;i<size;i++) {graph.getOpenTransactions().getAt(0).rollback()}


REGISTER_INDEX Registers the index with all instances in the graph cluster. After an index is installed, it must be registered with all graph instances
REINDEX Re-builds the index from the graph
ENABLE_INDEX Enables the index so that it can be used by the query processing engine. An index must be registered before it can be enabled.
DISABLE_INDEX Disables the index in the graph so that it is no longer used.
REMOVE_INDEX Removes the index from the graph (optional operation). Only on composite index.


#add property
hehe = mgmt.makePropertyKey('hehe').dataType(String.class).cardinality(Cardinality.SET).make()


graph.tx().rollback()

#REGISTER
size = graph.getOpenTransactions().size();
for(i=0;i<size;i++) {graph.getOpenTransactions().getAt(0).rollback()}

mgmt = graph.openManagement()
code = mgmt.getPropertyKey('code')
mgmt.buildIndex('byCodeComposite', Vertex.class).addKey(code).buildCompositeIndex()
mgmt.commit()

m = graph.openManagement()
m.updateIndex(m.getGraphIndex("byCodeComposite"), SchemaAction.REGISTER_INDEX).get()
m.commit()

ManagementSystem.awaitGraphIndexStatus(graph, 'byCodeComposite').call()

#REINDEX
graph.tx().rollback()
size = graph.getOpenTransactions().size();
for(i=0;i<size;i++) {graph.getOpenTransactions().getAt(0).rollback()}

mgmt = graph.openManagement()
mgmt.updateIndex(mgmt.getGraphIndex("byicaoComposite"), SchemaAction.REINDEX).get()
mgmt.commit()
ManagementSystem.awaitGraphIndexStatus(graph, 'byicaoComposite').status(SchemaStatus.ENABLED).call()

#ENABLE
m = graph.openManagement()
m.updateIndex(m.getGraphIndex('byicaoComposite'), SchemaAction.ENABLE_INDEX).get() 
m.commit() 
ManagementSystem.awaitGraphIndexStatus(graph, 'byicaoComposite').status(SchemaStatus.ENABLED).call()

#test
g.V().has('icao', '123').profile()


mgmt = graph.openManagement()
it=mgmt.getOpenInstances().iterator(); while (it.hasNext()){ nxt=it.next(); if(!nxt.contains("current"))  mgmt.forceCloseInstance(nxt)}
mgmt.commit()








size = graph.getOpenTransactions().size();
for(i=0;i<size;i++) {graph.getOpenTransactions().getAt(0).rollback()}  //Never create new indexes while a transaction is active
mgmt = graph.openManagement()
name = mgmt.getPropertyKey('name')
age = mgmt.getPropertyKey('age')
mgmt.buildIndex('booksBySummary', Vertex.class).addKey(summary, Mapping.TEXTSTRING.asParameter()).buildMixedIndex("search")
mgmt.buildIndex('zz', Vertex.class).addKey(name).addKey(age).buildMixedIndex("search")
mgmt.updateIndex(mgmt.getGraphIndex("zz"), SchemaAction.REGISTER_INDEX).get()
mgmt.commit()
ManagementSystem.awaitGraphIndexStatus(graph, 'zz').call()

#ENABLE
m = graph.openManagement()
m.updateIndex(m.getGraphIndex('byicaoComposite'), SchemaAction.ENABLE_INDEX).get() 
m.commit() 
ManagementSystem.awaitGraphIndexStatus(graph, 'byicaoComposite').status(SchemaStatus.ENABLED).call()

