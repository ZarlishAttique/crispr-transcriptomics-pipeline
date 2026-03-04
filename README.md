# perturbation_pipeline

A comprehensive pipeline for perturbation analysis integrating DepMap and L1000 data.

## Setup Instructions

### 1. Prerequisites

- Python 3.13 or higher
- `uv` package manager (recommended) or `pip`

### 2. Install Dependencies

Using `uv` (recommended):
```bash
uv sync
```

Or using `pip`:
```bash
pip install -r requirements.txt
```

### 3. Data Directory Setup

The pipeline requires three sets of data files: DepMap data, L1000 data, and Integration data. These are not included in the repository due to their size.

#### 3.1 DepMap Data Setup

1. **Create the DepMap data directory:**
   ```bash
   mkdir -p perturbation/dep_map/data
   ```

#### 3.3 Integration Data Setup

1. **Ensure the Integration data directory exists:**
   ```bash
   mkdir -p perturbation/integration/data
   ```

2. **Download Integration data files from Google Drive:**
   - Navigate to: https://drive.google.com/file/d/1zMbCQklZJTMQa5IF2FZWbMjk-vZyFI6c/view?usp=drive_link
   - Download the file(s) from the folder
   - Place them directly in `perturbation/integration/data/`

3. **Required Integration files:**
   The following file must be present in `perturbation/integration/data/`:
   - `Drugability_Toxicity.csv` - Contains drug druggability and toxicity information used for scoring

   **Note:** The `HGNC_GenesSymbols.csv` file should already exist in `perturbation/integration/data/`. If it's missing, ensure it's present as it's required for gene symbol normalization.

### 4. Verify Setup

After downloading, verify that all required files are present:

**For DepMap:**
```bash
# On Windows PowerShell
Get-ChildItem perturbation\dep_map\data\*.csv | Measure-Object | Select-Object Count

# On Linux/Mac
ls perturbation/dep_map/data/*.csv | wc -l
```

**For L1000:**
```bash
# On Windows PowerShell
Get-ChildItem perturbation\l1000\data\ | Select-Object Name

# On Linux/Mac
ls -lh perturbation/l1000/data/
```

**For Integration:**
```bash
# On Windows PowerShell
Get-ChildItem perturbation\integration\data\ | Select-Object Name

# On Linux/Mac
ls -lh perturbation/integration/data/
```

Ensure you see all the required files listed above.

### 5. Prepare Input Files

Before running the pipeline, you need to prepare your input files:

1. **DEGs (Differentially Expressed Genes) file:**
   - Must be a CSV, TSV, or Excel file
   - Required columns: `Gene`, `HGNC_Synonyms`, `Patient_LFC_Trend`
   - Should contain a `Log2FC` column (or a column ending with `log2fc`)

2. **Pathways file:**
   - Must be a CSV, TSV, or Excel file
   - Required columns: `Pathway ID`, `number_of_genes`, `number_of_genes_in_background`, `Pathway associated genes`, `p_value`, `fdr`, `Pathway`, `Regulation`, `Main_Class`, `Sub_Class`

### 6. Run the Pipeline

Edit `main.py` to point to your input files:

```python
from perturbation import run_full_pipeline
from pathlib import Path

if __name__ == "__main__":
    run_full_pipeline(
        raw_deg_path=Path("path/to/your/degs.csv"),
        pathway_path=Path("path/to/your/pathways.csv"),
        output_dir=Path("Output_Perturbation_Pipeline"),
        disease="YourDiseaseName",
    )
```

Then run:
```bash
python main.py
```

### 7. Pipeline Output

The pipeline will create an output directory with three subdirectories:
- `depmap/` - DepMap analysis results
- `l1000/` - L1000 analysis results
- `integration/` - Integrated analysis results

## Troubleshooting

### Missing Data Files
If you encounter errors about missing files:
1. Verify all files are downloaded completely
2. Check file names match exactly (case-sensitive)
3. Ensure files are in the correct directories

### Large File Downloads
The L1000 `.gctx` file is very large (~2GB). If download fails:
- Use Google Drive's download manager
- Ensure sufficient disk space
- Check your internet connection stability

### Python Version Issues
This pipeline requires Python 3.13+. If you have an older version:
- Update Python or use a virtual environment with Python 3.13+
- Consider using `pyenv` or `conda` to manage Python versions
