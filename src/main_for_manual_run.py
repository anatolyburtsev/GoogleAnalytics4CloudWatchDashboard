import json

from src.ga_utils import get_ga_report
from src.graph_utils import ga_report_to_html_graph
from src.index import get_gcp_credentials

if __name__ == "__main__":
    PROPERTY_ID = "363855928"
    secret_name = 'hello_ga_secret_key'

    # ga_creds = get_gcp_credentials(secret_name)
    # report = get_ga_report(PROPERTY_ID, ga_creds)
    response = json.loads('''
        {"dimensionHeaders": [{"name": "date"}], "metricHeaders": [{"name": "activeUsers", "type": "TYPE_INTEGER"}, {"name": "screenPageViews", "type": "TYPE_INTEGER"}], "rows": [
        {"dimensionValues": [{"value": "20230407"}], "metricValues": [{"value": "2"}, {"value": "23"}]},
        {"dimensionValues": [{"value": "20230408"}], "metricValues": [{"value": "1"}, {"value": "13"}]},
        {"dimensionValues": [{"value": "20230409"}], "metricValues": [{"value": "3"}, {"value": "43"}]}
        ], "rowCount": 1, "metadata": {"currencyCode": "USD", "timeZone": "America/Los_Angeles"}, "kind": "analyticsData#runReport"}
    ''')
    # print(json.dumps(report))
    html = ga_report_to_html_graph(response)
    with open("html_report.html", "w") as f:
        f.write(html)
