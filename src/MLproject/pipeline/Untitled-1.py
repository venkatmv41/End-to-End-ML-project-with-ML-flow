 
from pathlib import Path
with open(Path("artifacts/data_validation/status.txt"), "r") as f:
    #status = f.read().strip(" ")[-1
    print(f.read().strip(":")[-4:])