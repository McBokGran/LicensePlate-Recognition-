import jaydebeapi


conn = jaydebeapi.connect("org.h2.Driver", "jdbc:h2:~/data/demo", ["sa", ""])
curs = conn.cursor()
curs.execute("insert into VISITOR(VISITOR_ID, FIRST_NAME, IS_DELETED, LAST_NAME, LICENSE_PLATE,PHONE) values (1, 'John','False','Doe','XX123')")
curs.execute("select * from VISITOR")
data = curs.fetchall()
print(data)

#import psycopg2
#conn = psycopg2.connect("dbname=jdbc:h2:~/data/demo user=sa password= host=localhost port=8082")
#try:
 #       curs = conn.cursor()
  #      # Fetch the last 10 timestamps
   #     curs.execute("INSERT into VISITOR(VISITOR_ID, FIRST_NAME, IS_DELETED, LAST_NAME, LICENSE_PLATE,PHONE) values (1, 'John','False','Doe','XX123')")
    #    curs.execute("select * from VISITOR")
     #   print(curs.fetchall())
#finally:
 #       if curs is not None:
  #              curs.close()
   #     if conn is not None:
    #            conn.close()