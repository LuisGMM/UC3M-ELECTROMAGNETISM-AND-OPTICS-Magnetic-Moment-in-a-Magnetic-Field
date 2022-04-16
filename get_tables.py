
import data_hemlotz as D
from to_latex import to_latex



def do_nothing(x):
    return f'{x}'



# print(to_latex(col_names=[r'$B_{off} (\pm 0.01 mT)$', '$B (\pm 0.01 mT)$', '$I ( \pm 0.01 A)$',
#                      '$Voltage ( \pm 0.01 V)$'],
#         cols=D.offset_magnetic_current_voltage,
#         index=False,
#         escape=False,
#         column_format='cccc',
# ))


# print(to_latex(col_names=[r'$B_{off} (\pm 0.01 mT)$', '$B (\pm 0.01 mT)$', '$Z (\pm 0.5 m)$', '$I ( \pm 0.01 A)$',
#                      '$Voltage ( \pm 0.01 V)$'],
#         cols=D.offset_magnetic_z_distance_current_voltage,
#         index=False,
#         escape=False,
#         column_format='ccccc',
#         formatters=[do_nothing, do_nothing, lambda x: str(round(float(x), 1)), do_nothing, do_nothing]
# ))

# print(to_latex(col_names=[r'$B_{off} (\pm 0.01 mT)$', '$B (\pm 0.01 mT)$', '$Z (\pm 0.5 m)$', '$I ( \pm 0.01 A)$',
#                      '$Voltage ( \pm 0.01 V)$'],
#         cols=D.offset_magnetic_z_distance_current_voltage2,
#         index=False,
#         escape=False,
#         column_format='ccccc',
#         formatters=[do_nothing, do_nothing, lambda x: str(round(float(x), 1)), do_nothing, do_nothing]
# ))

# print(to_latex(col_names=[r'$B_{off} (\pm 0.01 mT)$', '$B (\pm 0.01 mT)$', '$Z (\pm 0.5 m)$', '$I ( \pm 0.01 A)$',
#                      '$Voltage ( \pm 0.01 V)$'],
#         cols=D.offset_magnetic_z_distance_current_voltage3,
#         index=False,
#         escape=False,
#         column_format='ccccc',
#         formatters=[do_nothing, do_nothing, lambda x: str(round(float(x), 1)), do_nothing, do_nothing]
# ))

# print(to_latex(col_names=[r'$B_{off} (\pm 0.01 mT)$', '$B (\pm 0.01 mT)$', '$Z (\pm 0.5 m)$', '$I ( \pm 0.01 A)$',
#                      '$Voltage ( \pm 0.01 V)$'],
#         cols=D.offset_magnetic_z_distance_current_voltage4,
#         index=False,
#         escape=False,
#         column_format='ccccc',
#         formatters=[do_nothing, do_nothing, lambda x: str(round(float(x), 1)), do_nothing, do_nothing]
# ))

# print(to_latex(col_names=[r'$A_{Big coil} (\pm 0.01 A)$', '$A_{Small coil} (\pm 0.01 A)$', '$Force ( \pm 0.05 mN)$'],
#         cols=D.bigcoil_smallcoil_miliNewton,
#         index=False,
#         escape=False,
#         column_format='ccc',
#         formatters=[do_nothing, do_nothing, lambda x: str(round(float(x), 2))],
# ))