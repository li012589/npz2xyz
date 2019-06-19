import numpy as np

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-npz",default=None,help = "name of the npz file")
parser.add_argument("-xyz",default=None,help = "name of the xyz file")
parser.add_argument("-name",default=None,help = 'name of the data saved in npz file')
parser.add_argument("-smile",default=None,help = "Smile expression of the molecule")
parser.add_argument("-batch",default=100,type=int,help = "batch size of configurations to convert")
parser.add_argument("-scaling",default=10,type=float,help = "scaling factor of npz data, default is for nm to ångströms")
parser.add_argument("-join",action='store_true',help="store all into one xyz file")
args = parser.parse_args()

smiles = []
for cha in args.smile:
    if cha.isalpha():
        smiles.append(cha)
smiles = ''.join(smiles)
N = len(smiles)

with np.load(args.npz) as data:
    argOne = data[args.name].reshape(-1,N,3)*args.scaling

if args.join:
    with open(args.xyz,"w") as f:
        for n in range(args.batch):
            f.write(str(N)+"\n"+args.smile+"\n")
            for i,cha in enumerate(smiles):
                f.write(cha+"  "+str(argOne[n,i,0])+"  "+str(argOne[n,i,1])+"  "+str(argOne[n,i,2])+"\n")


else:
    for n in range(args.batch):
        with open(args.xyz.replace(".xyz",str(n)+".xyz"),"w") as f:
            f.write(str(N)+"\n"+args.smile+"\n")
            for i,cha in enumerate(smiles):
                f.write(cha+"  "+str(argOne[n,i,0])+"  "+str(argOne[n,i,1])+"  "+str(argOne[n,i,2])+"\n")
