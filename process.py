log_file = open("um-server-01.txt")
#the line of above is letting the .py file access the data file um-server-01.txt

def sales_reports(log_file):
    #we created a new varible called sales_reports. that invokes log_file which runs through the data file
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Tue":
            print(line)
# then we created a for lop. then we created a new var called line. line.rstip removes everyting besides the first index which happened to be the date. without any arguments passed in. we set a new var called day and had it equal the value of line which is the date. so if its true its going to print in the console the line.

sales_reports(log_file)
 #this is going to console all of the things purchased on monday       