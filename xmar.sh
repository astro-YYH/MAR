#!/bin/bash

path="/home/yang/bonnpor/runs/plummer_sample/"  # path to folder containing the RAMSES simulation output
N_out="66"  # total number of outputs from RAMSES sims
n_thread="4"  # Number of CPU threads used for the RAMSES simulation

python modify_par.py ${path} ${N_out} ${n_thread}

./xpordata.x

python MAR.py
python plot_mar.py

rm -rf images; mkdir images 
mv image*.dat images
rm -rf particles; mkdir particles
mv part*.asc particles
rm -rf "times"; mkdir "times"  
mv gpa*.txt "times"
rm sfr.dat "times.dat"
