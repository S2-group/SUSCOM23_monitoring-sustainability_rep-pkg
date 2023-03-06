"""
Based on:
https://gist.github.com/geberl/c65517bf8273552486f9a8954e80ddf4
Retrieved:
2021-09-10
Installation: Get the *Miniconda* Python Distribution - not the Python distrubution from python.org!
- https://conda.io/miniconda.html
Then install modules:
- `cd ~/miniconda3/bin`
- `./conda install numpy pandas matplotlib`
Original source:
- https://stackoverflow.com/questions/24659005/radar-chart-with-multiple-scales-on-multiple-axes
- That code has problems with 5+ axes though
"""

import numpy as np
import matplotlib.pyplot as plt

class Radar(object):
    def __init__(self, figure, title, labels, colors, rect=None):
        if rect is None:
            rect = [0.15, 0.15, 0.7, 0.7]
        
        self.offset = 126

        self.n = len(title)
        self.angles = np.arange(0, 360, 360.0/self.n)
        self.angles = self.angles + self.offset
        self.angles = self.angles % 360

        self.axes = [figure.add_axes(rect, projection='polar', label='axes%d' % i) for i in range(self.n)]

        self.ax = self.axes[0]
        self.ax.set_thetagrids(self.angles, labels=title, fontsize=14)
        self.ax.tick_params(pad=30)

        for ax in self.axes[1:]:
            ax.patch.set_visible(False)
            ax.grid(False)
            ax.xaxis.set_visible(False)

        for ax, angle, label, color in zip(self.axes, self.angles, labels, colors):
            ax.set_rgrids(range(1, 6), angle=angle, labels=label)
            ax.spines['polar'].set_visible(False)
            ax.set_ylim(0, 5)
            ax.bar(np.deg2rad(angle), 5, bottom=0.0, width=np.deg2rad(360.0/self.n), facecolor=color, alpha=0.4)

    def plot(self, values, *args, **kw):
        angle = np.deg2rad(np.r_[self.angles, self.angles[0]])
        values = np.r_[values, values[0]]
        self.ax.plot(angle, values, *args, **kw)
        self.ax.fill(angle, values, kw['color'], alpha=0.15)
    
    def rescale(self, v, maxNew, minNew, maxOld, minOld):
        newVal = ((maxNew-minNew)/(maxOld-minOld)) * (v-maxOld) + maxNew
        print(v, ' = ', newVal)
        return newVal
    
    def rescale2(self, x, xmin, xrange, n):
        y = ((x - xmin) / xrange) * n
        print(y)
        return y


if __name__ == '__main__':
    fig = plt.figure(figsize=(8, 8))

    tit = ['# of\nIncidents\n(n/a)', 'Security Risk\nScore', 'Satisfaction\n(n/a)', '# of SSL\nVulnerabilities', 'Cyber Risk Score']
    col = ['#5DB6E2', '#B6D86A', '#FED970', '#FED970', '#E1565E']

    # STANDARD labels
    lab = [
        ['0', '', '', '', ''],
        ['5', '4', '3', '2', '1'],
        ['0', '2.5', '5', '7.5', '10'],
        ['20', '15', '10', '5', '0'],
        ['100', '75', '50', '25', '0']
    ]

    # Plot
    radar = Radar(fig, tit, lab, col)
    radar.plot([
        radar.rescale(1,5,1,5,1),
        radar.rescale(2.8,5,1,1,5),
        radar.rescale(0,5,1,10,0),
        radar.rescale(17,5,1,0,20),
        radar.rescale(29.63,5,1,0,100)], '-', lw=2, color='b', alpha=0.8, label='2021')

    # EXPECTED
    radar.plot([5,5,5,5,5], '-', lw=2, color='k', alpha=1.0, label='expected')

    radar.ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2))
    fig.savefig('result_Security.pdf')