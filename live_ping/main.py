import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime as dt
from subprocess import check_output
from sys import argv
plt.style.use('fivethirtyeight')
plt.xticks(rotation=90)

x_values = []
y_values = []

def animate(i, x_values, y_values):
    try:
        time = str(check_output(["ping", argv[1], "-c", "1", "-W", "1"])).split("time=")[1].split("ms")[0]
        time = time.replace(" ","")
    except:
        time=-1

    x_values.append(dt.datetime.now().strftime('%H:%M:%S'))
    y_values.append(float(time))

    if(len(x_values)>20):
        x_values = x_values[-20:]
        y_values = y_values[-20:]

    plt.cla()
    plt.xticks(rotation=45)
    plt.plot(x_values, y_values)
    plt.rc("font", size=10)
    plt.title(argv[1])
    #plt.ylim(-3,1000)
ani = FuncAnimation(plt.gcf(), animate, fargs=(x_values, y_values), interval=500)


plt.tight_layout()
plt.show()
