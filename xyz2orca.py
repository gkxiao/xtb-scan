#!/usr/bin/env python
def mol2gau(mol,charge,gauinp,atm1,atm2,atm3,atm4):
    """
    create ORCA constrained OPT input file for xyz.
    """
    cpu = '%PAL NPROCS 24 END'
    route = '! BP86 DEF2-TZVP D3 OPT RIJCOSX Def2/J'
    dihedral='{D '+str(int(atm1)-1)+' '+str(int(atm2)-1)+' '+str(int(atm3)-1)+' '+str(int(atm4)-1)+' C}'
    fout = open(gauinp,'w') 
    fout.write(cpu+'\n')
    fout.write(route+'\n')
    fout.write('%geom Constraints\n')
    fout.write(dihedral+"\n")
    fout.write('end\n')
    fout.write('end\n')
    fout.write('* xyzfile '+charge+' 1 '+mol+'\n')
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
    mol2gau(xyzfile,charge,output,atm1,atm2,atm3,atm4)
