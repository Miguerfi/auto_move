import os
import shutil
from pathlib import Path

mover = 1
original = 2

rMO = int(input("Deseja Mover(1) ou Restaurar(2)?"))
if rMO == 1:
    
    source = "dev_settings.py"
    dest = "mwdjango/"
    
    shutil.move(source, dest)
    print("dev_settings.py movida para mwdjango")
    
    oslist = os.listdir(dest)
    print(f"{oslist}")

    cors = """# CORS_ALLOWED_ORIGINS = [
#    'http://localhost:3000',
# ]"""
    rp = open('mwdjango/dev_settings.py')
    lines = rp.readlines()
    for row in lines:
        if row.find(cors):
            rep = cors.replace("""# CORS_ALLOWED_ORIGINS = [
#    'http://localhost:3000',
# ]""",""" CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
 ]""")

if rMO == 2:
    source = "mwdjango/dev_settings.py"
    dest = "dev_settings.py"
    shutil.move(source, dest)
    print("dev_settings.py foi restaurada para seu local de origem.")
