from pathlib import Path
import os 

list_of_files = "D:/MV/SWCODES/PYTHON_RELATED\MLOPS/End-to-End-ML-project-with-ML-flow"
filepath = Path(list_of_files)

filedir,filename = os.path.split(list_of_files)
print(filedir)
print(filename)