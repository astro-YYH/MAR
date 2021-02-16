# 大意了啊 还有 CPU threads
import sys


por_out_path = sys.argv[1]
num_out = str(-1 * int(sys.argv[2]))
n_thread = sys.argv[3]


with open("fmtramses.par") as fp:
    lines = fp.read().splitlines()
with open("fmtramses.par", "w") as fp:
    print("'" + por_out_path + "'" + "	   path to folder containing the RAMSES simulation output", file=fp)
    print(num_out + "	   	   Output No. (negative for all up to there, e.g. '-100' means all from 1 to 100)", file=fp)
    print(n_thread + "	   	   Number of CPU threads used for the RAMSES simulation", file=fp)
    j = 3
    while j < len(lines):
        print(lines[j], file=fp)
        j = j + 1
fp.close()
