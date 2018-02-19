#!/bin/bash
qsub -t 1-30 /home/dhl_ec/hseverin/tests/pypi.py
qsub -hold_jid piarray /home/dhl_ec/hseverin/tests/avg_pi.py
