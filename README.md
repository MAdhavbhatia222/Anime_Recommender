# Anime Recommender System

## Overview
This project demonstrates the creation of an Anime Recommender System, encompassing the entire workflow from data warehousing to model deployment.

## Data Source
Kaggle : [Anime Database](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database)

## Project Workflow
- **Data Warehousing**: CSV data was migrated to Oracle Autonomous Data Warehouse using Talend.
- **Data Exploration**: Python notebooks were used for exploring the data by connecting to the data warehouse.
- **Model Building**: Python scripts were developed for the machine learning model.
- **Containerization**: Docker was utilized for containerizing the application and its environment.
- **Deployment**: The model was deployed on an Oracle Compute Instance.

![image](https://github.com/MAdhavbhatia222/Anime_Recommender/assets/32282603/9418fc9b-9df0-407a-980b-44dd7209efa9)



https://github.com/MAdhavbhatia222/Anime_Recommender/assets/32282603/e25aeb2e-a8ac-4301-bdeb-23a87bd7f8fa



## Model Deployment
- The recommender system is live at [SuggestAnime](https://www.suggestanime.com).

## Repository Contents
- `indices.pkl`: Serialized indices file for recommendation.
- `Pipfile` & `Pipfile.lock`: Environment and dependency management files.
- `Predict.py`: Script for model prediction.
- `Predict_Test.py`: Script for testing predictions.
- `Training.py`: Model training script.
- `Dockerfile`: Docker build instructions.

## Getting Started
1. Clone the repository.
2. Install dependencies (`pipenv install`).
3. Train the model (`Training.py`).
4. Build the Docker container (`Dockerfile`).
5. Deploy on Oracle Compute Instance.

## Technologies Used
- Python
- Oracle Autonomous Data Warehouse
- Talend
- Docker

## Author
- Madhav Bhatia

## License
- MIT License
