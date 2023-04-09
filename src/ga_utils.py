from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime
from dateutil.relativedelta import relativedelta


def get_ga_report(property_id, ga_creds):
    # Set up credentials
    credentials = service_account.Credentials.from_service_account_info(
        ga_creds,
        scopes=[
            'https://www.googleapis.com/auth/analytics.readonly'])

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
    response = analytics.properties().runReport(
        property=f'properties/{property_id}', body=request_body).execute()
    return response
