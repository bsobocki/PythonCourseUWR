import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from playfield import play_field

system = {
    "lights":[(12,12),(13,12),(14,12)],
    "frog":[(12,12),(13,12),(13,12),(13,13),(14,13),(15,13)],
    "fountain": [(2,2),(2,3),(2,7),(2,8),
                 (3,1),(3,2),(3,4),(3,6),(3,8),(3,9),
                 (4,4),(4,6),
                 (5,4),(5,6),
                 (7,3),(7,4),(7,6),(7,7)]
}

pf = play_field(30)
pf.set_initial_system(system["lights"])

fig = plt.figure()
im = plt.imshow(pf.data, animated=True)
plt.title('Gra W Zycie')


def updatefig(i):
    if pf.iteration == 10:
        pf.set_initial_system(system["frog"])
    elif pf.iteration == 20:
        pf.set_initial_system(system["fountain"])
    im.set_array(pf.next_step())
    return im,

ani = animation.FuncAnimation(fig, updatefig,  interval=300, blit=True)

plt.show()