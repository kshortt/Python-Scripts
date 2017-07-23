#!/bin/bash
#$ -N python
#$ -pe make X
#$ -j y
#$ -o output.$JOB_ID
#$ -cwd
#$ -q research.q
#$ -v PATH

python FileName.py
