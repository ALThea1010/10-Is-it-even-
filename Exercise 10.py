"""
Assessment1-Programming-Skills-Portfolio Exercise 10: Is it even?
"""


# Function to check if a number is even
def is_it_even(num):
    # If the number is divisible by 2, it is even
    if num % 2 == 0:
        return True
    else:
        return False

# Main function to execute the program
def main():
    # Prompt the user to enter a number and convert it to an integer
    num = int(input("Enter any number to test whether it is odd or even: "))
    
    # Call is_it_even() to check if the number is even or odd
    if is_it_even(num):
        print(f"The number {num} is even.")
    else:
        print(f"The number {num} is odd.")

# Check if this file is being executed directly, and if so, call main()
if __name__ == "__main__":
    main()

