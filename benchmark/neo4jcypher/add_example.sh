初始化
CREATE (matrix1:Movie {tagline:"movie1",title:"The Matrix{random}",released:"1999"})
CREATE (actor1:Actor {name:"xxx1",gender:"female",age:"20"})
CREATE (actor2:Actor {name:"xxx2",gender:"male",age:"20"})
CREATE (company1:Company {name:"yyy1",date:"2019年02月13日"})
CREATE (company2:Company {name:"yyy2",date:"2019年02月13日"})
CREATE (b1:Boxoffice {total:"123,000"})
CREATE (movetype1:Movietype {movietype:"horrible"})
CREATE (matrix1)-[r1:INVITE]->(actor1)
CREATE (matrix1)-[r2:INVITE]->(actor2)
CREATE (company1)-[r3:INVEST]->(matrix1)
CREATE (company2)-[r4:INVEST]->(matrix1)
CREATE (matrix1)-[r5:EARN]->(b1)
CREATE (matrix1)-[r6:MOVIETYPE]->(movetype1)
RETURN matrix1,actor1,actor2,company1,company2,b1,movetype1

CREATE (matrix1:Movie {tagline:"movie1",title:"The Matrix{random}",released:"1999"}) CREATE (actor1:Actor {name:"xxx1",gender:"female",age:"20"}) CREATE (actor2:Actor {name:"xxx2",gender:"male",age:"20"}) CREATE (company1:Company {name:"yyy1",date:"2019年02月13日"}) CREATE (company2:Company {name:"yyy2",date:"2019年02月13日"}) CREATE (b1:Boxoffice {total:"123,000"}) CREATE (movetype1:Movietype {movietype:"horrible"}) CREATE (matrix1)-[r1:INVITE]->(actor1) CREATE (matrix1)-[r2:INVITE]->(actor2) CREATE (company1)-[r3:INVEST]->(matrix1) CREATE (company2)-[r4:INVEST]->(matrix1) CREATE (matrix1)-[r5:EARN]->(b1) CREATE (matrix1)-[r6:MOVIETYPE]->(movetype1) RETURN matrix1,actor1,actor2,company1,company2,b1,movetype1



match (n) detach delete n


同公司
MATCH (company1:Company) WHERE company1.name="yyy1"
MATCH (company2:Company) WHERE company2.name="yyy2"
MATCH (movetype1:Movietype) WHERE movetype1.movietype="horrible"
CREATE (matrix1:Movie {tagline:"movie2",title:"The Matrix{random}",released:"1999"})
CREATE (actor1:Actor {name:"xxx{random}",gender:"female",age:"20"})
CREATE (actor2:Actor {name:"xxx{random}",gender:"male",age:"20"})
CREATE (b1:Boxoffice {total:"123,000"})
CREATE (matrix1)-[r1:INVITE]->(actor1)
CREATE (matrix1)-[r2:INVITE]->(actor2)
CREATE (company1)-[r3:INVEST]->(matrix1)
CREATE (company2)-[r4:INVEST]->(matrix1)
CREATE (matrix1)-[r5:EARN]->(b1)
CREATE (matrix1)-[r6:MOVIETYPE]->(movetype1)
RETURN matrix1,actor1,actor2,company1,company2,b1,movetype1

MATCH (company1:Company) WHERE company1.name="yyy1" MATCH (company2:Company) WHERE company2.name="yyy2" MATCH (movetype1:Movietype) WHERE movetype1.movietype="horrible" CREATE (matrix1:Movie {tagline:"movie2",title:"The Matrix{random}",released:"1999"}) CREATE (actor1:Actor {name:"xxx{random}",gender:"female",age:"20"}) CREATE (actor2:Actor {name:"xxx{random}",gender:"male",age:"20"}) CREATE (b1:Boxoffice {total:"123,000"}) CREATE (matrix1)-[r1:INVITE]->(actor1) CREATE (matrix1)-[r2:INVITE]->(actor2) CREATE (company1)-[r3:INVEST]->(matrix1) CREATE (company2)-[r4:INVEST]->(matrix1) CREATE (matrix1)-[r5:EARN]->(b1) CREATE (matrix1)-[r6:MOVIETYPE]->(movetype1) RETURN matrix1,actor1,actor2,company1,company2,b1,movetype1


同演员
MATCH (actor1:Actor) WHERE actor1.name="xxx1"
MATCH (actor2:Actor ) WHERE actor2.name="xxx2"
MATCH (movetype1:Movietype) WHERE movetype1.movietype="horrible"
CREATE (matrix1:Movie {tagline:"movie1",title:"The Matrix{random}",released:"1999"})
CREATE (company1:Company {name:"yyy{random}",date:"2019年02月13日"})
CREATE (company2:Company {name:"yyy{random}",date:"2019年02月13日"})
CREATE (b1:Boxoffice {total:"123,000"})
CREATE (matrix1)-[r1:INVITE]->(actor1)
CREATE (matrix1)-[r2:INVITE]->(actor2)
CREATE (company1)-[r3:INVEST]->(matrix1)
CREATE (company2)-[r4:INVEST]->(matrix1)
CREATE (matrix1)-[r5:EARN]->(b1)
CREATE (matrix1)-[r6:MOVIETYPE]->(movetype1)
RETURN matrix1,actor1,actor2,company1,company2,b1,movetype1



MATCH (actor1:Actor) WHERE actor1.name="xxx1" MATCH (actor2:Actor ) WHERE actor2.name="xxx2" MATCH (movetype1:Movietype) WHERE movetype1.movietype="horrible" CREATE (matrix1:Movie {tagline:"movie1",title:"The Matrix{random}",released:"1999"}) CREATE (company1:Company {name:"yyy{random}",date:"2019年02月13日"}) CREATE (company2:Company {name:"yyy{random}",date:"2019年02月13日"}) CREATE (b1:Boxoffice {total:"123,000"}) CREATE (matrix1)-[r1:INVITE]->(actor1) CREATE (matrix1)-[r2:INVITE]->(actor2) CREATE (company1)-[r3:INVEST]->(matrix1) CREATE (company2)-[r4:INVEST]->(matrix1) CREATE (matrix1)-[r5:EARN]->(b1) CREATE (matrix1)-[r6:MOVIETYPE]->(movetype1) RETURN matrix1,actor1,actor2,company1,company2,b1,movetype1


