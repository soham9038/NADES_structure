#!/bin/bash -l
#$ -l h_rt=48:00:0
#$ -l mem=4G
#$ -l tmpfs=10G
#$ -N cluster
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



################################# Cluster calculation ######################################

python3 clusteranalysis.py


# File processing

cut -d' ' -f6- cluster_output.txt > x1.txt
tr -d ',[]' < x1.txt > x2.txt
awk '{for(i=1;i<=NF;i++) if($i > 2) printf $i (i<NF ? OFS : ""); print ""}' x2.txt > x3.txt # Cluster which contains more than 2 water molecules
awk '{print NF}' x3.txt > clusternumber_perframe.txt
awk '{for(i=1;i<=NF;i++) print $i}' x3.txt > clustersize.txt
rm -rf x*.txt
mv cluster_output.txt rawoutput_water.txt
