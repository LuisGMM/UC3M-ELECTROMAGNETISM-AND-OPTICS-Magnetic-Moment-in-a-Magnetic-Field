
import numpy as np

import data_hemlotz as D
from leastsq import leastsq

offset, current, magnetic, voltage = zip(*D.offset_current_magnetic_voltage)


results_5_1_3 = leastsq(x=np.array(current), y=np.array(magnetic), sigma=0.01)

print(results_5_1_3)


x = np.array(current) - np.array(offset)

results_5_1_3 = leastsq(x=x, y=np.array(magnetic), sigma=0.01)

print(results_5_1_3)