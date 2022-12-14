import os
import shutil
from pathlib import Path

mover = 1
original = 2

rMO = int(input("Deseja Mover(1) ou Restaurar(2)?"))
if rMO == 1:
    
    source = ""
    dest = ""
    
    shutil.move(source, dest)
    print(f"moved {source} to {dest}")
    
    oslist = os.listdir(dest)
    print(f"{oslist}")

if rMO == 2:
    source = ""
    dest = ""
    shutil.move(source, dest)
    print(f"{source} restored to {dest}")
