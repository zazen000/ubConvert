# ubConvert   v4.2.6
A Unit of Measure Conversion Module
Utility_Belt Designs, Tacoma, WA
@author: ZennDogg

ubConvert Unit Conversion Classes -

    - Temperatures()
    - Speed()
    - Lengths()
    - Weights()
    - Volumes()
    - Times()
    - Areas()
    - Numbers()
    - Power()

 ..................................................................

 Sample usage:


    import ubConvert as ub

    weight = ub.Weights()
    ounces = weight.grams_to_ounces(28)
    ounces = 1

 ..................................................................


   The functions for most classes can be called in two ways.
   First example, to convert Kelvin to Fahrenheit from class Temperatures():

        kelvin = 278.967
        kelvin_to_fahrenheit(kelvin) = 42.74059999999997 **

        ** this is the default.

   The second way is with a number representing the rounding factor, where:
   
        0 = no decimal place (integer),
        1 = one decimal place,
        2 = two decimal places, etc.,

        For example, using the above kelvin case:

        kelvin = 278.967
        kelvin_to_fahrenheit(kelvin, 2) = 42.74
        kelvin_to_fahrenheit(kelvin, 1) = 42.7
        kelvin_to_fahrenheit(kelvin, 0) = 43

   For converting and formatting Light-Years and Astronomical Units to kilometers
   or miles, things are a little different. The first way returns an integer:

        lt_years = 2
        light_years_to_miles(lt_years) = 11758000000000

   The second instance uses a 2nd argument to specify the number of decimal places
   in scientific notation:

        lt_years = 2
        light_years_to_miles(lt_years, 4) = 1.1758e+13

   Because the answers are such large integers, the third way returns the number
   in comma separated format for easier reading (second arg = 0, third arg = 1):

        lt_years = 2
        light_years_to_miles(lt_years, 0, 1) = 11,758,000,000,000


 Functions List by Class :
 NOTE - We use all lower case when calling functions, right? RIGHT?

    - Temperatures() function list

        Kelvin_to_Fahrenheit
        Kelvin_to_Celsius
        Fahrenheit_to_Kelvin
        Fahrenheit_to_Celsius
        Fahrenheit_to_Rankine
        Celsius_to_Fahrenheit
        Celsius_to_Kelvin
        Rankine_to_Fahrenheit
        Rankine_to_Celsius
        Celsius_to_Rankine
        Rankine_to_Kelvin
        Kelvin_to_Rankine


    - Speed() function list

        MPH_to_KPH
        KPH_to_MPH
        Mach_to_MPH
        MPH_to Mach
        Mach_to_KPH
        KPH_to_Mach
        Knots_to_MPH
        MPH_to_Knots
        Knots_to_KPH
        KPH_to_Knots
        MPH_to_Meters_per_Second
        Meters_per_Second_to_MPH
        Meters_per_Second_to_KPH
        KPH_to_Meters_per_Second


    - Class Lengths() function list

        Miles_to_Kilometers
        Kilometers_to_Miles
        Light_Years_to_Kilometers
        Kilometers_to_Light_Years
        Light_Years_to_Miles
        Miles_to_Light_Years
        Yards_to_Meters
        Meters_to_Yards
        Inch_to_Centimeter
        Centimeter_to_Inch
        Astronomical_Unit_to_Miles
        Miles_to_Astronomical_Unit
        Astronomical_Unit_to_Kilometers
        Kilometers_to_Astronomical_Unit


    - Class Weights() function list

	    Grams_to_Ounces
        Ounces_to_Grams
        Kilograms_to_Pounds
        Pounds_to_Kilograms
        Kilograms_to_Tons
        Tons_to_Kilograms
        Tons_to_Metric_Tonnes
        Metric_Tonnes_to_Tons


    - Class Volumes() function list

	    Liters_to_Gallons
        Gallons_to_Liters
        Ounces_to_Milliliters
        Milliliters_to_Ounces
        Cubic_Centimeter_to_Cubic_Inch
        Cubic_Inch_to_Cubic_Centimeter
        Pints_to_Liters
        Liters_to_Pints
        Pints_to_Quarts
        Quarts_to_Pints


    - Class Times() function list

	    Date_to_Timestamp
	    Timestamp_to_Date
        Now_to_Timestamp
        Now_to_Datetime
        Hours_to_Seconds
        Days_to_Seconds
        Weeks_to_Seconds
        Months_to_Seconds
        Years_to_Seconds


    - Class Areas() function list

        sq_Yards_to_sq_Meters
        sq_Meters_to_sq_Yards
        sq_Meters_to_sq_Feet( number, num=2 )
        sq_Kilometers_to_sq_Miles
        sq_Miles_to_sq_Kilometers
        Acres_to_sq_Yards
        Acres_to_sq_Feet
        Acres_to_Hectares
        Hectares_to_Acres
        Hectares_to_sq_Kilometers
        Hectares_to_sq_Miles


    - Class Numbers() function list

        Binary_to_Decimal
        Decimal_to_Binary
        Octal_to_Decimal
        Decimal_to_Octal
        Hexadecimal_to_Decimal
        Decimal_to_Hexadecimal


    - Class Power() function list

        Watt_to_Horsepower
        Horsepower_to_Watt
        Newton_Meter_to_Horsepower
        Horsepower_to_Newton_Meter
        Brake_Horsepower_to_Horsepower
        Horsepower_to_Brake_Horsepower
