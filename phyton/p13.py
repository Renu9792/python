from datetime import date
birthDate=int(input("enter the birthdate:"))
month=int(input("enter the month:"))
year=int(input("enter the year:"))
def calculateAge(birthDate):
    days_in_year = 365.2425   
    age = int((date.today() - birthDate).days / days_in_year)
    return age
         

print(calculateAge(date(year,month,birthDate)), "years")