import pandas as pd

print("Loading dataset...")
df = pd.read_csv("NSE_full_with_sector_and_cap.csv")

# Clean columns (just in case)
df["sector"] = df["sector"].fillna("UNKNOWN").astype(str)
df["cap_category"] = df["cap_category"].fillna("UNKNOWN").astype(str)

# ============================================
# 1️⃣ COUNT COMPANIES PER SECTOR
# ============================================
sector_counts = df["sector"].value_counts().reset_index()
sector_counts.columns = ["sector", "company_count"]

print("\n🔹 Companies per Sector:")
print(sector_counts)

sector_counts.to_csv("sector_summary.csv", index=False)
print("\n✔ Saved → sector_summary.csv")


# ============================================
# 2️⃣ COUNT COMPANIES PER MARKET CAP CATEGORY
# ============================================
cap_counts = df["cap_category"].value_counts().reset_index()
cap_counts.columns = ["cap_category", "company_count"]

print("\n🔹 Companies per Market Cap:")
print(cap_counts)

cap_counts.to_csv("marketcap_summary.csv", index=False)
print("\n✔ Saved → marketcap_summary.csv")


# ============================================
# 3️⃣ OPTIONAL — Combined Summary
# ============================================
combined = df.groupby(["sector", "cap_category"]).size().reset_index(name="count")
combined.to_csv("sector_cap_combined.csv", index=False)

print("\n🔹 Combined Sector × Market Cap Summary:")
print(combined.head())

print("\n✔ Saved → sector_cap_combined.csv")
