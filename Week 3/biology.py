# A program that determins the type of animal based on a simple classification scheme 
# Mwansa Ng'andu
# 02 March 2022

print ("Welcome to the Biology Expert")
print ("-----------------------------")

print ("Answer the following questions by selecting from among the options.")

skeleton = input("The skeleton is (internal/external)? \n")
if skeleton == 'external':
    print ("Type of animal: Arthropod")

else:
    fertilisation = input("The fertilisation of eggs occurs (within the body/outside the body)? \n")
    if fertilisation == 'outside the body':  
        lives = input("It lives (in water/near water)? \n")
        if lives == 'near water':
            print ("Type of animal: Amphibian")
        else: 
            print ("Type of animal: Fish")
    
    else:
        if fertilisation == 'within the body': 
            offspring = input("Young are produced by (waterproof eggs/live birth)? \n")
            if offspring == 'live birth':
                print ("Type of animal: Mammal")
                
            else:
                if offspring == 'waterproof eggs':
                    skin = input("The skin is covered by (scales/feathers)? \n")  
                    if skin == 'scales':
                        print ("Type of animal: Reptile")
                    elif skin == 'feathers':
                        print ("Type of animal: Bird")