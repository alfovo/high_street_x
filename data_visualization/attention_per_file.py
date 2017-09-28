import pandas as pd

from bokeh.io import output_file, show
from bokeh.charts import Bar
from bokeh.plotting import ColumnDataSource, figure

output_file('html/attention_per_file.html')
file = '../data/customer_content.csv'

customers = pd.read_csv(file)

bar_chart = Bar(customers, 'file_name', 
	values='attention_time', title='Attention Time per File', 
	legend=False, toolbar_location=None)

show(bar_chart)