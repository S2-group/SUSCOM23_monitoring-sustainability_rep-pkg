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
        
        self.offset = 135

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
            ax.set_rgrids(range(0, 5), angle=angle, labels=label)
            ax.spines['polar'].set_visible(False)
            ax.set_ylim(0, 4)
            ax.bar(np.deg2rad(angle), 5, bottom=0.0, width=np.deg2rad(360.0/self.n), facecolor=color, alpha=0.4)

    def plot(self, values, *args, **kw):
        angle = np.deg2rad(np.r_[self.angles, self.angles[0]])
        values = np.r_[values, values[0]]
        self.ax.plot(angle, values, *args, **kw)
        self.ax.fill(angle, values, kw['color'], alpha=0.15)
    
    def rescale(self, v, maxNew, minNew, maxOld, minOld):
        newVal = ((maxNew-minNew)/(maxOld-minOld)) * (v-maxOld) + maxNew
        print(newVal)
        return newVal


if __name__ == '__main__':
    fig = plt.figure(figsize=(8, 8))

    colTech = '#5DB6E2'
    colEnv = '#B6D86A'
    colSoc = '#FED970'
    colEco = '#E1565E'

    tit = ['Technical', 'Environmental', 'Social', 'Economic']
    col = [colTech, colEnv, colSoc, colEco]


    # NORMALIZED labels
    labNorm = [
        ['0', '0.25', '0.5', '0.75', '1'],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', '']
    ]


    # NORMALIZED
    radar = Radar(fig, tit, labNorm, col)
    radar.plot([
        radar.rescale(0.40000,4,0,1,0),
        radar.rescale(0.466667,4,0,1,0),
        radar.rescale(0.527778,4,0,1,0),
        radar.rescale(0.600000,4,0,1,0)], '-', lw=2, color='b', alpha=0.8, label='Governance & Security')
    
    radar.plot([
        radar.rescale(0.5577615,4,0,1,0),
        radar.rescale(0.300000,4,0,1,0),
        radar.rescale(0.514286,4,0,1,0),
        radar.rescale(0.260870 ,4,0,1,0)], '-', lw=2, color='r', alpha=0.8, label='PCS Messaging Portal')

    radar.ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2))
    fig.savefig('result_NORM.pdf')