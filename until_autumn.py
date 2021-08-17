from datetime import datetime, timedelta

def until():
    now = datetime.now()

    autumn = datetime(now.year, 9, 1, 0 , 0, 0)

    delta_autumn = autumn - now
    percent = delta_autumn.total_seconds() / (92 * 24 * 60 * 60) * 100
    format = float('%.3f' % percent)
    return format

while(True):
    print( f'От лета осталось {until()} %' ); input()
