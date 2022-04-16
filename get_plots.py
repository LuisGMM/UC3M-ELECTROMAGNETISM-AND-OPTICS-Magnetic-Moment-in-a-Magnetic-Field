
import matplotlib.pyplot as plt

import data_hemlotz as D



# offset, current, magnetic, voltage = zip(*D.offset_current_magnetic_voltage)

# plt.title(r'$B_{z=0, r=0}$ vs I')
# plt.ylabel(r'$B_{z=0, r=0} \ (mT)$')
# plt.xlabel(r'$I \ (A)$')

# plt.errorbar(current, magnetic, 0.01, 0.01, capsize=3, linewidth=1, linestyle='--', color='black')
# # plt.scatter(current, magnetic, color='black')
# # plt.plot(current, magnetic, color='black')

# plt.show()




# offset, zdistance1, magnetic1, voltage, current = zip(*D.offset_zdistance_magnetic_voltage_current)
# offset, zdistance_neg, magnetic_neg, voltage, current = zip(*D.offset_zdistance_magnetic_voltage_current2)

# plt.title(r'$B_{r=0}$ vs Z')
# plt.ylabel(r'$B_{r=0} \ (mT)$')
# plt.xlabel(r'$Z \ (cm)$')

# plt.errorbar([*zdistance_neg[::-1], *zdistance1[1:]], [*magnetic_neg[::-1], *magnetic1[1:]], 0.01, 0.05, capsize=3, linewidth=1, linestyle='--', color='black')
# # plt.scatter(current, magnetic, color='black')
# # plt.plot(current, magnetic, color='black')

# plt.show()



offset, zdistance1, magnetic1, voltage, current = zip(*D.offset_zdistance_magnetic_voltage_current3)
offset, zdistance_neg, magnetic_neg, voltage, current = zip(*D.offset_zdistance_magnetic_voltage_current4)

plt.title(r'$B_{z=0}$ vs R')
plt.ylabel(r'$B_{z=0} \ (mT)$')
plt.xlabel(r'$R \ (cm)$')

plt.errorbar([*zdistance_neg[::-1], *zdistance1[1:]], [*magnetic_neg[::-1], *magnetic1[1:]], 0.01, 0.05, capsize=3, linewidth=1, linestyle='--', color='black')
# plt.scatter(current, magnetic, color='black')
# plt.plot(current, magnetic, color='black')

plt.show()