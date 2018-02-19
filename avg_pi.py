#$ -l h_rt=00:01:00
#$ -l h_vmem=0.5G 
#$ -S /hpc/local/CentOS7/dhl_ec/software/sevpy/1/bin/python 
#$ -cwd 
#$ -o /home/dhl_ec/hseverin/logs/pi 
#$ -e /home/dhl_ec/hseverin/logs/pi
#$ -N pypiavg

import numpy, os
from glob import glob

pifiles = glob(os.path.join('/home/dhl_ec/hseverin/tests/pis/pi_*'))
pis = list()
for pifile in pifiles:
	pis.append(float(open(pifile, 'r').read()))

print(len(pis))
pimean = numpy.mean(pis)

with open('/home/dhl_ec/hseverin/tests/pis/result.txt', 'w') as out:
	out.write(str(pimean))

