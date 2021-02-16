import numpy as np


# physical constant in cgs unit system
G = 6.6726e-8
M_sun = 1.99e33
c = 2.99792458e10
kpc = 3.086e21


# functions
def get_part(datafile):
    f = open(datafile)
    part_pos = []
    part_mass = []
    for line in f.readlines():
        line_arr = line.strip().split()
        part_pos.append([float(line_arr[0]), float(line_arr[1]), float(line_arr[2])])
        part_mass.append(float(line_arr[6]))
        #part_pos.append([float(line_arr[0]), float(line_arr[1]), float(line_arr[2]), float(line_arr[6]), float(line_arr[3])]) #temp 3
    f.close()
    return part_pos, part_mass

def accretion_radius(M):  # radius in kpc
    return (2 * G * M * M_sun)/(c**2) * 1e10/kpc

def mass_center(part_pos, part_mass):  # for verification, extract_por has the coordinate original point in (0, 0, 0). 
    total_mass = np.sum(part_mass)
    pos_x_m = [0,0,0]
    j = 0
    while j < 3:
        k = 0
        while k < len(part_pos):  # 第 k + 1 个 particle
            pos_x_m[j] = pos_x_m[j] + part_pos[k][j] * part_mass[k]  
            k = k + 1       
        j = j + 1
    COM = np.array(pos_x_m)/total_mass
    return COM

def internal_M(part_pos, part_mass, R):  # Assuming the center of mass is at (0, 0, 0)   If necessary, the real COM will be used.
    M_R = 0
    j = 0
    while j < len(part_mass):
        r_power2 = part_pos[j][0]**2 + part_pos[j][1]**2 + part_pos[j][2]**2
        if r_power2 < R**2:  # r refers to the distance between the particle and the COM
            M_R = M_R + part_mass[j]
        j = j + 1
    return M_R

''' 用于探索 extract_por 速度单位
def get_v(particles):
    v = []
    for part in part_list:
        v.append(part[4])
    return v
'''
def get_x(part_pos):
    x = []
    for part in part_pos:
        x.append(part[0])
    return x

def get_acc_rate(M_R_list, time_list):
    acc_rate = []
    t_rate = []
    j = 1
    while j < len(M_R_list):
        dM = M_R_list[j] - M_R_list[j-1]
        dt = time_list[j] - time_list[j-1]
        acc_rate.append(dM/(1e6*dt))  # Msun/yr
        t_rate.append((time_list[j] + time_list[j-1])/2)
        j = j + 1
    return acc_rate, t_rate

def write_AR(acc_rate, t_rate, output_name):
    print("Writing accretion rate file.\n")
    AR_file = open(output_name, "w")
    AR_file.write("#accretion rate in Msun/yr  time in Myr\n")
    j = 0
    while j < len(acc_rate):
        AR_file.write("%8.5e  %8.2f\n" % (acc_rate[j], t_rate[j]))
        j = j + 1
    AR_file.close()
    print("Done.\n")

def get_time(file_list):
    time = []
    for fn in file_list:
        f = open(fn)
        line_arr = f.readlines()[0].strip().split()
        time.append(float(line_arr[1]))
        f.close()
    print("Time: %s Myr." % time) 
    return time   