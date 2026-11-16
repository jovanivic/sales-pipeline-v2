# pratice d7

def clean_up(v):
    if v is None or str(v).strip() == "":
        return None
    try:
        return float(str(v).replace("$", "").replace(",", ""))
    except ValueError as e:
        print(f"rejected {v!r}: {e}")
        return None

print(clean_up("$1,234.50"))
print(clean_up("N/A"))
print(clean_up(""))

for p in ["$5.00", "N/A", "abc", "1,299"]:
    print(clean_up(p))