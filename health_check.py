import shutil
import psutil

def disk_usage(disk):
   du = shutil.disk_usage(disk)
   free = du.free / du.total *100
   print("free:",free)
   return free > 20

def cpu_percent_usage():
  pu = psutil.cpu_percent(1)
  print("cpu percentage for 1 sec:",pu)
  return pu < 70

if not disk_usage("/") or not cpu_percent_usage():
   print("ERROR!!")

else:
   print("EVERY THING OK!!")