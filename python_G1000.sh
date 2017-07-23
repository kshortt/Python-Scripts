#!/bin/bash
#$ -N python
#$ -pe make 8
#$ -j y
#$ -o output.$JOB_ID
#$ -cwd
#$ -q research.q
#$ -v PATH

python FileName.py
