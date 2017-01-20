# Extract data from Rescuetime API

import requests
import yaml
import os
import csv
from datetime import date, datetime, timedelta as td

def get_params():
    """
    Extract credentials from the yml file.
    :return:
    """
    try:
        with open(base_dir + "credentials.yml", 'r') as ymlfile:
            params = yaml.load(ymlfile)
        return params
    except ValueError:
        print("Oops!  You forgot to remove the suffix from: credentials.yml.example.  Should be: credentials.yml")

def query_activity_detail(params, start_date, end_date):
    """
    Iteratively request data from the API at the document level (the lowest level of detail: Category > Activity > Document)
    :param params: contains the base url and API key in tuple form
    :return: return list of lists
    """
    # Example of output:
    """
    [u'Date', u'Time Spent (seconds)', u'Number of People', u'Activity', u'Document', u'Category', u'Productivity']
    [[u'2016-08-16T07:00:00', 61, 1, u'photos', u'No Details', u'Photos', -2],
    [u'2016-08-16T07:00:00', 2, 1, u'play.hbogo.com', u'No Details', u'Video', -2],
    [u'2016-08-16T08:00:00', 213, 1, u'microsoft powerpoint', u'Presentation1', u'Presentation', 2],
    [u'2016-08-16T08:00:00', 172, 1, u'prezi.com', u'Climb to Success- Prezi Template by Prezi Templates by Prezibase on Prezi', u'Presentation', 2],
    [u'2016-08-16T08:00:00', 109, 1, u'prezi.com', u'My prezis | Prezi', u'Presentation', 2],
    [u'2016-08-16T08:00:00', 86, 1, u'microsoft onenote', u'Presidents Scorecard', u'Project Management', 2],
    [u'2016-08-16T08:00:00', 66, 1, u'Tableau', u'Tableau - 160607 - Udacity Data', u'Data Visualization & Analytics ', 2],
    [u'2016-08-16T08:00:00', 56, 1, u'Finder', u'No Details', u'General Utilities', 0],
    [u'2016-08-16T08:00:00', 54, 1, u'Tableau', u'Tableau - Olympic Games Candidates', u'Data Visualization & Analytics ', 2],
    [u'2016-08-16T08:00:00', 48, 1, u'prezi.com', u'Staff Picks | Our Favorite Prezis | Prezi', u'Presentation', 2]]
    """

    # Configuration for Query
    payload = {
        'perspective':'interval',
        'resolution_time':'minute',
        'restrict_kind':'document',
        'restrict_begin': start_date,
        'restrict_end': end_date,
        'format':return_form
    }
    url = params['base_url'] + params['key']
    result = []

    # Setup Iteration - by Day
    d1 = datetime.strptime(payload['restrict_begin'], "%Y-%m-%d").date()
    d2 = datetime.strptime(payload['restrict_end'], "%Y-%m-%d").date()
    delta = d2 - d1

    # Iterate through the days, making a request per day
    for i in range(delta.days + 1):
        # Find iter date and set begin and end values to this to extract at once.
        d3 = d1 + td(days=i) # Add a day
        if d3.day == 1: print 'Pulling Current Month of: ', d3

        # Update the Payload
        payload['restrict_begin'] = str(d3) # Set payload days to current
        payload['restrict_end'] = str(d3)   # Set payload days to current

        # Request
        r = requests.get(url, payload) # Make Request
        iter_result = r.json() # Parse result

        # Add Header
        headers = iter_result['row_headers']
        if len(result) == 0: result.append(headers) # Only add the first time
        # Add Rows - one by one
        for row in iter_result['rows']:
            row[3] = row[3].upper()
            row[4] = row[4].upper()
            result.append(row)

    return result

def write_to_csv(filename,data):
    """
    Simply writes the data to csv file.
    """
    print 'Now writing to CSV...'
    filepath = base_dir + filename + '.csv'

    with open(filepath,'wb') as f:
        writer = csv.writer(f)
        for row in data:
            try:
                writer.writerow(row)
            except: # Exceptions handled for errors with converting unicode to ascii
                writer.writerow([unicode(s).encode("utf-8") for s in row])

    print 'Completed writing to CSV.'


if __name__ == '__main__':
    global return_form
    global base_dir
    return_form = 'json'

    # Setup these Fields
    base_dir   = '/Users/Miller/GitHub/Blog/RescueTime/'  # Base directory where this python file is located
    start_date = '2016-12-26'  # Start date for data
    end_date   = '2017-01-14'  # End date for data
    csv_name   = 'rescuetime_data'

    # Run Query & Export to CSV
    r_query = query_activity_detail(get_params(), start_date, end_date)
    write_to_csv(csv_name,r_query)

    print 'Script Complete!'