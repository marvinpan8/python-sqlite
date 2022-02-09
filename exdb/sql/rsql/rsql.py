import exdb

is_disk = False
tmgr = 'mursiw'
is_shm = False
is_debug = False

#Load Runtime configuration specified by parameters
exdb.init_runtime(is_disk, tmgr, shm=is_shm, debug=is_debug)

conn = exdb.connect('localhost', 5001)

cursor = conn.cursor()
cursor.execute("create table MyTable (pk int, value string)")
cursor.execute("insert into MyTable (pk,value) values (?,?)", (2012, "Good bye"))
cursor.execute("insert into MyTable (pk,value) values (?,?)", (2013, "Hello"))
cursor.execute("insert into MyTable (pk,value) values (?,?)", (2014, "Hello world!"))

cursor.execute("select pk,value from MyTable where pk>=?", (2013,))
row = cursor.fetchall()
cursor.close()

print ("Server returned row:")
print (row)

print("Server stats: %s" % conn.stats)

conn.close()
