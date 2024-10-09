def commonfun(str1, str2):
    return(len((set(str1)).intersection(set(str2))))    #set() removes duplicates character from string
                                                      #intersection() find common character from both sets
                                                      #len() is used to calculate the number of common character

str1 = "VISHAV"
str2 = "VANSHIKA"

no_of_common_character = commonfun(str1.lower(),str2.lower())

print("No. of Common Characters is: ", no_of_common_character)