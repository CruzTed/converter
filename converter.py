def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

prRed("\n*** Termmux Converter (Version:1.2) ***")
prGreen("\n*** Developed by Pavithran && Lalith ***")
print("\nAvailable Converters...")
print("\n[01]. Length\n[02]. Mass\n[03]. Volume\n[04]. Temperature")
start = int(input("\nEnter your Choice:"))
if start == 1:
    prYellow("\n*** Length Converter ***")
    print("\nAvailable Functions...")
    print("\n[01]. Kilometer(km) to Miles(mi)")
    print("\n[02]. Kilometer(km) to Feet(ft)")
    print("\n[03]. Meters(m) to Feet(ft)")
    print("\n[04]. Centimeter(cm) to Inches(in)")
    print("\n[05]. Millimeters(mm) to Inches(in)")
    print("\n[06]. Inches(in) to Meters(m)")
    print("\n[07]. Inches(in) to Centimeter(cm)")
    print("\n[08]. Inches(in) to Millimeter(mm)")
    print("\n[09]. Feet(ft) to Meters(m)")
    print("\n[10]. Yards(yd) to Meters(m)")
    print("\n[11]. Yards(yd) to Kilometers(km)")
    print("\n[12]. Miles(m) to Kilometers(km)")
    print("\n[13]. Millimeter(mm) to Centimeter(cm)")
    choice = int(input("\nEnter your Choice:"))
    if choice == 1:
        a = float(input("\nKilometer(km):"))
        b = a*0.62
        prGreen("\n%0.2f Miles(mi)"%b)
    if choice == 2:
        a = float(input("\nKilometer(km):"))
        b = a*3280.8
        prGreen("\n%0.2f Feet(ft)"%b)
    if choice == 3:
        a = float(input("\nMeter(m):"))
        b = a*3.28
        prGreen("\n%0.2f Feet(ft)"%b)
    if choice == 4:
        a = float(input("\nCentimeter(cm):"))
        b = a*0.39
        prGreen("\n%0.2f Inches(in)"%b)
    if choice == 5:
        a = float(input("\nMillimeter(mm):"))
        b = a*0.039
        prGreen("\n%0.2f Inches(in)"%b)
    if choice == 6:
        a = float(input("\nInches(in):"))
        b = a*0.0254
        prGreen("\n%0.2f Meters(m)"%b)
    if choice == 7:
        a = float(input("\nInches(in):"))
        b = a*2.54
        prGreen("\n%0.2f Centimeters(cm)"%b)
    if choice == 8:
        a = float(input("\nInches(in):"))
        b = a*25.40
        prGreen("\n%0.2f Millimeters"%b)
    if choice == 9:
        a = float(input("\nFeet(ft):"))
        b = a*0.30
        prGreen("\n%0.2f Meters(m)"%b)
    if choice == 10:
        a = float(input("\nYards(yd):"))
        b = a*0.91
        prGreen("\n%02f Meters(m)"%b)
    if choice == 11:
        a = float(input("\nYards(yd):"))
        b = a*0.00091
        prGreen("\n%0.2f Kilometers(km)"%b)
    if choice == 12:
        a = float(input("\nMiles(mi):"))
        b = a*1.61
        prGreen("\n%0.2f Kilometers(km)"%b)
    if choice == 13:
        a = float(input("\nMillimeter(mm):"))
        b = a*10
        prGreen("\n%0.2f Centimeters(cm)"%b)
    if choice > 13:
        prRed("\nInvalid Choice...Please Try Again...")
    if choice == 9:
        prRed("\nInvalid Choice...Please Try Again...")
if start == 2:
    prYellow("\n*** Mass Converter ***")
    print("\nAvailable Functions...")
    print("\n[01]. Kilogram(kg) to Tons(ton)")
    print("\n[02]. Kilogram(kg) to Pounds(lb)")
    print("\n[03]. Grams(g) to Ounces(oz)")
    print("\n[04]. Grams(g) to Pounds(lb)")
    print("\n[05]. Milligrams(mg) to Ounces(oz)")
    print("\n[06]. Ounces(oz) to Milligrams(mg)")
    print("\n[07]. Ounces(oz) to Grams(g)")
    print("\n[08]. Pounds(lb) to Kilograms(kg)")
    print("\n[09]. Tons(ton) to Kilograms(kg)")
    choice = int(input("\nEnter your Choice:"))
    if choice == 1:
        a = float(input("\nKilograms(kg):"))
        b = a*0.0011
        prGreen("\n%0.2f Tons(ton)"%b)
    if choice == 2:
        a = float(input("\nKilograms(kg):"))
        b = a*2.2046
        prGreen("\n%0.2f Pounds(lb)"%b)
    if choice == 3:
        a = float(input("\nGrams(g):"))
        b = a*0.035
        prGreen("\n%0.2f Ounces(oz)" %b)
    if choice == 4:
        a = float(input("\nGrams(g):"))
        b = a*0.002205
        prGreen("\n%0.2f Pounds(lb)"%b)
    if choice == 5:
        a = float(input("\nMilligrams(mg):"))
        b = a*0.000035
        prGreen("\n%0.2f Ounces(oz)"%b)
    if choice == 6:
        a = float(input("\nOunces(oz):"))
        b = a*28350
        prGreen("\n%0.2f Milligrams(mg)"%b)
    if choice == 7:
        a = float(input("\nOunces(oz):"))
        b = a*28.35
        prGreen("\n%0.2f Grams(g)"%b)
    if choice == 8:
        a = float(input("\nPounds(lb):"))
        b = a*0.454
        prGreen("\n%o.2f Kilograms(kg)"%b)
    if choice == 9:
        a = float(input("\nTons(ton):"))
        b = a*907.18
        prGreen("\n%0.2f Kilograms"%b)
    if choice > 9:
        prRed("\nInvalid Choice...Please Try Again...")
    if choice == 0:
        prRed("\nInvalid Choice...Please Try Again...")
if start == 3:
    prYellow("\n*** Volume Converter ***")
    print("\nAvailable Functions....")
    print("\n[01]. Liters(l) to Quarts(qt)")
    print("\n[02]. Liters(l) to Gallons(gal)")
    print("\n[03]. Milliliters(ml) to Cups(c)")
    print("\n[04]. Milliliters(ml) to Ounces(oz)")
    print("\n[05]. Ounces(oz) to Milliliters(ml)")
    print("\n[06]. Cups(c) to Milliliters(ml)")
    print("\n[07]. Quarts(qt) to Liters(l)")
    print("\n[08]. Gallons(gal) to Liters(l)")
    choice = int(input("\nEnter your Choice:"))
    if choice == 1:
        a = float(input("\nLiters(l):"))
        b = a*1.057
        prGreen("\n%0.2f Quarts(qt)"%b)
    if choice ==2:
        a = float(input("\nLiters(l):"))
        b = a*0.264
        prGreen("\n%0.2f Gallons(gal)"%b)
    if choice == 3:
        a = float(input("\nMilliliters(ml):"))
        b = a*0.0042
        prGreen("\n%0.2f Cups(c)"%b)
    if choice == 4:
        a = float(input("\nMilliliters(ml):"))
        b = a*0.0338
        prGreen("\n%0.2f Ounces(oz)"%b)
    if choice == 5:
        a = float(input("\nOunces(oz):"))
        b = a*29.57
        prGreen("\n%0.2f Milliliters(ml)"%b)
    if choice == 6:
        a =float(input("\nCups(c):"))
        b = a*236.6
        prGreen("\n%0.2f Milliliters(ml)"%b)
    if choice == 7:
        a =float(input("\nQuarts:"))
        b = a*0.95
        prGreen("\n%0.2f Liters(l)"%b)
    if choice == 8:
        a = float(input("\nGallons:"))
        b = a*3.785
        prGreen("\n%0.2f Liters(l)"%b)
    if choice > 8:
        prRed("\nInvalid Choice...Please Try Again...")
    if choice == 0:
        prRed("\nInvalid Choice...Please Try Again...")
if start == 4:
    prYellow("\n*** Temperature Converter ***")
    print("\nAvailable Functions....")
    print("\n[01]. Fahrenheit(F) to Celsius(C)")
    print("\n[02]. Celsius(C) to Fahrenheit(F)")
    choice = int(input("\nEnter your Choice:"))
    if choice == 1:
        a = float(input("\nFahrenheit(F):"))
        b =(a-32)*5/9
        prGreen("\n%0.2f Celsius(C)"%b)
    if choice ==2:
        a = float(input("\nCelsius(C):"))
        b=(a*9/5)+32
        prGreen("\n%0.2f Fahrenheit(F)"%b)
    if choice > 2:
        prRed("\nInvalid Choice...Please Try Again...")
    if choice == 0:
        prRed("\nInvalid Choice...Please Try Again...")
if start > 4:
        prRed("\nInvalid Choice...Please Try Again...")
if start == 0:
        prRed("\nInvalid Choice...Please Try Again...")






