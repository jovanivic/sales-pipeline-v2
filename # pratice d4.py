# PURPOSE: read every CSV in a folder, remove repeat orders,
# save one clean file. Safe to re-run (output is overwritten).

from pathlib import Path
import pandas as pd

# 1. SETUP
# base = Path(__file__).parent.parent
# input_folder = base / "dumbledore"
# output_folder = base / "output"     

# 2. EXTRACT

# frames = []
# for file in sorted(input_folder.glob("*.csv")):
#     df = pd.read_csv(file)
#     print(file.name, len(df))
#     frames.append(df)               

# print(len(frames))                      
# print(frames[0].equals(frames[1]))      

# 3. COMBINE
# combined = pd.concat(frames, ignore_index=True)

# 4. INSPECT (look BEFORE you fix)
# print(combined.dtypes)                            
# print(combined.isna().sum())                      
# print(combined["order_id"].duplicated().sum())    

# 5. CLEAN
# clean = combined.drop_duplicates(subset="order_id")

# 6. LOAD
# output_folder.mkdir(exist_ok=True)
# clean.to_csv(output_folder / "sales_clean.csv", index=False)

# 7. CHECK (look AFTER you fix)
# print(clean["order_id"].duplicated().sum())       
# print("combined:", len(combined), "| clean:", len(clean))





from pathlib import Path
import pandas as pd

base = Path(__file__).parent.parent
input_ff = base / "dumbledore"
out_ff = base / "ovde_folder"

f = []
for file_f in sorted(input_ff.glob("*.csv")):
    df = pd.read_csv(file_f)
    f.append(df)

print(f[0].equals(f[1]))

connect = pd.concat(f, ignore_index=True)

print(connect.isna().sum())
print(connect.dtypes)
print(connect["order_id"].duplicated().sum())

clean2 = connect.drop_duplicates(subset="order_id")

print(len(connect), len(clean2))

out_ff.mkdir(exist=True)
clean2.to_csv(out_ff/"novi_stavar", index=False)