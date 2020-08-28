import sys, os, io, pathlib, pyclbr 
from pathlib import Path
from AutoDRF import AutoDRF

if __name__=='__main__':
	a = Path(os.getcwd())
	E = AutoDRF(ProjectPath=a)
	E.ApplyProject()     

