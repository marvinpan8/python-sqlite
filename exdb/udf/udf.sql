create function psum(a integer,b integer) returns integer in 'python' as '
  import sys

  import pprint
  pprint.pprint ("UDF reports. eXtremeDB has runtime information: %s" %  exdb.get_runtime_info())

  print ("current session: %s" % current_session)
  print ("current runtime: %s" % current_runtime)

  return a+b
';

select psum(2,3);
