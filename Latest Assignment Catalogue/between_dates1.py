from datetime import datetime

def between_dates(start_date, end_date):
    # Convert input strings to datetime objects.
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Calculate the difference between the 2 dates.
    difference = abs((end_date - start_date).days)

    # print the difference.
    return difference

start_date = "2010-02-28"
end_date = "2012-12-07"

print(between_dates(start_date, end_date))