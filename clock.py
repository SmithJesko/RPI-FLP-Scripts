import fourletterphat as flp
import time
import os

os.environ['TZ'] = 'US/Central'
time.tzset()

def clock():
    try:
        t = time.localtime()
        now = time.strftime('%H%M', t)
        print(now)
        flp.print_str(str(now))
        flp.show()
        time.sleep(10)
        clock()
    except Exception as e:
        print(e)
        clock()

clock()
