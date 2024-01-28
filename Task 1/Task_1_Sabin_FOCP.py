def get_valid_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a number!")

def get_valid_yes_no_input(prompt):
    while True:
        answer = input(prompt).strip().upper()
        if answer == 'Y' or answer == 'N':
            return answer
        else:
            print('Please answer "Y" or "N".')

def calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app):
    pizza_price = 12
    delivery_cost = 2.5
    app_discount = 0.25
    tuesday_discount = 0.5

    total_price = num_pizzas * pizza_price

    if delivery_required == 'Y':
        if num_pizzas >= 5:
            delivery_cost = 0
        total_price += delivery_cost

    if is_tuesday == 'Y':
        total_price *= (1 - tuesday_discount)

    if used_app == 'Y':
        total_price *= (1 - app_discount)

    return round(total_price, 2)

def main():
    print("BPP Pizza Price Calculator\n==========================")

    num_pizzas = get_valid_integer_input("How many pizzas ordered? ")
    delivery_required = get_valid_yes_no_input("Is delivery required? (Y/N) ")
    is_tuesday = get_valid_yes_no_input("Is it Tuesday? (Y/N) ")
    used_app = get_valid_yes_no_input("Did the customer use the app? (Y/N) ")

    total_price = calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app)

    print(f"\nTotal Price: £{total_price:.2f}.")

if __name__ == "__main__":
    main()

    