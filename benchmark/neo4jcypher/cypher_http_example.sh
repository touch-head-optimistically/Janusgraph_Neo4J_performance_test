curl.sh

#!/bin/bash

QUERY=query.json

time curl -i -XPOST \
    -o output.log \
    --data "@$QUERY" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    http://127.0.0.1:7474/db/data/transaction/commit




query.json
{
    "statements": [
        {
            "statement": "MATCH (d:Decision) WHERE id(d) = {decisionId} MATCH (c:Criterion) WHERE id(c) = {criterionId} WITH d, c MATCH (d)<-[:VOTED_FOR]-(vg:VoteGroup)-[:VOTED_ON]->(c) RETURN vg",
            "parameters": {
                "decisionId": "1",
                "criterionId": "1"
            }
        }
    ]
}