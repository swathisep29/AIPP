// BankAccount class simulates basic banking operations.
// Fix: Added private property declaration for _balance

class BankAccount {
    private _balance: number; // Added property declaration

    constructor(initialBalance: number = 0) {
        // Initializes the account with an initial balance (default is 0)
        this._balance = initialBalance;
    }

    deposit(amount: number): void {
        if (amount <= 0) {
            console.log("Deposit amount must be positive.");
            return;
        }
        this._balance += amount;
        console.log(`Deposited: $${amount}. New balance: $${this._balance}`);
    }

    withdraw(amount: number): void {
        if (amount <= 0) {
            console.log("Withdrawal amount must be positive.");
            return;
        }
        if (amount > this._balance) {
            console.log("Insufficient funds.");
            return;
        }
        this._balance -= amount;
        console.log(`Withdrew: $${amount}. New balance: $${this._balance}`);
    }

    getBalance(): number {
        console.log(`Current balance: $${this._balance}`);
        return this._balance;
    }
}

// The BankAccount class above encapsulates common banking operations.

