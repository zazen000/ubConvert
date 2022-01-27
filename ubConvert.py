# -*- coding: utf-8 -*-
# Created on Thu May 10 16:04:56 2020

from datetime import datetime, timedelta, date
import time


def main():
    """
    ubConvert conversion module
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

    *** Sample usage: ***


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


    Functions: NOTE- We use all lower case when calling functions, right?

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
    """
    pass



def dry(num: int, equation: float) -> float:
    """
    dry = Don't Repeat Yourself. This function
    is used by most of the conversion functions
    to format the output.

    Default: num = -1
    """
    if num == -1:
        return equation

    elif num == 0:
        return int( equation )

    else:
        return round( equation, num )


def dry_2(num: int, equation: float, comma: int) -> float:
    """
    This function is used by the large number
    astronomical functions to format the output.
    """
    if comma > 0:
        return "{:,}".format( equation )

    elif num > 0 and not comma:
        return format( round( equation, num ) ), (
                "10." + str( num ) + "e"
        )

    else:
        num == -1
        return equation



class Temperatures(object):
    """
    Formulas for Temperature Conversions
    """

    def kelvin_to_fahrenheit(number, num=-1):
        equation = float(( number ) - 273.15) * 1.8 + 32
        return dry( num, equation )


    def kelvin_to_celsius(number, num=-1):
        equation = float( number ) - 273.15
        return dry( num, equation )


    def fahrenheit_to_kelvin(number, num=-1):
        equation = (float( number ) + 459.67) * 0.555555
        return dry( num, equation )


    def celsius_to_fahrenheit(number, num=-1):
        equation = float( number ) * (1.8) + 32
        return dry( num, equation )


    def celsius_to_kelvin(number, num=-1):
        equation = float( number ) + 273.15
        return dry( num, equation )


    def fahrenheit_to_celsius(number, num=-1):
        equation = ((float( number ) - 32) * 0.555555)
        return dry( num, equation )


    def fahrenheit_to_rankine(number, num=-1):
        equation = float( number ) + 459.67
        return dry(num, equation)


    def rankine_to_fahrenheit(number, num=-1):
        equation = float( number ) - 459.67
        return dry(num, equation)


    def celsius_to_rankine(number, num=-1):
        equation = (float(number) + 273.15) * 1.8
        return dry( num, equation )


    def rankine_to_celsius(number, num=-1):
        equation = (float(number) - 491.67) * 0.555555
        return dry( num, equation )


    def kelvin_to_rankine(number, num=-1):
        equation = float( number ) * 1.8
        return dry( num, equation )


    def rankine_to_kelvin(number, num=-1):
        equation = float( number ) * 0.555555556
        return dry( num, equation )



class Speed(object):
    """
    Formulas for Speed and Distance Conversions
    """

    def mph_to_kph(number, num=-1):
        equation = float(number) * 1.609344
        return dry(num, equation)


    def kph_to_mph(number, num=-1):
        equation = float(number) * 0.621371192237334
        return dry(num, equation)


    def meters_per_second_to_mph(number, num=-1):
        equation = float(number) * 2.2369362921
        return dry(num, equation)


    def mph_to_meters_per_second(number, num=-1):
        equation = float(number) * 0.4470399999908875
        return dry(num, equation)


    def meters_per_second_to_kph(number, num=-1):
        equation = float(number) * 3.599999999712
        return dry(num, equation)


    def kph_to_meters_per_second(number, num=-1):
        equation = float(number) * 0.2777777778
        return dry(num, equation)


    def mach_to_mph(number, num=-1):
        equation = float(number) * 660
        return dry( num, equation )


    def mph_to_mach(number, num=-1):
        equation = float(number) * 0.00130104773
        return dry( num, equation )


    def mach_to_kph(number, num=-1):
        equation = float(number) * 1062.16704
        return dry( num, equation )


    def kph_to_mach(number, num=-1):
        equation = float(number) * .0009414715034
        return dry( num, equation )


    def knots_to_mph(number, num=-1):
        equation = float(number) * 1.150779448
        return dry( num, equation )


    def mph_to_knots(number, num=-1):
        equation = float(number) * .8689762419
        return dry( num, equation )


    def knots_to_kph(number, num=-1):
        equation = float(number) * 1.852
        return dry( num, equation )


    def kph_to_knots(number, num=-1):
        equation = float(number) * .5399568034557235
        return dry( num, equation )



class Lengths(object):
    """
    Formulas for Length(Distance) Conversions
    """

    def miles_to_kilometers(number, num=-1):
        equation = float(number) * 1.609344
        return dry(num, equation)


    def kilometers_to_miles(number, num=-1):
        equation = float(number) * 0.621371192237334
        return dry(num, equation)


    def astronomical_unit_to_miles(number, num=-1, comma=1):
        equation = float(number) * 92955807.26743
        return dry_2(num, equation, comma)


    def astronomical_unit_to_kilometers(number, num=-1, comma=1):
        equation = float(number) * 149597870.7
        return dry_2(num, equation, comma)


    def miles_to_astronomical_unit(number, num=-1):
        equation = float(number) / 92955807.26743
        return dry(num, equation)


    def kilometers_to_astronomical_unit(number, num=-1):
        equation = float(number) / 149597870.69
        return dry(num, equation)


    def light_years_to_kilometers(number, num=-1, comma=1):
        equation = float(number) * 9460730472580
        return dry_2(num, equation, comma)


    def light_years_to_miles(number, num=-1, comma=1):
        equation = float(number) * 58786253731831
        return dry_2(num, equation, comma)


    def miles_to_light_years(number):
        return float(number) * 1.70107795e-13


    def kilometers_to_light_years(number):
        return float(number) * 1.057000834e-13


    def meters_to_yards(number, num=-1):
        equation = float(number) * 1.0936133
        return dry(num, equation)


    def yards_to_meters(number, num=-1):
        equation = float(number) * 0.914399998610112
        return dry(num, equation)


    def inch_to_centimeter(number, num=-1):
        equation = float(number) * 2.54
        return dry(num, equation)


    def centimeter_to_inch(number, num=-1):
        equation = float(number) * 0.3937007874015748
        return dry(num, equation)



class Weights(object):
    """
    Formulas for Weight Conversions
    """

    def grams_to_ounces(number, num=-1):
        equation = float(number) * 0.0352739619
        return dry(num, equation)


    def ounces_to_grams(number, num=-1):
        equation = float(number) * 28.34952316484755
        return dry(num, equation)


    def kilograms_to_pounds(number, num=-1):
        equation = float(number) * 2.2046226218
        return dry(num, equation)


    def kilograms_to_ton(number, num=-1):
        equation = float(number) * 0.0011023113
        return dry(num, equation)


    def tons_to_kilograms(number, num=-1):
        equation = float(number) * 907.1847489905982
        return dry(num, equation)


    def tons_to_metric_tonnes(number, num=-1):
        equation = float(number) * 0.90718474
        return dry(num, equation)


    def metric_tonnes_to_tons(number, num=-1):
        equation = float(number) * 1.102311310924388
        return dry(num, equation)


    def pounds_to_kilograms(number, num=-1):
        equation = float( number) *  0.4535923700100354
        return dry(num, equation)



class Volumes(object):
    """
    Formulas for Volume Conversions
    """

    def liters_to_gallons(number, num=-1):
        equation = float(number) * 0.26417205236
        return dry(num, equation)


    def gallons_to_liters(number, num=-1):
        equation = float(number) * 3.785411784
        return dry(num, equation)


    def ounces_to_milliliters(number, num=-1):
        equation = float(number) * 29.57352968750042
        return dry(num, equation)


    def milliliters_to_ounces(number, num=-1):
        equation = float(number) * 0.033814022558919
        return dry(num, equation)


    def cubic_centimeter_to_cubic_inch(number, num=-1):
        equation = float(number) * 0.0610237440947323
        return dry(num, equation)


    def cubic_inch_to_cubic_centimeter(number, num=-1):
        equation = float(number) * 16.387064
        return dry(num, equation)


    def quarts_to_liters(number, num=-1):
        equation = float(number) * 0.946352946
        return dry( num, equation )


    def liters_to_quarts(number, num=-1):
        equation = float(number) * 1.056688209432594
        return dry( num, equation )


    def pints_to_liters(number, num=-1):
        equation = float(number) * 0.473176473
        return dry( num, equation )


    def liters_to_pints(number, num=-1):
        equation = float(number) * 2.113376418865187
        return dry( num, equation )



class Times(object):
    """
    Formulas for Time Conversions
    NOTE: tzinfo not incorporated
    """

    def timestamp_to_date(number):
        return datetime.fromtimestamp(int(number))


    def date_to_timestamp(date_str):
        """
        date_str format = '2021-1-19 12:0:0'
        """
        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        return int(dt.timestamp())


    def now_to_timestamp():
        return time.time()


    def now_to_datetime():
        return str(datetime.now())


    def hours_to_seconds(number, num=-1):
        equation = float(number) * 3600
        return dry( num, equation )


    def days_to_seconds(number, num=-1):
        equation = float(number) * 86400
        return dry( num, equation )


    def weeks_to_seconds(number, num=-1):
        equation = float(number) * 604800
        return dry( num, equation )


    def months_to_seconds(number, num=-1):
        equation = float(number) * 2628000
        return dry( num, equation )


    def years_to_seconds(number, num=-1):
        equation = float(number) * 31536000
        return dry( num, equation )



class Areas(object):
    """
    Formulas for Area Conversions
    """

    def sq_yards_to_sq_meters(number, num=-1):
        equation = float(number) * .83612736
        return dry(num, equation)


    def sq_meters_to_sq_yards(number, num=-1):
        equation = float(number) * 1.19599004630108
        return dry(num, equation)


    def sq_meters_to_sq_feet(number, num=-1):
        equation = float(number) * 10.76391041670972
        return dry( num, equation )


    def sq_kilometers_to_sq_miles(number, num=-1):
        equation = float(number) * 0.38610215854245
        return dry(num, equation)


    def sq_miles_to_sq_kilometers(number, num=-1):
        equation = float(number) * 2.589988110336
        return dry(num, equation)


    def acres_to_sq_yards(number, num=-1):
        equation = float(number) * 4840.01936
        return dry(num, equation)


    def acres_to_sq_feet(number, num=-1):
        equation = float(number) * 43560.04
        return dry( num, equation )


    def acres_to_hectares(number, num=-1):
        equation = float(number) * 0.4046856422
        return dry( num, equation )


    def hectares_to_acres(number, num=-1):
        equation = float(number) * 2.471053814915898
        return dry( num, equation )


    def hectares_to_sq_kilometers(number, num=-1):
        equation = float(number) / 100
        return dry( num, equation )


    def hectares_to_sq_miles(number, num=-1):
        equation = float(number) *0.0038610216
        return dry( num, equation )



class Numbers(object):
    """
    Formulas for number base Conversions
    """

    def decimal_to_binary(number):
        return bin(number).replace("0b", "")


    def binary_to_decimal(number):
        var = str(number)
        return int(var, 2)


    def decimal_to_octal(number):
        return oct(number).replace("0o", "")


    def octal_to_decimal(number):
        var = str(number)
        return int(var, 8)

        return decimal


    def decimal_to_hexadecimal(number):
        decimal = int(number)
        return hex(decimal).replace("0x", "")


    def hexadecimal_to_decimal(number):
        var = str(number)
        return int(var, 16)



class Power(object):
    """
    Formulas for Power conversions
    Horsepower = horsepower-hour
    """

    def watt_to_horsepower(number, num=-1):
        equation = float(number) * 0.0013410220888438
        return dry( num, equation )


    def horsepower_to_watt(number, num=-1):
        equation = float(number) * 745.69987158
        return dry( num, equation )


    def newton_meter_to_horsepower(number, num=-1):
        equation = float(number) * 0.000000372506
        return dry( num, equation )


    def horsepower_to_newton_meter(number, num=-1):
        equation = float(number) * 2684519.5376862
        return dry( num, equation )


    def horsepower_to_brake_horsepower(number, num=-1):
        equation = float( number ) * 0.9863217468971388
        return dry( num, equation )


    def brake_horsepower_to_horsepower(number, num=-1):
        equation = float( number ) * 1.01386794232804
        return dry( num, equation )



if __name__ == "__main__":
    main()

