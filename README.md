# pdbUtils

## Usage
This is a small python module that can parse PDB files as pandas DataFrames. 

PDB formatting can be all over the place depending on how they have been created. 
PdbUtils has been written such that it tolerates all sorts of weird stuff when reading a PDB file, but writes PDB files strictly according to PDB formatting rules:
https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html

You can load a pdb file as a DataFrame by:
```python
import pdbUtils

myPdbFile = "/home/eugene/5xh3.pdb"

pdbDf = pdbUtils.pdb2df(myPdbFile)
```
Once loaded as a DataFrame, you can modiy and interrogate it to your heart's content. 
You can access each column of your new DataFrame using the following column names:
```python
print(pdbDf["ATOM"])            ## string "ATOM" or "HETATM"
print(pdbDf["ATOM_ID"])         ## int atom number 
print(pdbDf["ATOM_NAME"])       ## string atom name (eg. "OG")
print(pdbDf["RES_NAME"])        ## string residue name (eg. "SER")
print(pdbDf["CHAIN_ID"])        ## chain identifier (eg. "B")
print(pdbDf["RES_ID"])          ## string residue number (eg. "131")
print(pdbDf["X"])               ## float X coordinate
print(pdbDf["Y"])               ## float Y coordinate
print(pdbDf["Z"])               ## float Z coordinate
print(pdbDf["OCCUPANCY"])       ## float occupancy (usually 1.00 or 0.00)
print(pdbDf["BETAFACTOR"])      ## float betafactor or pLDDT if it's a structural prediction
print(pdbDf["ELEMENT"])         ## string element (eg. "O")
```



When you want to write back to a PDB file:
```python
outPdbFile = "home/eugene/5xh3_new.pdb"
pdbUtils.pdb2df(pdbDf, outPdbFile)
```

I have also added the function to read AutoDock PDBQT files in the same manner:
```python
import pdbUtils

myPdbqtFile = "/home/eugene/5xh3.pdbqt"

pdbDf = pdbUtils.pdbqt2df(myPdbFile)
```

## Installation

1. Clone this repo

```bash
git clone https://github.com/ESPhoenix/pdbUtils
```

2. Install Pandas (unless you already have it!)
``` bash
pip install pandas
``` 
