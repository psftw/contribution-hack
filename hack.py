import os
import datetime
import Image

tdate = datetime.datetime(2012, 9, 30, 17, 0)
oneday = datetime.timedelta(days=1)

def commit(num):
    for i in range(num):
        os.system('date >> commits')
        os.system('git add commits && git commit -m "github contribution hack"')
    
def setdate(td):
    os.system('date -u %s' % td.strftime('%m%d%H%M%Y'))
    
img = Image.open('yay.png')
lookup = {238: 0, 214: 1, 140: 2, 68: 4, 30: 6}
cdata = []
for x in range(0, 664, 13):
    for y in range(0, 79, 13):
            setdate(tdate)
	    tdate += oneday
            if y == 0:
                cdata.append([])
            r, g, b, a = img.getpixel((x,y))
            cdata[-1].append(lookup[r])
            commit(lookup[r])
            
