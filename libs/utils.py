import matplotlib.pyplot as plt
import mpld3
from datetime import datetime

from dateutil.relativedelta import relativedelta
# from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import MaxNLocator


# Function to format y-axis tick labels as integers
# def int_formatter(x, pos):
#     return 'pew {:d}'.format(int(x) * 2)
# int_formatter_instance = FuncFormatter(int_formatter)

def ga_report_to_html_graph(response):
    dates = [datetime.strptime(row['dimensionValues'][0]['value'], "%Y%m%d").date() for row in response['rows']]
    active_users = [int(row['metricValues'][0]['value']) for row in response['rows']]
    screen_page_views = [int(row['metricValues'][1]['value']) for row in response['rows']]

    # Create a figure with two subplots (axes)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

    # Function to set dynamic y-axis ticks and gridlines
    def set_dynamic_yticks(ax, data, small_step, large_step):
        max_value = max(data)
        if max_value < small_step:
            step = 1
        else:
            step = large_step
        ax.set_yticks(range(0, max_value + step, step))
        ax.grid(True)
        # ax.yaxis.set_major_formatter(int_formatter_instance)

    # Set x-axis range for the last 3 months
    three_months_ago = datetime.now().date() - relativedelta(months=3)
    today = datetime.now().date()

    # Plot active users
    ax1.plot(dates, active_users, marker='o', linestyle='-', label='Active Users')
    ax1.set_title('Active Users')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Number of Active Users')
    ax1.set_xlim([three_months_ago, today])
    ax1.yaxis.set_major_locator(MaxNLocator(integer=True))
    set_dynamic_yticks(ax1, active_users, 10, 50)

    # Plot screen/page views
    ax2.plot(dates, screen_page_views, marker='o', linestyle='-', label='Screen/Page Views', color='orange')
    ax2.set_title('Screen/Page Views')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Number of Screen/Page Views')
    ax2.set_xlim([three_months_ago, today])
    ax2.yaxis.set_major_locator(MaxNLocator(integer=True))
    set_dynamic_yticks(ax2, screen_page_views, 10, 50)

    # Adjust the layout
    plt.tight_layout()

    # Save the figure as an HTML file
    html = mpld3.fig_to_html(fig)
    with open('output.html', 'w') as f:
        f.write(html)

    # Display a message
    print("Graphs saved as 'output.html'")