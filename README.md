# Banking System CLI Project

This Python program simulates a simple banking system operated via the command line. Users can view accounts, create new accounts, and edit account balances (deposit/withdraw) through interactive prompts.

---

## 📂 Project Structure

- `main.py` — Main entry point for the program; handles the CLI loop and user input.
- `other.py` — Contains helper functions for greetings, displaying help, creating/viewing/editing accounts.
- `accounts.py` — Manages the storage of account data and handles account number generation.

---

## 🚀 Features

### Greeting
- On startup, users are welcomed with a custom greeting.

### Command Navigation
- Type `help` to view available commands:
  - `view_accounts` — View all existing bank accounts.
  - `create_account` — Create a new bank account with a unique account number.
  - `exit` — Exit the program.

### Account Management
- **View Accounts**: Lists all stored accounts with their names, account numbers, and balances.
- **Create Accounts**:
  - Enter a first name and an initial deposit amount.
  - System automatically generates a unique 4-digit account number.
- **Edit Accounts**:
  - After viewing accounts, select an account by its number.
  - Choose to `withdraw` or `deposit` funds.
  - Balance updates are reflected immediately.

### Error Handling
- Handles unrecognized commands with a friendly error message.
- Prevents overdrawing an account during withdrawal operations.

---



