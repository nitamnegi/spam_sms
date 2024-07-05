# Spam SMS Detection

This repository contains a project for detecting spam emails using machine learning techniques. The project includes data preprocessing, feature extraction, and model training.

## Project Structure

- **templates/**: HTML templates for the web application
- **app.py**: Flask web application script
- **feature_extraction.pkl**: Pickle file for feature extraction
- **model.pkl**: Trained machine learning model
- **spam-sms-prediction.ipynb**: Jupyter notebook for model development
- **spam.csv**: Dataset used for training and testing

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Pandas
- Scikit-learn
- Jupyter Notebook

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/nitamnegi/spam_sms.git
    cd spam_sms
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Use the web interface to upload email text for spam detection.

### Model Training

To retrain the model, run the Jupyter notebook `spam-sms-prediction.ipynb` which contains the steps for data preprocessing, feature extraction, and model training.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request.
