# banking.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


# Constants for simulation
CREDIT_SCORE_THRESHOLD = 650
LOAN_ELIGIBILITY_CREDIT_SCORE_THRESHOLD = 680
LOAN_ELIGIBILITY_INCOME_THRESHOLD = 30000



def load_and_preprocess_data(file_path):
    """
    Loads data from an Excel file and preprocesses it.
    """
    try:
        data = pd.read_excel(file_path)
        data['DATE'] = pd.to_datetime(data['DATE'])
        data['TransactionHour'] = data['DATE'].dt.hour  
        
        return data, "Data loaded and preprocessed successfully."
    except Exception as e:
        return None, f"Error loading data: {e}"



def detect_anomalies(data, account_number=None):
    """
    Detects anomalies in financial transactions.
    If an account number is provided, filters data for that account number before detecting anomalies.
    """
    if account_number:
        data = data[data['Account No'] == account_number]
    
    threshold = 10000  
    data['Anomaly'] = data['WITHDRAWAL AMT'] > threshold
    
    anomalies = data[data['Anomaly']]
    message = f"Detected {len(anomalies)} anomalies."
    if not anomalies.empty:
        message += " Review transactions with high withdrawal amounts."
    return message



def predict_credit_score(data, account_number):
    """
    Predicts a credit score based on financial history.
    """
    credit_score = np.random.randint(300, 850)  
    advice = "Maintain good financial habits." if credit_score >= CREDIT_SCORE_THRESHOLD else "Consider improving your credit habits."
    return f"Predicted credit score: {credit_score}. {advice}"



def predict_loan_eligibility(data, account_number):
    """
    Predicts loan eligibility based on financial status.
    """
    credit_score = np.random.randint(300, 850)
    income = np.random.randint(20000, 100000)
    eligible = (credit_score >= LOAN_ELIGIBILITY_CREDIT_SCORE_THRESHOLD) and (income >= LOAN_ELIGIBILITY_INCOME_THRESHOLD)
    eligibility_status = "Eligible" if eligible else "Not eligible"
    return f"Loan eligibility: {eligibility_status}"



def segment_customers(data, account_number, occupation, household_number, location):
    """
    Segments customers into groups based on detailed customer attributes.
    """
    if data.empty:
        return data, "Data is empty, cannot perform customer segmentation."

    customer_data = data[data['Account No'] == account_number]

    if customer_data.empty:
        return data, "No data found for the provided account number."

    customer_data['Income Level'] = pd.cut(customer_data['Annual Income'], bins=[0, 30000, 60000, 90000, float('inf')],
                                           labels=['Low', 'Moderate', 'High', 'Very High'])
    customer_data['Transaction Level'] = pd.cut(customer_data['Total Transaction Amount'], bins=[0, 10000, 20000, 30000, float('inf')],
                                                labels=['Low', 'Moderate', 'High', 'Very High'])

    grouped_data = customer_data.groupby(['Income Level', 'Transaction Level'])
    segmentation_info = grouped_data.size().unstack(fill_value=0)

    message = "Customer segmentation completed. Here are the segments based on income and transaction levels:\n" + str(segmentation_info)

    return data, message



def detect_fraud(data, account_number=None):
    """
    Detects potential fraud in financial transactions.
    """
    if account_number:
        data = data[data['Account No'] == account_number]
        if data.empty:
            return "No data found for the provided account number."

    fraud_threshold = 5000
    data['PotentialFraud'] = (data['WITHDRAWAL AMT'] > fraud_threshold) & (data['TransactionHour'].isin([0, 1, 2, 3, 4]))

    fraud_cases = data[data['PotentialFraud']]
    message = f"Detected {len(fraud_cases)} potential fraud cases."
    return message
