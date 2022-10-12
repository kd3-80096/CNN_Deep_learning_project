## Deep classifier project



## workflow

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config.
6. Update the components
7. Update the pipeline
8. Test run pipeline stage
9. run tox for testing your package
10. Update the dvc.yaml        ##construct pipelines by defining individual stages in one or more dvc. yaml files
11. run "dvc repro" for running all the stages in pipeline


![img](https://raw.githubusercontent.com/deveshpatil619/CNN_Deep_learning_project/main/docs/Data%20Ingestion%402x%20(1).png)



STEP 1: Set the env variable | Get it from dagshub -> remote tab -> mlflow tab

MLFLOW_TRACKING_URI=https://dagshub.com/deveshpatil619/CNN_Deep_learning_project.mlflow \
MLFLOW_TRACKING_USERNAME=deveshpatil619 \
MLFLOW_TRACKING_PASSWORD=bfb47fe0fe79d1f887537f03b89660425bad64fb \


STEP 2: install mlflow

STEP 3: Set remote URI

STEP 4: Use context manager of mlflow to start run and then log metrics, params and model


## Sample-Data for testing URl-Link

https://raw.githubusercontent.com/c17hawke/raw_data/main/sample_data.zip





