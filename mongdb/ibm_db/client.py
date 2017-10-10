import ibm_db
print(ibm_db.__file__)
conn = ibm_db.connect("DATABASE=emsdb;HOSTNAME=192.168.163.129;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=tivoli;", "", "")

  #  if conn:
   #     sql = "SELECT * from tablename"
    #    stmt = ibm_db.exec_immediate(conn, sql)
    #    result = ibm_db.fetch_both(stmt)
     #   while( result ):
      #      print "Result :", result[0]
       #     result = ibm_db.fetch_both(stmt)