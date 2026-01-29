# Heart Attack Prediction Classification

A machine learning project that predicts the likelihood of a heart attack based on medical and health parameters using classification algorithms.

## Project Overview

This project leverages machine learning techniques to build a predictive model for identifying individuals at risk of heart attack. The model is trained on a comprehensive dataset containing various health indicators and demographic information, then deployed as a web application using Flask for easy accessibility and user interaction.

## Dataset

The dataset used in this project is sourced from **Kaggle**: [Heart Attack Prediction Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset/data)

### Dataset Features

- Contains multiple health indicators (age, blood pressure, cholesterol, etc.)
- Binary classification target (heart attack risk: yes/no)
- Pre-processed and cleaned data ready for analysis

## Project Workflow

### 1. Exploratory Data Analysis (EDA)

- Statistical analysis of features
- Data distribution visualization
- Correlation analysis between variables
- Identification of patterns and outliers

### 2. Data Preprocessing

- Handling missing values
- Feature scaling and normalization
- Encoding categorical variables
- Train-test data splitting

### 3. Model Selection & Training

- Evaluation of multiple classification algorithms
- Hyperparameter tuning
- Cross-validation for model robustness
- Selection of the best performing model

## Technologies & Libraries

- **Python 3.x**
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Scikit-learn** - Machine learning algorithms
- **Matplotlib & Seaborn** - Data visualization
- **Flask** - Web framework for deployment
- **Jupyter Notebook** - Interactive development environment

## Project Structure

```
heart-attack-classification/
├── Heart Attack Classification.ipynb  # Main analysis and model development
├── heart_attack_prediction_dataset.csv # Dataset file
└── README.md                           # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone or download this project
2. Install required dependencies:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn flask jupyter
```

### Usage

1. **Notebook Analysis**: Open the Jupyter notebook to explore the data, preprocessing steps, and model selection:

```bash
jupyter notebook "Heart Attack Classification.ipynb"
```

1. **Flask Deployment** (Coming soon): Deploy the trained model as a web service for real-time predictions.

## Results & Output

The notebook outputs:

- Statistical summaries and visualizations
- Model performance metrics (accuracy, precision, recall, F1-score)
- Feature importance rankings
- Best model selection for deployment

## Future Enhancements

- Flask web application for user-friendly predictions
- API endpoint for model inference
- Model explainability features (SHAP values, etc.)
- Real-time monitoring and performance tracking

## License

This project uses publicly available data from Kaggle for educational purposes.

## Teams

- Dhimas Primajaya
- Dimas Tubagus Berlian
- Dr. Elsye Maria Rosa
- Jackson
- Reynold Kunarto
- Rijki Hardiyanti
- Wadhifatur Rosyidah
- Zufar Bagas P.
