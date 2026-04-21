days_of_the_week={"Mon","Tue","Wed","Thur","Fri","Sat","Sun","Mon"}
print(days_of_the_week)

days_of_the_week.add("Jan")
print(days_of_the_week)
#remove friday and sunday
days_of_the_week.remove("Fri")
days_of_the_week.remove("Sun")
print(days_of_the_week)
#add back friday and sunday
days_of_the_week.add("Fri")
days_of_the_week.add("Sun")
print(days_of_the_week)