# Create list of recurring todotxt tasks
#
# Write output to a csv.
import datetime

priority = "(B)"
number_of_recurrences = 10

# set start date
year = 2025
month = 4
day = 1
start_date = datetime.date(year, month, day)

description = "Replace toothbrush head"
creation_date = "2025-03-15"
end_time = ""
all_day_event = ""
context = ""
project = ""

path = 'G:\\OneDrive\\Desktop\\recurring-tasks.txt'
with open(path, 'w') as outfile:
#    comment to remove column headers
#    outfile.write(str("Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description,Location,Private\n"))
    for i in range(number_of_recurrences):
        threshold_date = start_date
        month1 = start_date.month
        outfile.write("{0} {1} {2} due:{3} t:{4} {5} {6}\n".format(priority, creation_date, description, start_date, threshold_date, project, context))
        start_date = start_date + datetime.timedelta(weeks=6)
        month2 = start_date.month
        #if month2 == month1:
        #   start_date = start_date + datetime.timedelta(days=7)
