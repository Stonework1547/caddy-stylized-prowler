# Create list of Networking Breakfast Meeting calendar items
#
# Write output to a csv.
import datetime

meetingName = "Networking Breakfast Meeting"
number_of_meetings = 6

# set start date
year = 2025
month = 2
day = 2
start_date = datetime.date(year, month, day)

start_time = "7:00 AM"
end_time = "9:00 AM"
all_day_event = "False"
description = ""
location = " St Timothy Lutheran Church 1051 Kempsville Rd Norfolk VA 23502"
private = "False"

path = 'G:\\OneDrive\\Desktop\\chapter_calendar_nbm.csv'
with open(path, 'w') as outfile:
    outfile.write(str("Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description,Location,Private\n"))
    for i in range(number_of_meetings):
        end_date = start_date
        month1 = start_date.month
        outfile.write("{0},{1},{2},{3},{4},{5},{6},{7},{8}\n".format(meetingName, start_date, start_time, end_date, end_time, all_day_event, description, location, private))
        start_date = start_date + datetime.timedelta(weeks=4)
        month2 = start_date.month
        if month2 == month1:
            start_date = start_date + datetime.timedelta(days=7)
