# leap year

def isleapyear(year):
    if(year%4==0 and year %100!=0) or year%400==0:
        return True
    else:
        return False
      
year=int(input( "Enter a year")) 

if isleapyear(year):
    print ('{} is a lear year.'. format(format))
else:
  print('{}is not a leap year.'.format(year))