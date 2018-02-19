#!/bin/bash 
#$ -l h_rt=00:05:00
#$ -l h_vmem=5G 
#$ -S /hpc/local/CentOS7/dhl_ec/software/sevpy/1/bin/python 
#$ -cwd 
#$ -o /home/dhl_ec/hseverin/logs/pi
#$ -e /home/dhl_ec/hseverin/logs/pi 
#$ -N piarray
 
import socket, math, random, os

taskid = os.environ["SGE_TASK_ID"]

def piguess(rounds):
    count_inside = 0
    for count in range(rounds):
        d = math.hypot(random.random(), random.random())
        if d < 1:    
                count_inside += 1
    pi =  4.0 * count_inside / rounds
    return pi

pi = piguess(100000000)

with open('/home/dhl_ec/hseverin/tests/pis/pi_%s'% str(taskid), 'w') as out:
        out.write(str(pi))

