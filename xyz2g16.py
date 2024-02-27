#!/usr/bin/env python
def xyz2gau(xyzfile,charge,gauinp,atm1,atm2,atm3,atm4):
    """
    create Gaussian 16 constrained OPT input file from xyz.
    """
    prefix_xyzfile,format=xyzfile.split('.')
    dihedral=str(atm1)+' '+str(atm2)+' '+str(atm3)+' '+str(atm4)
    check = '%chk='+prefix_xyzfile+'_D_'+str(atm1)+'-'+str(atm2)+'-'+str(atm3)+'-'+str(atm4)+'_constrained_opt.chk'
    route = '# B3LYP/6-311+G(d,p) OPT=(modredundant) symmetry=(none) EmpiricalDispersion=(gd3bj)'
    fout = open(gauinp,'w') 
    fout.write(check+'\n')
    fout.write(route+'\n')
    fout.write('\n')
    fout.write(prefix_xyzfile+' Dihedral angle '+str(atm1)+'-'+str(atm2)+'-'+str(atm3)+'-'+str(atm4)+' constrained optimization\n')
    fout.write('\n')
    fout.write(charge+' 1\n')
    f=open(xyzfile,'r')
    lines = f.readlines()
    f.close()
    for i in range(2,len(lines)):
        fout.write(lines[i])
    fout.write('\n')
    fout.write(dihedral+' F\n')
    fout.write('\n')
    fout.close()
if __name__ == "__main__":
    import sys,string,argparse
    from optparse import OptionParser
    parser = argparse.ArgumentParser(description="Create ORCA input file for xzy file.\n")
    parser.add_argument('xyzfile',metavar='<Input>',help="XYZ file with full hydrogen")
    parser.add_argument('charge',metavar='<charge>',help="formal charge")
    parser.add_argument('atom1',metavar='<atom1>',help="Atom 1")
    parser.add_argument('atom2',metavar='<atom2>',help="Atom 2")
    parser.add_argument('atom3',metavar='<atom3>',help="Atom 3")
    parser.add_argument('atom4',metavar='<atom4>',help="Atom 4")
    parser.add_argument('output',metavar='<Output>',help="ORCA input file")
    args = parser.parse_args()
    xyzfile = args.xyzfile
    charge = args.charge
    atm1 = args.atom1
    atm2 = args.atom2
    atm3 = args.atom3
    atm4 = args.atom4
    output = args.output
    xyz2gau(xyzfile,charge,output,atm1,atm2,atm3,atm4)
