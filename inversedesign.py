import pandas as pd
import numpy as np

np.random.seed(42)

# 100 Polymer Samples
samples = [
"PEO_LiTFSI","PEO_LiPF6","PEO_LiClO4","PEO_LiBF4","PEO_LiAsF6",
"PAN_LiTFSI","PAN_LiPF6","PAN_LiClO4","PAN_LiBF4","PAN_LiAsF6",
"PMMA_LiTFSI","PMMA_LiPF6","PMMA_LiClO4","PMMA_LiBF4","PMMA_LiAsF6",
"PVDF_LiTFSI","PVDF_LiPF6","PVDF_LiClO4","PVDF_LiBF4","PVDF_LiAsF6",
"PVP_LiTFSI","PVP_LiPF6","PVP_LiClO4","PVP_LiBF4","PVP_LiAsF6",

"PEO_PVDF_LiTFSI","PEO_PVDF_LiPF6","PEO_PMMA_LiClO4","PEO_PAN_LiBF4","PEO_PVP_LiTFSI",
"PAN_PMMA_LiClO4","PAN_PVDF_LiPF6","PMMA_PVDF_LiTFSI","PMMA_PVP_LiBF4","PVDF_PVP_LiClO4",
"PEO_PAN_LiTFSI","PEO_PMMA_LiPF6","PAN_PVP_LiBF4","PVDF_PMMA_LiClO4","PEO_PVDF_LiBF4",

"PEO_LiTFSI_EC","PEO_LiTFSI_PC","PEO_LiPF6_EC","PEO_LiPF6_PC","PEO_LiClO4_EC",
"PAN_LiClO4_PC","PAN_LiPF6_EC","PMMA_LiClO4_PC","PMMA_LiPF6_EC","PVDF_LiTFSI_EC",
"PVDF_LiPF6_PC","PVP_LiClO4_EC","PVP_LiPF6_PC","PAN_LiTFSI_PC","PMMA_LiTFSI_EC",

"PEO_Gel_LiTFSI","PEO_Gel_LiPF6","PEO_Gel_LiClO4","PAN_Gel_LiTFSI","PAN_Gel_LiPF6",
"PMMA_Gel_LiClO4","PMMA_Gel_LiTFSI","PVDF_Gel_LiPF6","PVDF_Gel_LiClO4","PVP_Gel_LiTFSI",
"PEO_Gel_LiBF4","PAN_Gel_LiBF4","PMMA_Gel_LiBF4","PVDF_Gel_LiBF4","PVP_Gel_LiBF4",

"PEO_LiTFSI_Al2O3","PEO_LiPF6_SiO2","PEO_LiClO4_TiO2","PAN_LiTFSI_ZnO","PAN_LiPF6_Al2O3",
"PMMA_LiClO4_SiO2","PMMA_LiTFSI_TiO2","PVDF_LiPF6_ZnO","PVDF_LiClO4_Al2O3","PVP_LiTFSI_SiO2",
"PEO_LiBF4_TiO2","PAN_LiBF4_ZnO","PMMA_LiBF4_Al2O3","PVDF_LiBF4_SiO2","PVP_LiBF4_TiO2",

"Crosslinked_PEO_LiTFSI","Crosslinked_PEO_LiPF6","BlockCopolymer_PEO_LiClO4",
"StarPolymer_PEO_LiBF4","Hyperbranched_PEO_LiTFSI",
"IonicLiquid_PEO_LiTFSI","IonicLiquid_PAN_LiPF6","IonicLiquid_PMMA_LiClO4",
"IonicLiquid_PVDF_LiTFSI","IonicLiquid_PVP_LiPF6",
"CeramicHybrid_PEO_LiTFSI","CeramicHybrid_PAN_LiPF6","CeramicHybrid_PMMA_LiClO4",
"CeramicHybrid_PVDF_LiBF4","CeramicHybrid_PVP_LiTFSI"
]

df = pd.DataFrame({"Sample": samples})

# 12 Features
df["Molecular_Weight"] = np.random.uniform(10000,100000,len(df))
df["Ion_Size"] = np.random.uniform(0.1,1.0,len(df))
df["Decomposition_Temperature"] = np.random.uniform(300,800,len(df))
df["Ion_Transference_Number"] = np.random.uniform(0.1,1.0,len(df))
df["Humidity"] = np.random.uniform(10,90,len(df))
df["Degree_of_Polymerization"] = np.random.uniform(50,500,len(df))
df["Anion_Radius"] = np.random.uniform(1.0,3.0,len(df))
df["Phase_Transition_Temp"] = np.random.uniform(200,500,len(df))
df["Band_Gap"] = np.random.uniform(1.0,6.0,len(df))
df["Expansion_Coefficient"] = np.random.uniform(1e-6,1e-4,len(df))
df["Crosslink_Density"] = np.random.uniform(0,1,len(df))
df["Processing_Time"] = np.random.uniform(1,24,len(df))

# Add missing values
for col in df.columns[1:]:
    df.loc[df.sample(frac=0.1).index, col] = np.nan

# Cleaning
df.fillna(df.mean(numeric_only=True), inplace=True)

# Save as CSV (NO ERROR VERSION)
df.to_csv("Sai_Final_Dataset.csv", index=False)

print("🔥 Dataset created successfully!")
