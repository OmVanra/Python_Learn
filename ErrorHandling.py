# try/except catches exceptions so your program doesn't crash.

# Use specific exception types (ValueError, TypeError) rather than bare except.

# finally always runs — use it for cleanup like closing files.


# Basic try/except
try:
    result = int(input("Enter number: "))
    print(10 / result)
except ValueError:
    print("Not a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
except Exception as e:
    print(f"Unexpected: {e}")
finally:
    print("Done.")    # always runs

# Custom exception
class InsufficientFunds(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFunds(f"Need ₹{amount}, have ₹{balance}")
    return balance - amount