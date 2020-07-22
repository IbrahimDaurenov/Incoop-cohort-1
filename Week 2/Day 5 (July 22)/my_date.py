from datetime import datetime
import time



now = datetime.now()
moment1 = now.timestamp()

#print(now)
#print(now.day)
#print(now.year)
#print(now.month)
#print(now.hour)
#print(now.minute)
#print(now.second)
#print(now.timestamp())

now = datetime.now()
moment2 = now.timestamp()


print(moment2-moment1)
