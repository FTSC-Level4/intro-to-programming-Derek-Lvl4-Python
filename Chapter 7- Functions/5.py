



def describe_city(city, country="Iceland"):
 """
 Prints a simple sentence describing a city and its country.

 Args:
   city: The name of the city.
   country: The country the city is in (defaults to Iceland).
 """
 print(f"{city} is in {country}.") # this is used to describe the city 
 # and combining the value of city and country 

# Call the function for three different cities
describe_city("Reykjavik")  # Uses the default country
describe_city("Tokyo", "Japan")  # Specifies a different country
describe_city("Paris", "France")  # Specifies another country