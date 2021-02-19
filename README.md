# MAR-2.2

This is a code for calculating Mass Accretion Rate from RAMSES simulations, developed by Yanhui Yang. It should be used together with *extract_por* developed by Ingo Thies. The accretion radius is set as 0.01 pc currently, which could be modified if needed. 

## Dependencies  
- Python3
- Shell
- Whatever required by *extract_por*

## Files inside ZIP archive  
- README.md
- fmtramses.par (This parameter file is used by xpordata.x. Please use this file instead of the original one from *extract_por*, unless you want to set those parameters by yourself.)
- MAR.py
- mar_funcs.py
- modify_par.py
- plot_mar.py
- xmar.sh

## Installation
There is no specific operations for installing MAR (mainly python), but you need a executable binary from *extrac_por*. So all you need do are:  
1. Download MAR-XX.zip to your device and extract files from it to /path/to/MAR/.
2. Compile *extract_por* and get the binary, *xpordata.x*. (If you have been using *BonnPoR*, you will find a folder named "extract_por". And you could compile the code according to its *README.txt*. Else, you could get this tool from https://github.com/GFThomas/MOND)

## Usage
You just need do a few simple operations to realize your goal to get accretion rates:  
1. Copy *xpordata.x* to /path/to/MAR/.
2. Set 3 parameters in *xmar.sh*， e.g.,
   ```
   path="/home/yang/bonnpor/runs/plummer_sample/"  # path to the folder containing the RAMSES simulation output
   N_out="66"  # total number of outputs from RAMSES sims
   n_thread="4"  # Number of CPU threads used for the RAMSES simulation
   ```
   Explanation: The *plummer_sample* folder contains a series of folders named "output_\*\*\*\*\*". When *N_out* is set to "66", all outputs from 1 to 66 will be analysed.
3. Execute programs:
   ```
   $ bash xmar.sh
   ```
You will get files you want:  
- accretion_rates.txt  
- mass_accretion_rate.pdf (a plot figure showing the evolution of mass accretion rate)  

and some folders containing files from *extract_por*:  
- images
- times 
- particles  

