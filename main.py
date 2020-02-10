#Asks the user for 5 scores and gives the highest score, lowest score, and weighted average.
#Will ask if they want to keep going. If yes will reset scores and start over.
# Keeps a counter


large = 0
small = 10
total = 0
counter = 0 
entry = 'y'
overallAvg = 0

while entry == 'y'or entry == "Y":
   counter = counter + 1
   print 'Run number', counter
   for i in range (5):
    score = float(input('Input the score between 0 and 10'))
    while score < 0 or score > 10:
      print 'Invalid Score try again'
      score = float(input('Input the score between 0 and 10'))

    if score > large:
      large = score
    elif score < small:
      small = score
    total = total + score
  


   print 'The highest score was', large ,'and the lowest was', small
   avg = (total - large - small)/3
   print 'The average is', avg
   overallAvg = overallAvg + total
  
 
   entry = str(input('Would you like to go again? Enter y for yes and n for no.'))
   if entry == 'y'or entry == "Y":
     total = 0
     score = 0
     large = 0
     small = 10
     
   else:
     finalAvg = overallAvg/counter
     print 'The finall average is', finalAvg