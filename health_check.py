import shutil
import psutil

def disk_usage(disk):
   du = shutil.disk_usage(disk)
   free = du.free / du.total *100
   print("free:",free)
   return free > 20
def available_memory_check():
   available= psutil.virtual_memory().available
   available_in_mb= available /1024 **2
   return available_in_mb > 500
   
def cpu_percent_usage():
  pu = psutil.cpu_percent(1)
  print("cpu percentage for 1 sec:",pu)
  return pu < 80

if not disk_usage("/"):
   print("ERROR !!-DISK USAGE MORE THAN 80%")
   
elif not available_memory_check():
   print("ERROR!!- Available memory is less than 500mb")

elif not cpu_percent_usage():
   print("ERROR!!-CPU USAGE morethan 80%")

else:
   print("EVERY THING OK!!")
