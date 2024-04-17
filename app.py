# app.py

import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, scrolledtext
import pandas as pd
import threading
import banking
import chatbot

class BankingApp:
    def __init__(self, root):
        self.root = root
        self.data = pd.DataFrame()
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Banking Assistance Application")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Styling fonts
        title_font = ("Arial", 16, "bold")
        label_font = ("Arial", 12)
        button_font = ("Arial", 10, "bold")

        
        self.output_text = scrolledtext.ScrolledText(self.root, state='disabled', height=20, font=("Arial", 10))
        self.output_text.pack(pady=10, fill=tk.BOTH, expand=True)

        self.display_initial_message()

        # Buttons and labels with styling
        tk.Button(self.root, text="Upload Data", command=self.upload_data_async, font=button_font, bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=5)
        tk.Label(self.root, text="Enter Command Number:", bg="#f0f0f0", font=label_font).pack(pady=(5,0))
        
        self.command_entry = tk.Entry(self.root, font=("Arial", 12))
        self.command_entry.pack(pady=(0,5))
        
        tk.Button(self.root, text="Execute Command", command=self.execute_command_async, font=button_font, bg="#2196F3", fg="white", padx=10, pady=5).pack(pady=5)
        tk.Button(self.root, text="Close Application", command=self.root.destroy, font=button_font, bg="#f44336", fg="white", padx=10, pady=5).pack(pady=(5,0))

    def display_initial_message(self):
        initial_message = chatbot.get_initial_message()
        self.display_output(initial_message)

    def upload_data_async(self):
        threading.Thread(target=self.upload_data, daemon=True).start()

    def upload_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if file_path:
            self.data, message = banking.load_and_preprocess_data(file_path)
            self.display_output(message)

    def execute_command_async(self):
        self.root.after(0, self.execute_command)

    def execute_command(self):
        command_index = int(self.command_entry.get()) - 1
        self.command_entry.delete(0, tk.END)
        if self.data.empty:
            self.display_output("Please upload data before executing commands.")
            return

        command_texts = [
            "detect_anomalies_for_all",
            "detect_anomalies_for_customer",
            "predict_credit_score",
            "check_loan_eligibility",
            "segment_customers",
            "detect_fraud_for_all",
            "detect_fraud_for_customer"
        ]

        if 0 <= command_index < len(command_texts):
            command_action = command_texts[command_index]
            response = chatbot.respond_to_command(command_action, self.data)
            self.display_output(response)
            self.ask_for_continuation()
        else:
            self.display_output("Invalid command number.")

    def ask_for_continuation(self):
        continue_choice = simpledialog.askinteger("Continue?", "Enter 1 to perform another action, or 2 to exit.")
        if continue_choice == 1:
            self.display_initial_message()
        elif continue_choice == 2:
            self.root.destroy()

    def display_output(self, message):
        self.output_text.config(state='normal')
        self.output_text.insert(tk.END, message + "\n\n")
        self.output_text.config(state='disabled')
        self.output_text.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()
