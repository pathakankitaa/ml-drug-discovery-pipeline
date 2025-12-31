# ML-Guided Drug Discovery Pipeline

## Overview
This repository demonstrates a practical, chemistry-first machine learning workflow
for prioritizing small-molecule drug candidates beyond docking scores alone.

The goal is not to build a black-box AI, but to combine docking outputs,
physicochemical descriptors, and simple ML models to support medicinal chemistry decisions.

## Problem Statement
Docking-based virtual screening often produces many false positives.
High-scoring compounds may be chemically unrealistic or experimentally inactive.

This pipeline uses ML to:
- Integrate docking scores with chemical features
- Improve hit prioritization
- Reduce unnecessary synthesis and testing

## Features Used
- Docking score (e.g., Glide XP)
- MM-GBSA binding energy
- Molecular weight
- TPSA
- Rotatable bonds
- H-bond donors / acceptors

Descriptors are generated using RDKit and combined with docking outputs.

## Model
A Random Forest classifier is used because:
- Early drug discovery datasets are small
- Feature importance is interpretable
- Performance is robust to noisy docking scores

## Evaluation
- 5-fold cross-validation
- Metrics: ROC-AUC and enrichment over random
- ML ranking compared against docking-only ranking

## Key Outcome
The ML model improves enrichment of true actives in top-ranked compounds,
allowing reduction of synthesis candidates compared to docking alone.

## Limitations
- Model performance depends on docking quality
- Small datasets limit generalization
- Intended for early prioritization, not final decision-making

## Practical Relevance
This workflow reflects real-world AI-assisted drug discovery,
where models support chemist decisions rather than replace them.
