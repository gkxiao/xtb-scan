#!/usr/bin/env python
import os,sys,string
from rdkit import Chem
from rdkit.Chem import rdMolTransforms
import numpy as np

if len(sys.argv) != 6:
    print("")
    print("usage:  ")
    print(sys.argv[0]," <input sdf file> <dihedral atom index:3,2,8,4>")
    print("For example:")
    print(sys.argv[0],"xtbscan.sdf 3 2 8 4")
    print("Any question, Please feel free to contact me. info@molcalx.com")
    sys.exit()


sdf_file = sys.argv[1]
if not os.path.exists(sdf_file):
   #message = "Sorry, I cannot find the "%s" file."
   print("Sorry, Cannot find the %s file" % sdf_file)
   sys.exit()

atm1 = int(sys.argv[2]) - 1
atm2 = int(sys.argv[3]) - 1
atm3 = int(sys.argv[4]) - 1
atm4 = int(sys.argv[5]) - 1

suppl = Chem.SDMolSupplier(sdf_file, removeHs=False)
pose = 0
energys = []
angles = []
confs = []
for mol in suppl:
    pose = pose + 1
    conf = mol.GetConformer(0)
    angle = rdMolTransforms.GetDihedralDeg(conf,atm1,atm2,atm3,atm4)
    title = mol.GetProp('_Name')
    energy = float(title.split()[1])
    conf_id = 'CONF_'+str(pose)
    confs.append(conf_id)
    angles.append(angle)
    energys.append(energy)

energy_min=min(energys)
#print(energys)
#print('energy min=',energy_min)
rel_energys = []
for energy in energys:
    energy = round(627.5*(float(energy) - float(energy_min)),3)
    rel_energys.append(energy)
print('CONF_ID,Angle,Relative_energy')
for i in range(len(confs)):
    conf_id = confs[i]
    angle = round(float(angles[i]),2)
    energy = rel_energys[i]
    print(f'{conf_id},{angle},{energy}')


