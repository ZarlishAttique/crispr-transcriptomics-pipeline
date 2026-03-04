# Setup Checklist

Use this checklist to ensure your pipeline is properly configured before running.

## Prerequisites
- [ ] Python 3.13+ installed
- [ ] Dependencies installed (`uv sync` or `pip install`)

## DepMap Data Setup
- [ ] Created directory: `perturbation/dep_map/data/`
- [ ] Downloaded all CSV files from: https://drive.google.com/drive/folders/1Ud_p6mswJQGuLnqNX-kzTaP9_coqhXAR
- [ ] Verified required files are present:
  - [ ] `Model.csv`
  - [ ] `Gene.csv`
  - [ ] `CRISPRGeneEffect.csv`
  - [ ] `CRISPRGeneDependency.csv`
  - [ ] `OmicsExpressionTPMLogp1HumanProteinCodingGenes.csv`
  - [ ] `OmicsCNGeneWGS.csv`
  - [ ] `ModelCondition.csv`
  - [ ] `CRISPRScreenMap.csv`
  - [ ] `ScreenSequenceMap.csv`
  - [ ] `AvanaGuideMap.csv`
  - [ ] `AvanaLogfoldChange.csv`
  - [ ] `CellLines_Master_AllModels.csv`

## L1000 Data Setup
- [ ] Created directory: `perturbation/l1000/data/`
- [ ] Downloaded all files from: https://drive.google.com/drive/folders/173ItTYxSH6GjVNRNJwy8fvQz3iRJ0RZR
- [ ] Verified required files are present:
  - [ ] `Metadata.csv`
  - [ ] `GSE92742_Broad_LINCS_sig_info.txt`
  - [ ] `GSE92742_Broad_LINCS_pert_info.txt`
  - [ ] `GSE92742_Broad_LINCS_cell_info.txt`
  - [ ] `GSE92742_Broad_LINCS_gene_info.txt`
  - [ ] `GSE92742_Broad_LINCS_Level5_COMPZ.MODZ_n473647x12328.gctx` (large file!)

## Integration Data Setup
- [ ] Created directory: `perturbation/integration/data/`
- [ ] Downloaded file from: https://drive.google.com/file/d/1zMbCQklZJTMQa5IF2FZWbMjk-vZyFI6c/view?usp=drive_link
- [ ] Verified required files are present:
  - [ ] `Drugability_Toxicity.csv`
  - [ ] `HGNC_GenesSymbols.csv` (should already exist)

## Input Files Preparation
- [ ] DEGs file prepared with required columns:
  - [ ] `Gene`
  - [ ] `HGNC_Synonyms`
  - [ ] `Patient_LFC_Trend`
  - [ ] `Log2FC` (or similar column)
- [ ] Pathways file prepared with required columns:
  - [ ] `Pathway ID`
  - [ ] `number_of_genes`
  - [ ] `number_of_genes_in_background`
  - [ ] `Pathway associated genes`
  - [ ] `p_value`
  - [ ] `fdr`
  - [ ] `Pathway`
  - [ ] `Regulation`
  - [ ] `Main_Class`
  - [ ] `Sub_Class`

## Configuration
- [ ] Updated `main.py` with correct paths to your DEGs and Pathways files
- [ ] Set appropriate disease name in `main.py`
- [ ] Configured output directory path

## Ready to Run
- [ ] All data files verified
- [ ] Input files prepared
- [ ] Configuration updated
- [ ] Run: `python main.py`
