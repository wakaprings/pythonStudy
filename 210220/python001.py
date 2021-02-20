# import sqlite3

# #conn = sqlite3.connect("test_sqlite.db")
# # テスト用にメモリ上にDBを作成する
# conn = sqlite3.connect(":memory:")
# conn.close()

# https://qiita.com/kenmatsu4/items/f75616461dc5c63ecfe1
# neo4jは正当にインストールしてみる

# neo4j
# http://192.168.100.142:7474
# C:\tools\neo4j-community\neo4j-community-3.5.1\conf\neo4j.conf
# <修正ライン>
# #dbms.connectors.default_listen_address=0.0.0.0  
# dbms.connectors.default_listen_address=0.0.0.0
# <再起動>
# C:\tools\neo4j-community\neo4j-community-3.5.1\bin\tools\prunsrv-amd64.exe //RS//neo4j
# 21年2月20日のみのパスワード
# user : neo4j / pass : rt3Jpf0PYd3U65a6

# https://neo4j.com/docs/api/python-driver/current/
from neo4j import GraphDatabase
uri = "bolt://192.168.100.142:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "rt3Jpf0PYd3U65a6"))

def create_friend_of(tx, name, friend):
    tx.run("MATCH (a:Person) WHERE a.name = $name "
           "CREATE (a)-[:KNOWS]->(:Person {name: $friend})",
           name=name, friend=friend)

with driver.session() as session:
    session.write_transaction(create_friend_of, "Alice", "Bob")

with driver.session() as session:
    session.write_transaction(create_friend_of, "Alice", "Carl")

driver.close()