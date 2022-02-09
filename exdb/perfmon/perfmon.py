import exdb

# define input for python 2
try:
    input = raw_input
except NameError:
    pass

schema = '''
#define uint4     unsigned<4>
declare database opendb;
class myclass  {
uint4 i4;
};
'''

exdb.init_runtime(disk=False, tmgr='mursiw', shm=False, debug=False, UsePerfmon=True)

mcodict = exdb.load_dictionary(schema, persistent=False, debug=False)
db = exdb.open_database(dbname='mydb', dictionary=mcodict, is_disk=False, db_segment_size=128*1024*1024)

exdb.Perfmon.init()
exdb.Perfmon.attach(db)

hv = exdb.HV()
print(dir(hv))
print (hv, hv.metadict, hv.hv)
hv.start()

input("Point your web browser to http://localhost:8082. Or Press Enter to stop...")

hv.stop()

exdb.Perfmon.detach(db)
exdb.Perfmon.close()
