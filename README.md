# House Price Prediction Using Multiple Linear Regression

This project implements a multiple linear regression model to predict house prices based on three features: area, room count, and building age. The model is trained on a dataset stored in `housepricesdataset.csv` and tested with sample data to generate price predictions.

## Project Overview

- **Objective**: Predict house prices using multiple linear regression.
- **Features**: 
  - Area (square footage)
  - Room Count (number of rooms)
  - Building Age (years since construction)
- **Target**: Price (in dollars)
- **Tools**: Python, scikit-learn, pandas, numpy, matplotlib

## Prerequisites

To run this project, you'll need the following installed:
- Python 3.x
- Required Python packages:
  ```bash
  pip install numpy pandas scikit-learn matplotlib

File Structure
housepricesdataset.csv: Training dataset containing house features and prices.
house_price_prediction.py: Main Python script with the regression model and predictions.
README.md: This file.

## How to Run

1. Clone the Repository:

git clone https://github.com/ibryam/house-price-prediction.
cd your-repo-name

2. Ensure Data Availability:

Place housepricesdataset.csv in the same directory as the script.
The CSV should have columns: area, roomcount, buildingage, price.

3. Run the Script:
python main.py

4. Output:

- Console output includes:
- Training data overview
- Model coefficients and intercept
- Predictions for test data

## Model Details

Algorithm: Multiple Linear Regression from scikit-learn
Training Data: Loaded from housepricesdataset.csv
Test Data: Three sample houses with predefined attributes:
House 1: 230 sq ft, 4 rooms, 10 years old
House 2: 230 sq ft, 6 rooms, 0 years old

## Usage

The script:

Loads and explores the training data
Trains a linear regression model
Outputs model coefficients and intercept
Makes predictions on test data
Displays results in a DataFrame
House 3: 355 sq ft, 3 rooms, 20 years old


## Results

The output includes:

Coefficients showing the impact of each feature on price
Intercept of the regression line
Predicted prices for the test houses

## Visualizations
[To be added separately]

## Contributing

Feel free to fork this repository, submit issues, or create pull requests with improvements.

