import random
"""
Since credit card option will always be approved its OK by default and show if it is "full price" or "Discounted".
Otherwise the remaining options can be randomly chosen.
apc_counter(): simulates the count of passengers boarding at a particular stop
"""
import random

def apc_counter():
    """Return a random passenger count between 0 and 75."""
    return random.randint(0, 75)

def select_payment_option():
    """Select a random payment option."""
    payment_options = ["In App tickets", "SL cards", "Credit card"]
    return random.choice(payment_options)

def determine_payment_result(payment_option):
    """Determine the payment result based on the payment option."""
    if payment_option == "Credit card":
        payment_result = "OK"
        discount_options = ["Full price", "Discounted"]
        discount = random.choice(discount_options)
    else:
        payment_results = ["OK", "PASSBACK", "NO TICKET"]
        payment_result = random.choice(payment_results)
        discount = None
    return payment_result, discount

def ticket_validation_result():
    """Perform ticket validation for 20 passengers."""
    for _ in range(20):
        passenger_count = apc_counter()
        print("Passenger Count:", passenger_count)
        if passenger_count == 0:
            print("No ticket validation required")
        else:
            payment_option = select_payment_option()
            payment_result, discount = determine_payment_result(payment_option)
            print("Payment Option:", payment_option)
            print("Result:", payment_result)
            if discount:
                print("Discount:", discount)
        print("---")

# Call the function
ticket_validation_result()
