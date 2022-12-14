import os
import shutil
from pathlib import Path

mover = 1
original = 2


rMO = int(input("Move(1) or Restore(2)?"))
source = str(input("Archive Path Location:"))
dest = str(input("Destin Path:"))
        

if rMO == 1:
    shutil.move(source, dest)
    print(f"moved {source} to {dest}")
    
    oslist = os.listdir(dest)
    print(f"{oslist}")
if rMO == 2:
    shutil.move(source, dest)
    print(f"{source} restored to {dest}")

