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
    git clone <repository_url>
    cd <repository_folder_name>
    ```
    (Replace `<repository_url>` and `<repository_folder_name>` with the actual URL and folder name.)

*   **Option B: Save the Code Manually**
    If you don't want to clone, simply save the Python code provided above into a file named `grocery_billing_system.py` (or any other `.py` filename you prefer) on your local machine.

### 2. Navigate to the Project Directory

If you cloned, you should already be in the project directory. If you saved the file manually, open your terminal or command prompt and navigate to the directory where you saved `grocery_billing_system.py`.

### 3. Run the Application

Execute the Python script from your terminal:
```bash
python grocery_billing_system.py
