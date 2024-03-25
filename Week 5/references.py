# A program to reformat references
# Mwansa Ng'andu
# 21 March 2022

wrong_ref = input("Enter the reference:\n")

a = wrong_ref.index ('(')
b = wrong_ref.index (')')
start = b
c = wrong_ref.index (',', start)

lower_ref = wrong_ref[:a+1].lower() # Capitalize every word before first open bracket
caps_ref = lower_ref.title() # Capitalize every word before first open bracket
lower_ref_1 = wrong_ref[b:c+1].lower() # Lowercase everything after first close bracket up until first comma 
upper_ref = lower_ref_1[2::].capitalize() # Uppercase first word of the title

print ("Reformatted reference:\n", caps_ref+wrong_ref[a+1:b]+') '+upper_ref+wrong_ref[c+1::], sep='')