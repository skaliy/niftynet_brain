NiftyNet_Brain
==============================
Project:  Description
------------

Project Organization
------------

    ├── config                             <- Configuration files for different tasks. 
    │   └── brats
    │       └── brats.ini
    │    
    ├── models                  
    │   └── brats
    │       ├── logs  
    │       ├── models                      <- Trained models 
    │       ├── __init__.py  
    │       ├── dataset_split.csv
    │       ├── evaluation_niftynet_log
    │       ├── inference_niftynet_log  
    │       ├── label_mapping_whole_tumor.txt
    │       ├── settings_evaluation.txt
    │       ├── settings_inference.txt
    │       ├── settings_training.txt  
    │       └── training_niftynet_log
    │
    ├── nbs                                 <- Jupyter notebooks. 
    │   └── brats 
    │       ├── prepare.ipynb 
    │       └── utils.py
    │
    ├── NiftyNet                            <-  TODO .gitmodules 
    │
    ├── outputs <-  Segmentation result.
    │       ├── evaluation
    │       │    ├── eval_label.csv
    │       │    └── eval_subject_id_label.csv 
    │       │
    │       └── inference
    │
    └── README.md                           <-The top-level README for developers using this project.
--------
## Notebooks
`prepare.ipynb`: description
## Python classes 
`utils.py`: description 