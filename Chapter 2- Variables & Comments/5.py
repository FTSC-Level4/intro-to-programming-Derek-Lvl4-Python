# Define the cost of one USB stick and the total budget
usb_stick_price = 6
total_budget = 50

# Calculate how many USB sticks can be bought
usb_sticks_bought = total_budget // usb_stick_price
# The operator '//' is used for division. The usb stick price is divided by the overall budget in this operation. 
#We calculate the remaining pounds using the modulo operator %. 
# Calculate the remaining pounds after buying USB sticks
remaining_pounds = total_budget % usb_stick_price

# Display the results
print("USB sticks bought:", usb_sticks_bought)
print("Remaining pounds:", remaining_pounds)
