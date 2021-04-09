import porespy as ps
import matplotlib.pyplot as plt
import openpnm as op
ps.settings.notebook = False

# np.random.seed(3)
im1 = ps.generators.blobs(shape=[200, 200, 200], porosity=None, blobiness=2) < 0.4
im2 = ps.generators.blobs(shape=[200, 200, 200], porosity=None, blobiness=2) < 0.7
phases = im1 + (im2 * ~im1)*2
# phases = phases > 0

snow_n = ps.networks.snow2(phases,
                           phase_alias={1: 'solid', 2: 'void'},
                           boundary_width=5,
                           return_all=True,
                           accuracy='high')

fig = plt.figure()
plt.imshow(snow_n.regions.T)

pn, geo = op.io.PoreSpy.import_data(snow_n.network)
op.topotools.plot_connections(network=pn, fig=fig)
op.topotools.plot_coordinates(network=pn, fig=fig)
plt.axis('off')
