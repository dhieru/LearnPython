hrs = raw_input("Enter Hours:")
h = float(hrs)
rateperhour = raw_input("Enter rate per hour: ")
r = float(rateperhour)
grosspay = 40*r
if h > 40:
    hourextra = h-40
    grosspay = grosspay + (1.5*hourextra*r)
print grosspay