package main

// package zz

// import (
// 	"bytes"
// 	"encoding/json"
// 	"errors"
// 	"fmt"
// 	"math/rand"
// 	"net/http"
// 	"strings"
// 	"time"

// 	gin "datatom/gin.v1"
// )

// type stateX struct {
// 	Statement string `json:"statement"`
// }

// type AutoGenerated struct {
// 	Statements []stateX `json:"statements"`
// }

// func HttpGet(ip string, port int, uri string, body string) (response []byte, err error) {
// 	url := fmt.Sprintf("http://%s:%d%s",
// 		ip,
// 		port,
// 		uri)

// 	client := &http.Client{}

// 	req, err := http.NewRequest("POST", url, strings.NewReader(body))
// 	if err != nil {
// 		return []byte(""), err
// 	}

// 	req.SetBasicAuth("neo4j", "123456")
// 	req.Header.Set("Content-Type", "application/json")

// 	resp, err := client.Do(req)
// 	if err != nil {
// 		return []byte(""), err
// 	}

// 	defer resp.Body.Close()

// 	buf := new(bytes.Buffer)
// 	buf.ReadFrom(resp.Body)

// 	var errget error
// 	if resp.StatusCode != 200 {
// 		errget = errors.New(string(buf.Bytes()))
// 	}

// 	return buf.Bytes(), errget
// }

// func main() {
// 	x := 0
// 	//var wg sync.WaitGroup
// 	for {
// 		if x < 1 {
// 			// wg.Add(1)
// 			// go func() {
// 			// 	defer wg.Done()
// 			r := rand.New(rand.NewSource(time.Now().UnixNano()))
// 			randNum := r.Intn(1000000)
// 			ip := "192.168.50.5"
// 			port := 21811

// 			// 新增关于2个公司的
// 			// queryString_company := fmt.Sprintf("MATCH (company1:Company) WHERE company1.name=\"yyy1\" MATCH (company2:Company) WHERE company2.name=\"yyy2\" MATCH (movetype1:Movietype) WHERE movetype1.movietype=\"horrible\" CREATE (matrix1:Movie {tagline:\"movie2\",title:\"The Matrix%d\",released:\"1999\"}) CREATE (actor1:Actor {name:\"xxx%d\",gender:\"female\",age:\"20\"}) CREATE (actor2:Actor {name:\"xxx%d\",gender:\"male\",age:\"20\"}) CREATE (b1:Boxoffice {total:\"123,000\"}) CREATE (matrix1)-[r1:INVITE]->(actor1) CREATE (matrix1)-[r2:INVITE]->(actor2) CREATE (company1)-[r3:INVEST]->(matrix1) CREATE (company2)-[r4:INVEST]->(matrix1) CREATE (matrix1)-[r5:EARN]->(b1) CREATE (matrix1)-[r6:MOVIETYPE]->(movetype1) RETURN matrix1,actor1,actor2,company1,company2,b1,movetype1",
// 			// 	randNum, randNum, randNum)

// 			// 新增关于2个演员的
// 			queryString_actor := fmt.Sprintf("MATCH (actor1:Actor) WHERE actor1.name=\"xxx1\" MATCH (actor2:Actor) WHERE actor2.name=\"xxx2\" MATCH (movetype1:Movietype) WHERE movetype1.movietype=\"horrible\" CREATE (matrix1:Movie {tagline:\"movie1\",title:\"The Matrix%d\",released:\"1999\"}) CREATE (company1:Company {name:\"yyy%d\",date:\"2019年02月13日\"}) CREATE (company2:Company {name:\"yyy%d\",date:\"2019年02月13日\"}) CREATE (b1:Boxoffice {total:\"123,000\"}) CREATE (matrix1)-[r1:INVITE]->(actor1) CREATE (matrix1)-[r2:INVITE]->(actor2) CREATE (company1)-[r3:INVEST]->(matrix1) CREATE (company2)-[r4:INVEST]->(matrix1) CREATE (matrix1)-[r5:EARN]->(b1) CREATE (matrix1)-[r6:MOVIETYPE]->(movetype1) RETURN matrix1,actor1,actor2,company1,company2,b1,movetype1",
// 				randNum, randNum, randNum)
// 			// fmt.Println(queryString)

// 			s := stateX{}
// 			//s.Statement = queryString
// 			s.Statement = queryString_actor

// 			var ss []stateX
// 			body := gin.H{
// 				"statements": append(ss, s),
// 			}

// 			zz, _ := json.Marshal(body)

// 			// fmt.Println(string(zz))

// 			_, err := HttpGet(ip, port, "/db/data/transaction/commit", string(zz))
// 			// fmt.Println(string(res))
// 			if err != nil {
// 				fmt.Println(err.Error())
// 				fmt.Println("failed")
// 				return
// 			}
// 			// }()
// 			x++
// 		} else {
// 			break
// 		}
// 	}
// 	// wg.Wait()
// 	// fmt.Print("pass")
// }
