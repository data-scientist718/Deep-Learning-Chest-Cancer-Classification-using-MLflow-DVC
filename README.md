# Deep-Learning-Chest-Cancer-Classification-using-MLflow-DVC and Dagshub

## Author : ABD UR REHMAN

## Date :22-05-2024

## project structure

```
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
├── score.json
├── setup.py
├── dvc.yaml
├── README.md
```

## DagsHub Integration

### What is DagsHub?

[DagsHub](https://dagshub.com/) is a platform for data science and machine learning collaboration. It provides version control for data, experiments, models, and code, using tools like DVC (Data Version Control) and MLflow. This allows data scientists and machine learning engineers to work together seamlessly and track their progress.

### How This Project Uses DagsHub

This project leverages DagsHub for:

- **Data Versioning**: All datasets are version-controlled using DVC, allowing for reproducible experiments and easy collaboration.
- **Experiment Tracking**: Experiments are tracked using MLflow, enabling detailed tracking of model performance and parameters.
- **Model Management**: Models are versioned and managed efficiently, ensuring that the best models are easily accessible and deployable.

### Visualizations

Below are some visualizations from our DagsHub repository showing different model characteristics and performance:


## Data Version Control (DVC)

### What is DVC?

[Data Version Control (DVC)](https://dvc.org/) is an open-source tool for versioning data, managing machine learning models, and tracking experiments. DVC extends the capabilities of Git to handle large data files, machine learning models, and complex pipelines, ensuring reproducibility and collaboration.

### How This Project Uses DVC

This project uses DVC for the following purposes:

- **Data Versioning**: DVC tracks the versions of datasets used in the project, allowing you to reproduce experiments with specific data versions.
- **Pipeline Management**: DVC defines and manages the stages of the machine learning pipeline, from data ingestion to model evaluation.
- **Model Versioning**: Models are versioned using DVC, ensuring you can always retrieve and deploy a specific version of a model.
- **Experiment Tracking**: By integrating DVC with MLflow, we can track and visualize the performance metrics of different experiments.

### DVC Pipelines

The DVC pipeline for this project is defined in the `dvc.yaml` file. Below is an overview of the stages:

1. **Data Ingestion**:
    - **Command**: `python src/Chest_Cancer_Classification/pipeline/stage_01_data_ingestion.py`
    - **Dependencies**:
        - `src/Chest_Cancer_Classification/pipeline/stage_01_data_ingestion.py`
        - `config/config.yaml`
    - **Outputs**:
        - `artifacts/Chest-CT-Scan-data`

2. **Prepare Base Model**:
    - **Command**: `python src/Chest_Cancer_Classification/pipeline/stage_02_prepare_base_model.py`
    - **Dependencies**:
        - `src/Chest_Cancer_Classification/pipeline/stage_02_prepare_base_model.py`
        - `config/config.yaml`
    - **Parameters**:
        - `IMAGE_SIZE`
        - `INCLUDE_TOP`
        - `CLASSES`
        - `WEIGHTS`
        - `LEARNING_RATE`
    - **Outputs**:
        - `artifacts/prepare_base_model`

3. **Training**:
    - **Command**: `python src/Chest_Cancer_Classification/pipeline/stage_03_model_trainer.py`
    - **Dependencies**:
        - `src/Chest_Cancer_Classification/pipeline/stage_03_model_trainer.py`
        - `config/config.yaml`
        - `artifacts/Chest-CT-Scan-data`
        - `artifacts/prepare_base_model`
    - **Parameters**:
        - `IMAGE_SIZE`
        - `EPOCHS`
        - `BATCH_SIZE`
        - `AUGMENTATION`
    - **Outputs**:
        - `artifacts/training/model.h5`

4. **Evaluation**:
    - **Command**: `python src/Chest_Cancer_Classification/pipeline/stage_04_model_evaluation.py`
    - **Dependencies**:
        - `src/Chest_Cancer_Classification/pipeline/stage_04_model_evaluation.py`
        - `config/config.yaml`
        - `artifacts/Chest-CT-Scan-data`
        - `artifacts/training/model.h5`
    - **Parameters**:
        - `IMAGE_SIZE`
        - `BATCH_SIZE`
    - **Metrics**:
        - `scores.json`

### Getting Started with DVC

To set up DVC and run the pipeline:

1. **Clone the repository**:

    ```sh
    git clone https://dagshub.com/yourusername/yourprojectname.git
    cd yourprojectname
    ```

2. **Install DVC**:

    ```sh
    pip install dvc
    ```

3. **Pull the data and models**:

    ```sh
    dvc pull
    ```

4. **Run the pipeline**:

    ```sh
    dvc repro
    ```

### Additional Resources

- [DVC Documentation](https://dvc.org/doc)
- [DagsHub Documentation](https://dagshub.com/docs/)
- [MLflow Documentation](https://www.mlflow.org/docs/latest/index.html)

We hope you find DVC to be a powerful tool for managing your data science and machine learning projects.
