#!/usr/bin/env python
def mol2gau(mol,gauinp,atm1,atm2,atm3,atm4):
    from rdkit import Chem
    """
    Convert RDKIT mol into ORCA constrained OPT input file.
    """
    cpu = '%PAL NPROCS 24 END'
    route = '! BP86 DEF2-TZVP D3BJ OPT'
    dihedral='{D '+str(int(atm1)-1)+' '+str(int(atm2)-1)+' '+str(int(atm3)-1)+' '+str(int(atm4)-1)+' C}'
    fout = open(gauinp,'w') 
    fout.write(cpu+'\n')
    fout.write(route+'\n')
    fout.write('%geom Constraints\n')
    fout.write(dihedral+"\n")
    fout.write('end\n')
    fout.write('end\n')
    n = mol.GetNumAtoms()
    formalcharge = str(Chem.rdmolops.GetFormalCharge(mol))
    fout.write('* xyz '+formalcharge+" 1\n")
    for i in range(n):
        pos = mol.GetConformer().GetAtomPosition(i)
        element = mol.GetAtoms()[i].GetSymbol()
        x = str(round(pos.x,4))
        y = str(round(pos.y,4))
        z = str(round(pos.z,4))
        fout.write(element+" "+x+" "+y+" "+z+'\n')
    fout.write("*\n")
    fout.write(" \n")
    fout.close()

if __name__ == "__main__":
    from rdkit import Chem
    import sys,string,argparse
    from optparse import OptionParser
    parser = argparse.ArgumentParser(description="Convert SDF to ORCA constrained OPT input file.\n")
    parser.add_argument('sdffile',metavar='<Input>',help="SDF file with full hydrogen")
    parser.add_argument('atom1',metavar='<atom1>',help="Atom 1")
    parser.add_argument('atom2',metavar='<atom2>',help="Atom 2")
    parser.add_argument('atom3',metavar='<atom3>',help="Atom 3")
    parser.add_argument('atom4',metavar='<atom4>',help="Atom 4")
    parser.add_argument('output',metavar='<Output>',help="G16 input file")
    args = parser.parse_args()
    sdffile = args.sdffile
    atm1 = args.atom1
    atm2 = args.atom2
    atm3 = args.atom3
    atm4 = args.atom4
    output = args.output
    suppl = Chem.SDMolSupplier(sdffile, removeHs=False)
    mol = suppl[0]
    mol2gau(mol,output,atm1,atm2,atm3,atm4)
