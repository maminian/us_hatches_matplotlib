from matplotlib import pyplot
import json
import numpy as np

np.random.seed(2718)  # play with seed for different patterns

# data via https://eric.clst.org/tech/usgeojson/
with open('gz_2010_us_040_00_20m.json', 'r') as f:
    state_json = json.load(f)

# following available hatches seen at
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.patches.Polygon.html
hatches = ('/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*')

fig,ax = pyplot.subplots(1,1, constrained_layout=True, figsize=(11,6))

for j,state in enumerate( np.random.permutation(state_json['features']) ):
    for subregion in state['geometry']['coordinates']:
        # need to squeeze due to quirks in data structure
        xy = np.squeeze(subregion)
        ax.fill(xy[:,0], xy[:,1], fc='w', ec='k', hatch=hatches[j % len(hatches)], zorder=3)

ax.set_xlim([-125,-65])
ax.set_ylim([24,51])
ax.grid(zorder=-3)

ax.set_title('United Hatches of America', fontsize=18, loc='left', ha='left')

fig.show()
fig.savefig('united_hatches_of_america.png', dpi=120)
