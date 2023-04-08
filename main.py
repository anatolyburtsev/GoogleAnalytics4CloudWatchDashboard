from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from libs.utils import ga_report_to_html_graph

KEY_FILE_PATH = 'gcp_key.json'

PROPERTY_ID = "363855928"

# Set up credentials
credentials = service_account.Credentials.from_service_account_file(
    KEY_FILE_PATH, scopes=['https://www.googleapis.com/auth/analytics.readonly'])

# Initialize the Analytics Data API client
analytics = build('analyticsdata', 'v1beta', credentials=credentials)

start_date = (datetime.now() - relativedelta(months=3)).strftime('%Y-%m-%d')
# Define the request
request_body = {
    'date_ranges': [{'start_date': start_date, 'end_date': 'today'}],
    'dimensions': [{'name': 'date'}],
    'metrics': [{'name': 'activeUsers'}, {'name': 'screenPageViews'}],
}

# Make the request
response = analytics.properties().runReport(property=f'properties/{PROPERTY_ID}', body=request_body).execute()

ga_report_to_html_graph(response)
print(json.dumps(response, indent=2))
