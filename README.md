NiftyNet_Brain
==============================
Project:  Description
------------

Project Organization
-----------
    ├── config                              <- Configuration files for different tasks. 
    │   ├── brats
    │   │   └── brats.ini
    │   └── ixi
    │       └── ixi.ini
    ├── nbs                                 <- Jupyter notebooks. 
    │   ├── brats 
    │   │   ├── dataset_split.ipynb
    │   │   └── prepare.ipynb
    │   └── ixi   
    │        ├── create_patient_folders.ipynb
    │        └── prepare.ipynb
    │
    ├── NiftyNet                            <- .gitmodules 
    └── README.md                           <-The top-level README for developers using this project.
--------
## Notebooks
`prepare.ipynb`: create csv files with pathname for the images 
`dataset_split.ipynb`: modify niftynets `dataset_split.csv`. 
`create_patient_folders.ipynb`:create folders for each study and rename the files. 

