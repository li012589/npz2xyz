# npz2xyz

A small python script to convert npz files to xyz files used in molecular dynamics.

## example:

```bash
python ./main.py -npz "./examples/alanine-dipeptide-3x250ns-heavy-atom-positions.npz" -xyz "./alanine-dipeptide-3x250ns-heavy-atom-positions.xyz" -name "arr_0" -smile "CC(=O)NC(C)C(=O)NC" -batch 2500 -join -fixy 23.222
```

