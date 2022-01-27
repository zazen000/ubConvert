import ubConvert as ub

"""
Test file for ubConvert. Tests all functions. 
"""

area = ub.Areas
power = ub.Power
times = ub.Times
speed = ub.Speed
length = ub.Lengths
weight = ub.Weights
volume = ub.Volumes
numbers = ub.Numbers 	# binary, octal, decimal, hexadecimal
temperature = ub.Temperatures


var = 100

print("Temperature Class Test")
print(temperature.kelvin_to_fahrenheit(var))
print(temperature.kelvin_to_celsius(var))
print(temperature.fahrenheit_to_kelvin(var))
print(temperature.celsius_to_fahrenheit(var))
print(temperature.celsius_to_kelvin(var))
print(temperature.fahrenheit_to_celsius(var))
print(temperature.fahrenheit_to_rankine(var))
print(temperature.rankine_to_fahrenheit(var))
print(temperature.celsius_to_rankine(var))
print(temperature.rankine_to_celsius(var))
print(temperature.kelvin_to_rankine(var))
print(temperature.rankine_to_kelvin(var))
print()

print("Weights Class Test")
print(weight.grams_to_ounces(var))
print(weight.ounces_to_grams(var))
print(weight.kilograms_to_pounds(var))
print(weight.kilograms_to_ton(var))
print(weight.tons_to_kilograms(var))
print(weight.tons_to_metric_tonnes(var))
print(weight.metric_tonnes_to_tons(var))
print(weight.pounds_to_kilograms(var))
print()

print("Speed Class Test")
print(speed.mph_to_kph(var))
print(speed.kph_to_mph(var))
print(speed.meters_per_second_to_mph(var))
print(speed.mph_to_meters_per_second(var))
print(speed.meters_per_second_to_kph(var))
print(speed.kph_to_meters_per_second(var))
print(speed.mach_to_mph(var))
print(speed.mph_to_mach(var))
print(speed.mach_to_kph(var))
print(speed.kph_to_mach(var))
print(speed.knots_to_mph(var))
print(speed.mph_to_knots(var))
print(speed.knots_to_kph(var))
print(speed.kph_to_knots(var))
print()

print("Length Class Test")
print(length.miles_to_kilometers(var))
print(length.kilometers_to_miles(var))
print(length.astronomical_unit_to_miles(var))
print(length.astronomical_unit_to_kilometers(var))
print(length.miles_to_astronomical_unit(var))
print(length.kilometers_to_astronomical_unit(var))
print(length.light_years_to_kilometers(var))
print(length.light_years_to_miles(var))
print(length.miles_to_light_years(var))
print(length.kilometers_to_light_years(var))
print(length.meters_to_yards(var))
print(length.yards_to_meters(var))
print(length.inch_to_centimeter(var))
print(length.centimeter_to_inch(var))
print()

print("Area Class Test")
print(area.sq_yards_to_sq_meters(var))
print(area.sq_meters_to_sq_yards(var))
print(area.sq_meters_to_sq_feet(var))
print(area.sq_kilometers_to_sq_miles(var))
print(area.sq_miles_to_sq_kilometers(var))
print(area.acres_to_sq_yards(var))
print(area.acres_to_sq_feet(var))
print(area.acres_to_hectares(var))
print(area.hectares_to_acres(var))
print(area.hectares_to_sq_kilometers(var))
print(area.hectares_to_sq_miles(var))
print()

print("Volume Class Test")
print(volume.liters_to_gallons(var))
print(volume.gallons_to_liters(var))
print(volume.ounces_to_milliliters(var))
print(volume.milliliters_to_ounces(var))
print(volume.cubic_centimeter_to_cubic_inch(var))
print(volume.cubic_inch_to_cubic_centimeter(var))
print(volume.quarts_to_liters(var))
print(volume.liters_to_quarts(var))
print(volume.pints_to_liters(var))
print(volume.liters_to_pints(var))
print()

print("Numbers Class Test")
print(numbers.decimal_to_binary(var))
print(numbers.binary_to_decimal(var))
print(numbers.decimal_to_octal(var))
print(numbers.decimal_to_hexadecimal(var))
print(numbers.octal_to_decimal(var))
print(numbers.hexadecimal_to_decimal(var))
print()

print("Times Class Test")
print(times.timestamp_to_date(1628272978))
print(times.date_to_timestamp('2021-1-19 12:0:0'))
print(times.now_to_timestamp())
print(times.now_to_datetime())
print(times.hours_to_seconds(var))
print(times.days_to_seconds(var))
print(times.weeks_to_seconds(var))
print(times.months_to_seconds(var))
print(times.years_to_seconds(var))
print()

print("Power Class Test")
print(power.watt_to_horsepower(var))
print(power.horsepower_to_watt(var))
print(power.newton_meter_to_horsepower(var))
print(power.horsepower_to_newton_meter(var))
print(power.horsepower_to_brake_horsepower(var))
print(power.brake_horsepower_to_horsepower(var))

