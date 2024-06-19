# Deep-Learning-Chest-Cancer-Classification-using-MLflow-DVC and Dagshub

# Author : ABD UR REHMAN

# Date :22-05-2024

## project structure

'''
├── artifacts/
│ ├── Chest-CT-Scan-data
│ ├── data_ingestion
│ ├── prepare_base_model
│ ├── training
├── config/
│ ├── config.yaml
├── research/
│ ├── 01_data_ingestion.ipynb
│ ├── 02_prepare_base_model.ipynb
│ ├── 03_model_trainer.ipynb
│ ├── 04_model_evaluation_with_mlflow.ipynb
├── src/Chest_Cancer_Classification/
│ ├── components/
│ │ ├── data_ingestion.py
│ │ ├── prepare_base_model.py
│ │ ├── model_trainer.py
│ │ ├── model_evaluation.py
│ ├── config/
│ │ ├── configuration.py
│ ├── entity/
│ │ ├── config_entity.py
│ ├── constants/
│ │ ├── init.py
│ ├── pipeline/
│ │ ├── stage_01_data_ingestion.py
│ │ ├── stage_02_prepare_base_model.py
│ │ ├── stage_03_model_trainer.py
│ │ ├── stage_04_model_evaluation.py
│ ├── utils/
│ │ ├── common.py
├── main.py
├── params.yaml
├── templates
├── app.py
├── requirements.txt
├── setup.py
├── dvc.yaml
├── README.md
'''
