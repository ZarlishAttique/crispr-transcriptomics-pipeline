from perturbation import run_full_pipeline
from pathlib import Path



if __name__ == "__main__":
    run_full_pipeline(
        raw_deg_path=Path(r"C:\Ayass Bio Work\Agentic_AI_ABS\perturbation_pipeline\lupus_DEGs_prioritized.csv"),
        pathway_path=Path(r"C:\Ayass Bio Work\Agentic_AI_ABS\perturbation_pipeline\lupus_Pathways_Consolidated.csv"),
        # raw_deg_path=Path(r"C:\Ayass Bio Work\Agentic_AI_ABS\gene_prioritization_pipeline\OUTPUT\Lupus_DEGs_prioritized.csv"),
        # pathway_path=Path(r"C:\Ayass Bio Work\Agentic_AI_ABS\agentic_pathways_module\ALL_ANALYSIS\Lupus_Pathways_Enrichment.csv"),
        output_dir=Path("Output_Perturbation_Pipeline_Lupus_With_ACE"),
        disease="Lupus",
        max_sigs=500
    )
