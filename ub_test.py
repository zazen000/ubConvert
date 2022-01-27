from ubConvert import Temperatures as temp
from ubConvert import Weights as weight
import ubConvert as ub


stuff = ub.Speed.kph_to_mph(102)
temperature = ub.Temperatures
change = temperature.fahrenheit_to_celsius(111)
answer = weight.pounds_to_kilograms(28, 2)
print(stuff)
print(answer)
print(change)
