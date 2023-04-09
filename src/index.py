import json
from ga_utils import get_ga_report
from graph_utils import ga_report_to_html_graph
import boto3


def get_gcp_credentials(secret_name):
    secretsmanager = boto3.client("secretsmanager")
    response = secretsmanager.get_secret_value(SecretId=secret_name)
    gcp_credentials = json.loads(response["SecretString"])
    return gcp_credentials


DOCS = """
## GA Hello World 
Function to return basic data from Google Analytics for a given property id
### Widget parameters
Param | Description
---|---
**property_id** | GA4 property id

### Example parameters
``` yaml
property_id: 363855928
```"""


def handler(event, context):
    PROPERTY_ID = event.get("property_id", "363855928")
    secret_name = 'hello_ga_secret_key'

    ga_creds = get_gcp_credentials(secret_name)
    report = get_ga_report(PROPERTY_ID, ga_creds)
    html = ga_report_to_html_graph(report)

    if 'describe' in event:
        return DOCS

    return html
#
