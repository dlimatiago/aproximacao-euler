import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('dark_background')


class Animar:
    def __init__(self, pos):
        step = int(pos.shape[0] * .01)
        xmaxlim, ymaxlim = abs(np.max(pos[:, 0])) + 5e2, abs(np.max(pos[:, 0])) + 5e2

        self.xskip = pos[::step if step > 0 else 1, 0]
        self.yskip = pos[::step if step > 0 else 1, 1]
        self.x = pos[:, 0]
        self.y = pos[:, 1]

        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(-xmaxlim, xmaxlim), ylim=(-ymaxlim, ymaxlim))
        self.fig.set_size_inches(15, 15)
        self.lines = [plt.plot([], [], 'oy', ms=30, mfc='darkorange')[0],
                      plt.plot([], [], 'ob', mfc='royalblue')[0],
                      plt.plot([], [], 'g--')[0]]

    def update(self):
        # init lines
        for line in self.lines:
            line.set_data([], [])

        return self.lines  # return everything that must be updated

    def animate(self, i):
        # animate lines
        self.lines[0].set_data(0, 0)
        self.lines[1].set_data(self.xskip[i], self.yskip[i])
        self.lines[2].set_data(self.xskip[:i], self.yskip[:i])

        return self.lines  # return everything that must be updated

    def animation(self):
        plt.title('Trajetória do corpo com relação ao Sol')
        plt.axis('off')
        ani = FuncAnimation(self.fig, self.animate, init_func=self.update, frames=len(self.xskip), interval=25, blit=True)
        ani.save('trajetoria.gif')


if __name__ == '__main__':
    x = np.random.randint(3e2, size=(1000, 2))
    print(np.min(x[:, 0]))
