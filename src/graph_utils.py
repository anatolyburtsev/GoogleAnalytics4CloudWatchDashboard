from datetime import datetime


def generate_html_table(dates, active_users, screen_page_views):
    table_rows = ""

    for i, date in enumerate(dates):
        table_rows += f"""
<tr>
    <td>{date}</td>
    <td>{active_users[i]}</td>
    <td>{screen_page_views[i]}</td>
</tr>
"""

    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Data Table</title>
    <style>
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th, td {{
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>Date</th>
                <th>Active Users</th>
                <th>Screen Page Views</th>
            </tr>
        </thead>
        <tbody>
            {table_rows}
        </tbody>
    </table>
</body>
</html>
"""

    return html_content


def ga_report_to_html_graph(response):
    dates = [datetime.strptime(row['dimensionValues'][0]['value'], "%Y%m%d").date() for row in response['rows']]
    active_users = [int(row['metricValues'][0]['value']) for row in response['rows']]
    screen_page_views = [int(row['metricValues'][1]['value']) for row in response['rows']]

    return generate_html_table(dates, active_users, screen_page_views)
