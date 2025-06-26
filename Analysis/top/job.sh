#!/bin/bash -l
#$ -l h_rt=48:00:0
#$ -l mem=4G
#$ -l tmpfs=10G
#$ -N TOP
#$ -pe smp 1
#$ -cwd

module purge
module load beta-modules
module unload -f compilers mpi gcc-libs
module load gcc-libs/7.3.0
module load compilers/gnu/7.3.0
module load mpi/openmpi/3.1.4/gnu-7.3.0
module load python/3.9.10 openblas/0.3.7-serial/gnu-4.9.2 python3/3.9
module load python3
module load gromacs/2021.2/gnu-7.3.0



# Delete preexisting files
rm -rf top-multiframe.txt
rm -rf angle-multiframe.txt
rm -rf all-polar1.pdb


for i in {180000..200000..2} # Loop over all the frames of the trajectory for last 10 ns
do
    gmx select -f ../noPBC.xtc -s ../prod.tpr -b $i -e $i -n ../index.ndx -select 'group OW' -on test.ndx # All 'OW' at all frames in a single index file
    gmx trjconv -f ../noPBC.xtc -s ../prod.tpr -b $i -e $i -n test.ndx -o selected-water.pdb
    echo 0 > system-index.txt
    gmx trjconv -f ../noPBC.xtc -s ../prod.tpr -b $i -e $i -o all-polar.pdb -n ../index.ndx < system-index.txt
    grep "ATOM" selected-water.pdb | awk '{print $5}' > selected.txt # Index of OW atoms
    grep 'O0\| OW\| N0' all-polar.pdb | awk '{print $2}' > c1.txt
    grep 'O0\| OW\| N0' all-polar.pdb | awk '{n = 6; for (--n; n >= 0; n--){ printf "%s\t",$(NF-n)} print ""}' > x.txt
    awk '{print $1, $2, $3}' x.txt > c2.txt
    paste c1.txt c2.txt | awk '{print $1, $2, $3, $4}' > all-polar.txt # Index and coordinates of all E.N. atoms
    rm -rf c1.txt c2.txt x.txt
    grep 'O0\| OW\| N0' all-polar.pdb >> all-polar1.pdb
    grep "ATOM" all-polar.pdb | grep "OW" | awk '{print $2, $5}' > all-water.txt
    python3 top.py
    rm \#*
    cat top.txt >> top-multiframe.txt
    cat angle.txt >> angle-multiframe.txt
done

awk '{if($1>-1) print $1}' top-multiframe.txt > y.txt #calculate the probability of q
python3 probability.py y.txt 100
mv output.txt hist-top.txt
python3 probability.py angle-multiframe.txt 100 # calculate the probability of angle (output file: hist-angle.txt)
mv output.txt hist-angle.txt
rm -rf y.txt