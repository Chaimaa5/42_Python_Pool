import datetime
from time import time
timenow = time()
date = datetime.datetime.now()
print(f"Seconds since January 1, 1970: {timenow} or {timenow:.2e} in scientific notation")
print (date.strftime("%b %d %Y"))