# plot

from matplotlib import pyplot as plt

def read_AR(AR_file):
    acc_rate = []
    t_rate = []
    f = open(AR_file)
    for line in f.readlines():
        line_arr = line.strip().split()
        if line_arr[0][0] == "#":
            continue
        acc_rate.append(float(line_arr[0]))
        t_rate.append(float(line_arr[1]))
    f.close()
    return acc_rate, t_rate

AR_list, TR_list = read_AR("accretion_rates.txt") 

print("Plotting ...")

plt.figure(figsize=(8,6))
plt.plot(TR_list, AR_list)
plt.title("Mass Accretion Rate")
plt.xlabel("Time (Myr)")  # 可改字体
plt.ylabel("Mass Accretion Rate (Msun/yr)")
plt.savefig("mass_accretion_rate.pdf")

print("Plotting... done.  mass_accretion_rate.pdf")
