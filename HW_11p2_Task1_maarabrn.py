# Activity Python 11: Task 1
# File: ACT_Python_HeaderTemplate_Team355_maarabrn.py 
# Date:    12 11 2023
# By:      Rania Maaraba
# Section: 21
# Team:    355
# 
# ELECTRONIC SIGNATURE
# Rania Maaraba
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# The program calculates the maximum heart rate in bpm for
# automatic and manual machines as well exercise intensity
# based on the number of calories burned.

# Input user values for weight, age, heart rate, and machiene type
Y1= float(input('Enter the user age in years: '))
L1= float(input('Enter the user weight in pounds: '))
CHR1= float(input('Enter the user current heart rate in bpm: '))
MT1= str(input('Enter the type of machine:'))


# Determine the type of machine selected
if MT1 in ['Manual', 'manual', 'm,']:
    MHR1 = 206-(0.88*Y1)
    CB1 = Y1*0.074-L1*0.05741+CHR1*0.4472-20.4022
    CB= (CB1/4.184)*60
elif MT1 in ['Auto', 'auto', 'automatic', 'Automatic']:
    MHR1 = 205.8-(0.685*Y1)
    CB1 = Y1*0.2017+L1*0.09036+CHR1*0.6309-55.969
    CB= (CB1/4.184)*60

    
# Determine Exercise Intensity Levels
if MHR1*(60/100) > CHR1:
    EIL= 'Below Level'
elif MHR1*(60/100) <= CHR1 < MHR1*(70/100):
    EIL = 'Weight Loss'
elif MHR1*(70/100) <= CHR1 < MHR1*(80/100):
    EIL = 'Cardio'
elif MHR1*(80/100) <= CHR1 < MHR1*(90/100):
    EIL= 'Anaerobic (Hardcore)'
else:
    EIL = 'Above Level'
    
# Print values for calories burned and acitivty levels
print("Calornies burnt per hour is:{0:.2f}".format(CB), end=" ")
print("for an activity level of: " + EIL)