# Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item.
def likes(names):
   if not names:
       return "no one likes this"
   elif len(names) == 1:
       return names[0] + " likes this"
   elif len(names) == 2:
       return names[0] + " and " + names[1] + " like this"
   elif len(names) == 3:
       return names[0] + ", " + names[1] + " and " + names[2] + " like this"
   else:
       return names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like            this"
