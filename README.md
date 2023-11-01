# ✓ Prime Number Verification Application - Documentation

## Introduction

This Python program is an application that verifies if a given number is a prime number or not. The program allows the user to enter a list of numbers and checks each number in the list to determine if it is a prime number.

## How to Use

1. Run the program in your preferred Python environment.
2. Enter the total number of numbers you want to verify when prompted by the application.
3. For each number, enter the number you want to check for primality.
4. Press 'ESC' key to exit the application at any time.
5. The program will display the list of prime numbers (if any) from the given inputs.

## Program Logic

- The program consists of two functions:

### 1. `verify(pri)`

- This function takes an integer (`pri`) as input and checks if it is a prime number.
- It starts by checking if the input is 0. If it is, the function returns True (since 0 is not a prime number).
- The function then initializes two variables: `test` and `cont`. `test` keeps track of the remainder, and `cont` is used to iterate over possible divisors (from 2 to `pri-1`).
- It then enters a while loop to calculate the remainder of `pri` when divided by each `cont`. If the remainder is 0, `test` will be greater than 0, and the loop will break, indicating that the number is not prime.
- Finally, the function returns True if the number is prime (i.e., `test` is 0), otherwise, it returns False.

### 2. `main()`

- This is the main function that interacts with the user and performs the verification process.
- It starts by initializing some variables, including an empty list `primo` to store the prime numbers found.
- The user is prompted to enter the total number of numbers (`n`) they want to verify.
- The program then enters a loop where the user is asked to input each number to be checked for primality.
- For each input number, the `verify` function is called to check if it is a prime number. If it is, the number is appended to the `primo` list.
- The program continues until the desired number of inputs are processed.
- After processing all inputs, the program displays the list of prime numbers (if any) found.

## Example Usage

```
Digite a quantidade de números que deseja verificar: 5
Digite o 1° número para verificação: 7
(Press ESC to exit)
Digite o 2° número para verificação: 4
(Press ESC to exit)
Digite o 3° número para verificação: 11
(Press ESC to exit)
Digite o 4° número para verificação: 1
(Press ESC to exit)
Digite o 5° número para verificação: 9
(Press ESC to exit)
Esses são os números primos: [7, 11]
```

## Note

- The program demonstrates a simple prime number verification application based on the user's inputs.
- The program does not handle non-integer inputs or invalid inputs from the user. For a real-world application, proper input validation should be implemented for robustness.
