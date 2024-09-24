def main():
    cost_per_item = 19.99
    quantity = 5 

    # YOUR CODE FOR PART 1 GOES HERE  

    subtotal_cost = cost_per_item * quantity
    tax = subtotal_cost * 0.13
    total_cost = subtotal_cost + tax


    # YOUR CODE FOR PART 2 GOES HERE
    print()
    print("Code for Part 2: \n")
    print(f'cost_per_item = ${cost_per_item:0.2f}') # a sample for you to use for the other prices
    print(f'quantity = {quantity}')
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')
    print(f'tax = ${tax:0.2f}')
    print(f'total_cost = ${total_cost:0.2f} \n')


    # THIS IS THE CODE FOR PART 3
    initial_investment = 1000
    interest_rate = 0.035
    investment = initial_investment
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    print("Code for Part 3: \n")
    print('After 5 years, your investment will be worth ' + str(investment) + ' dollars.')
    # expected output: After 5 years, your investment will be worth 1187.6863056468749 dollars.

    # The error in the original code for part 3 occurs in line 29, and the reason for the error is a TypeError in which you're trying to combine a string with a float
    # which you can't normally do in Python. There are numerous ways to solve this, most notable by using string formatting such as f-strings, but my solution here 
    # will be to just convert the variable investment from a float to a string in the print function in line 29, which is now line 32.


if __name__ == "__main__":
    main()