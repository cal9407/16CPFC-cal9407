name = 'Da Woon CHAE'
age = 23 # not a lie
height_cm = 176 # centimeter
cm_to_inch = 1.0 / 2.54
height_inch = height_cm * cm_to_inch
weight_kg = 72 # kilogram
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %g inches tall." % height_cm
print "He's %g inches tall." % height_inch
print "He's %d pounds heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %g, and %d I get %g." % (age, height_cm, weight_kg, age + height_cm + weight_kg)