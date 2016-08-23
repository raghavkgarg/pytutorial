import urllib2       # (*) urllib2 for in-session downloads
import pandas as pd  # (*) pandas for dataframe manipulation
import matplotlib.pyplot as plt
mpl_fig_obj= plt.figure()
import plotly.plotly as py
py.sign_in('raghav.garg', 'eukk6jkugw')

# Import data file from URL into pd datafram in session
data_url = 'http://datasets.flowingdata.com/crimeRatesByState2005.csv'
data_file = urllib2.urlopen(data_url)  
df = pd.read_csv(data_file, sep=',')

df = df.drop(df.index[0])  # drop first row (US totals) 
df = df[df['murder'] < 11] # drop out-of-range rows

mpl_fig_bubble = plt.figure()         # (!) set new mpl figure object
ax = mpl_fig_bubble.add_subplot(111)  # add axis

plt.axis([0,11,200,1280])
plt.xlabel('Murders per 100,000 population')
plt.ylabel('Burglaries per 100,000 population')

scatter = ax.scatter(
    df['murder'], 
    df['burglary'], 
    c=df['larceny_theft'],        # using some color scale
    s=np.sqrt(df['population']),
    linewidths=2, 
    edgecolor='w',
    alpha=0.6
)

for i_X, X in df.iterrows():
    plt.text(
        X['murder'],
        X['burglary'],
        X['state'][0:8], # only the first 8 letters
        size=8,
        horizontalalignment='center'
    )
    py.iplot_mpl(mpl_fig_bubble, filename='s6_bubble-chart')
  