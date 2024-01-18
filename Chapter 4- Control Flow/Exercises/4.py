
# With age 15 in my example, the condition age < 20 is true, so the program will print "The person is teenager" 
#the condition age < 20 is true, so the program prints "The person is a teenager." 


age = 15  # You can change this value to test different cases

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:  # Assuming the only remaining option is age 65 or older
    print("The person is an elder.")