# chatbot.py

import banking
import random

def get_initial_message():
    """
    Introduces the chatbot and asks what the user is here for, listing available commands.
    """
    introduction = (
        "Hello! I am your Banking Assistance and Consultant.\n"
        "I'm here to help you manage your banking needs effectively.\n"
        "Please upload your Excel file to get started.\n"
        "Once uploaded, you can select from the following commands:\n"
    )
    commands_list = [
        "1. Detect Anomalies for All Customers",
        "2. Detect Anomalies for a Customer",
        "3. Predict Credit Score",
        "4. Check Loan Eligibility",
        "5. Segment Customers",
        "6. Detect Fraud for All Customers",
        "7. Detect Fraud for a Customer"
    ]
    commands_display = "\n".join(commands_list)
    return introduction + commands_display + "\n\nWhat would you like to do today? Enter the number of your choice:"

def respond_to_command(command_text, data, credit_card_number=None, occupation=None, household_number=None, location=None):
    """
    Responds to a user's command, processes data accordingly, and optionally provides banking tips.
    """
    if data is None or data.empty:
        return "No data loaded. Please upload an Excel file."

    try:
        tips = {
            "detect_anomalies_for_all": "Regularly review your transaction patterns to easily spot anomalies.",
            "predict_credit_score": "Maintaining a good credit score is crucial for obtaining favorable loan terms.",
            "check_loan_eligibility": "Ensure your income details are up-to-date to maximize loan eligibility.",
            "segment_customers": "Understanding customer segments can help tailor your services effectively.",
            "detect_fraud_for_all": "Always monitor for unusual withdrawal times, especially late at night."
        }
        message = ""
        if command_text == "detect_anomalies_for_all":
            message = banking.detect_anomalies(data)

        elif command_text == "detect_anomalies_for_customer":
            message = banking.detect_anomalies(data, credit_card_number) if credit_card_number else "No account number provided."

        elif command_text == "predict_credit_score":
            message = banking.predict_credit_score(data, credit_card_number) if credit_card_number else "No account number provided."

        elif command_text == "check_loan_eligibility":
            message = banking.predict_loan_eligibility(data, credit_card_number) if credit_card_number else "No account number provided."

        elif command_text == "segment_customers":
            if all([credit_card_number, occupation, household_number, location]):
                _, message = banking.segment_customers(data, credit_card_number, occupation, household_number, location)
            else:
                message = "Complete information is required for segmenting customers."

        elif command_text == "detect_fraud_for_all":
            message = banking.detect_fraud(data)

        elif command_text == "detect_fraud_for_customer":
            message = banking.detect_fraud(data, credit_card_number) if credit_card_number else "No account number provided."

        else:
            message = "Unknown command. Please try again."

        
        if command_text in tips:
            message += "\nTip: " + tips[command_text]

        return message

    except Exception as e:
        return f"An error occurred: {str(e)}"

    return message
