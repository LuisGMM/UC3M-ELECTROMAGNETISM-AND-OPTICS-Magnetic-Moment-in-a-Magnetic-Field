

B0 = 0.02 # mt pm 0.01 mt

                        #A pm 0.01, mt pm 0.01, V pm 0.01
offset_current_magnetic_voltage = [(0.02, 1.00, -0.65, 4.52),
                                   (0.02, 1.52, -0.98, 6.78),
                                   (0.02, 2.02, -1.32, 9.05),
                                   (0.02, 2.53, -1.65, 11.33),
                                   (0.02, 3.04, -1.99, 13.61)
]

offset, current, magnetic, voltage = zip(*offset_current_magnetic_voltage)
offset_magnetic_current_voltage = [list(offset), list(magnetic), list(current), list(voltage)]

# All this at 3A, to one side               # distance cm pm 0.5 mm, mt pm 0.01, V pm 0.01, A pm 0.01,
offset_zdistance_magnetic_voltage_current = [(0.04,  0, -1.99, 13.57, 3.02), 
                                             (0.04,  1, -1.98, 13.63, 3.04),
                                             (0.05,  2, -1.98, 13.66, 3.04),
                                             (0.04,  3, -1.98, 13.66, 3.04),
                                             (0.04,  4, -1.97, 13.68, 3.04),
                                             (0.04,  5, -1.97, 13.67, 3.04),
                                             (0.05,  6, -1.96, 13.69, 3.04),
                                             (0.04,  7, -1.95, 13.71, 3.04),
                                             (0.05,  8, -1.93, 13.71, 3.04), # Por aaqui empieza a salir
                                             (0.04,  9, -1.89, 13.71, 3.04),
                                             (0.06, 10, -1.85, 13.73, 3.04),
                                             (0.05, 11, -1.80, 13.73, 3.04),
                                             (0.05, 12, -1.74, 13.74, 3.04),
                                             (0.06, 13, -1.69, 13.75, 3.04),
                                             (0.05, 14, -1.63, 13.75, 3.04),
                                             (0.05, 15, -1.54, 13.77, 3.04),
                                             (0.05, 16, -1.47, 13.77, 3.04),
                                             (0.06, 17, -1.39, 13.77, 3.04),
                                             (0.06, 18, -1.31, 13.74, 3.04),
                                             (0.06, 19, -1.23, 13.74, 3.04),
                                             (0.05, 20, -1.15, 13.74, 3.04),
]

offset, zdistance, magnetic, voltage, current = zip(*offset_zdistance_magnetic_voltage_current)
offset_magnetic_z_distance_current_voltage = [list(offset), list(magnetic), list(zdistance), list(current), list(voltage)]


# All this at 3A, to the other side till the center of the coil
offset_zdistance_magnetic_voltage_current2 = [(0.07,  -0, -1.97, 13.65, 3.04),
                                             (0.07,  -1, -1.96, 13.66, 3.04),
                                             (0.07,  -2, -1.96, 13.67, 3.04),
                                             (0.06,  -3, -1.95, 13.67, 3.04),
                                             (0.06,  -4, -1.95, 13.68, 3.04),
                                             (0.06,  -5, -1.94, 13.69, 3.04),
                                             (0.07,  -6, -1.93, 13.69, 3.04),
                                             (0.07,  -7, -1.92, 13.70, 3.04),
                                             (0.08,  -8, -1.89, 13.70, 3.04),
                                             (0.07,  -9, -1.87, 13.70, 3.04),  # Por aqui llega al centro del centro del right coil
                                             (0.07, -10, -1.82, 13.71, 3.04),
]

offset, zdistance, magnetic, voltage, current = zip(*offset_zdistance_magnetic_voltage_current2)
offset_magnetic_z_distance_current_voltage2 = [list(offset), list(magnetic), list(zdistance), list(current), list(voltage)]

# All this at 3A, hacia adelante till the extreme of the coil
offset_zdistance_magnetic_voltage_current3 = [(0.13,  0, -1.90, 13.65, 3.04),
                                             (0.13,  1, -1.90, 13.65, 3.04),
                                             (0.12,  2, -1.90, 13.67, 3.04),
                                             (0.13,  3, -1.90, 13.67, 3.04),
                                             (0.13,  4, -1.90, 13.67, 3.04),
                                             (0.13,  5, -1.89, 13.68, 3.04),
                                             (0.13,  6, -1.89, 13.68, 3.04),
                                             (0.13,  7, -1.87, 13.69, 3.04),
                                             (0.14,  8, -1.86, 13.69, 3.04),
                                             (0.13,  9, -1.86, 13.69, 3.04),
                                             (0.14, 10, -1.81, 13.70, 3.04),
                                             (0.13, 11, -1.77, 13.71, 3.04),
                                             (0.14, 12, -1.71, 13.73, 3.04),
                                             (0.14, 13, -1.62, 13.74, 3.04),
                                             (0.14, 14, -1.51, 13.74, 3.04),
                                             (0.13, 15, -1.41, 13.75, 3.04),
                                             (0.14, 16, -1.25, 13.75, 3.04),
                                             (0.14, 17, -1.11, 13.75, 3.04),
                                             (0.14, 18, -0.88, 13.75, 3.04),
]

offset, zdistance, magnetic, voltage, current = zip(*offset_zdistance_magnetic_voltage_current2)
offset_magnetic_z_distance_current_voltage3 = [list(offset), list(magnetic), list(zdistance), list(current), list(voltage)]

# All this at 3A, hacia detras till the extreme of the coil
offset_zdistance_magnetic_voltage_current4 = [(0.14,  0, -1.89, 13.72, 3.04),
                                             (0.14, -1, -1.89, 13.72, 3.04),
                                             (0.14, -2, -1.89, 13.73, 3.04),
                                             (0.14, -3, -1.89, 13.73, 3.04),
                                             (0.13, -4, -1.89, 13.73, 3.04),
                                             (0.14, -5, -1.88, 13.73, 3.04),
                                             (0.14, -6, -1.88, 13.73, 3.04),
                                             (0.14, -7, -1.88, 13.74, 3.04),
                                             (0.15, -8, -1.86, 13.74, 3.04),
                                             (0.14, -9, -1.85, 13.74, 3.04),
                                             (0.14, -10, -1.83, 13.75, 3.04),
                                             (0.15, -11, -1.80, 13.75, 3.04),
                                             (0.15, -12, -1.76, 13.75, 3.04),
                                             (0.14, -13, -1.69, 13.76, 3.04),
                                             (0.14, -14, -1.62, 13.76, 3.04),
                                             (0.14, -15, -1.50, 13.76, 3.04),
                                             (0.15, -16, -1.40, 13.76, 3.04),
                                             (0.14, -17, -1.23, 13.77, 3.04),
                                             (0.14, -18, -1.07, 13.78, 3.04),
]

offset, zdistance, magnetic, voltage, current = zip(*offset_zdistance_magnetic_voltage_current2)
offset_magnetic_z_distance_current_voltage4 = [list(offset), list(magnetic), list(zdistance), list(current), list(voltage)]

# scale in mN pm 0.05
# A
bigcoil_smallcoil_miliNewton = [(3.04, 5.08, 3),
                                (2.53, 5.08, 2.5),
                                (2.03, 5.08, 2.0),
                                (1.52, 5.08, 1.5),
                                (1.01, 5.08, 1.1),
]

bigcoil, smallcoil, miliNewton = zip(*bigcoil_smallcoil_miliNewton)
bigcoil_smallcoil_miliNewton = [list(bigcoil), list(smallcoil), list(miliNewton)]



if __name__=='__main__':

    offset, current, magnetic, voltage = zip(*offset_current_magnetic_voltage)
    offset_magnetic_current_voltage = [list(offset), list(magnetic), list(current), list(voltage)]

    print(offset_current_magnetic_voltage)
    print(offset_magnetic_current_voltage)