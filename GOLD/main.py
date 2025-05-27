# main.py
# Project: GOLD
# Author: LinObodo
# Description: This script demonstrates a basic Python entry point for GOLD project,
#              using code structure that could be enhanced with GitHub Copilot.

def greet_user(name):
    return f"Welcome to LinObodo's GOLD project, {name}!"

def calculate_discount(price, percentage):
    """Calculate discounted price"""
    discount = price * (percentage / 100)
    return price - discount

def main():
    name = input("Enter your name: ")
    print(greet_user(name))

    price = float(input("Enter product price: "))
    discount = float(input("Enter discount %: "))
    final_price = calculate_discount(price, discount)

    print(f"Discounted price: ${final_price:.2f}")

if __name__ == "__main__":
    main()

