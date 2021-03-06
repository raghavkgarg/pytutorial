import datetime
import matplotlib.pyplot as plt
import numpy as np

import plotly.plotly as py
py.sign_in('raghav.garg', 'eukk6jkugw')
import plotly.tools as tls

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api
plotly.offline.plot({
x = np.array([datetime.datetime(2014, i, 9) for i in range(1,13)])
y = np.random.randint(100, size=x.shape)

plt.plot(x,y)
plt.tight_layout()

fig = plt.gcf()
plotly_fig = tls.mpl_to_plotly( fig )

plotly_url = py.plot(plotly_fig, filename='mpl-time-series')
