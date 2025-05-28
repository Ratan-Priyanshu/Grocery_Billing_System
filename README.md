# 🛒 Grocery Billing System

A simple command-line application written in Python to generate grocery bills with conditional discounts. This project demonstrates basic Python concepts including functions, loops, conditionals, dictionaries, and lists. It focuses on a single transaction at a time and does not use external file storage for simplicity.

## 🌟 Features

*   **Add Items:** Add grocery items to the current bill, specifying name, price per unit, and quantity.
*   **View Current Bill:** Display a list of items currently added to the bill along with their details and the running subtotal.
*   **Calculate Total Bill:** Compute the subtotal of all items.
*   **Apply Conditional Discounts:** Automatically apply discounts based on the subtotal amount:
    *   5% off for subtotals $50 or more.
    *   10% off for subtotals $100 or more.
    *   15% off for subtotals $200 or more.
*   **Print Formatted Receipt:** Generate and display a well-formatted receipt including all items, subtotal, discount applied, and the final total due.
*   **Start New Bill:** Clear the current bill to start a new transaction.

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed on your system:

*   **Python:** Version 3.6 or higher. (The script uses f-strings which are standard in these versions). You can download Python from [python.org](https://www.python.org/downloads/).
*   **Git:** (Optional, but recommended for cloning if this were hosted on a version control platform). You can download Git from [git-scm.com](https://git-scm.com/downloads).

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### 1. Obtain the Code

*   **Option A: Clone the Repository (If Hosted)**
    If this project is hosted on a platform like GitHub, open your terminal or command prompt and run:
    ```bash
    git clone https://github.com/Ratan-Priyanshu/Grocery_Billing_System.git
    cd Grocery_Billing_System
    ```
*   **Option B: Save the Code Manually**
    If you don't want to clone, simply save the Python code provided above into a file named `grocery_billing_system.py` (or any other `.py` filename you prefer) on your local machine.

### 2. Navigate to the Project Directory

If you cloned, you should already be in the project directory. If you saved the file manually, open your terminal or command prompt and navigate to the directory where you saved `grocery_billing_system.py`.

### 3. Run the Application

Execute the Python script from your terminal:
```bash
python grocery_billing_system.py
```
The application will start, and you will see a menu with options to manage the grocery bill.

### 💻 How to Use

Once the application is running, you will be presented with a menu:
```bash
========================================
        GROCERY BILLING SYSTEM
========================================
1. Add Item to Bill
2. View Current Bill Items
3. Finalize and Print Bill
4. Start New Bill
5. Exit
----------------------------------------
Enter your choice (1-5):
```

Enter the number corresponding to the action you wish to perform and follow the on-screen prompts.
    When adding items, you'll be asked for the item name, price per unit, and quantity.
    The system assumes valid numeric input for price and quantity.

### 💾 Data Storage

Each run of the script starts a fresh billing session. Once an item is added, it remains in the current_bill list until the bill is finalized or a new bill is started.

### 🏗️ Project Structure

If you only have the script, your structure will be:
```bash
your_project_directory/
└── grocery_billing_system.py   # The main Python script
```

### 💡 Potential Future Enhancements: 

   -Robust Input Validation: Implement try-except blocks or more detailed string checks to handle non-numeric or invalid inputs gracefully without crashing.
    -Product Catalog:
    -Store a predefined list of grocery items and their prices (perhaps in a dictionary or a JSON file).
    -Allow users to select items from the catalog or add by item code.
    -Modify/Remove Items from Bill: Add functionality to edit the quantity of an item already in the bill or remove an item entirely.
    -Tax Calculation: Incorporate sales tax calculation.
    -Payment Types: Simulate different payment methods.
    -Save/Load Bills: Implement functionality to save completed bills to a file (e.g., JSON or text) and load them for review.
    -User Accounts/Loyalty Program: For a more advanced system, add user accounts and loyalty-based discounts.
    -Graphical User Interface (GUI): Develop a GUI using libraries like Tkinter, PyQt, or Kivy for a more interactive experience.
    -Unit Tests: Write tests to ensure the reliability of calculations and other functions.

### 🤝 Contributing : 

This is a simple project designed for learning and demonstration. 
For personal use, feel free to modify and extend it as you see fit!
