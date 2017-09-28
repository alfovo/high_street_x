import pandas as pd

from bokeh.io import output_file, show
from bokeh.charts import Bar
from bokeh.plotting import ColumnDataSource, figure
from bokeh.models import CategoricalColorMapper, HoverTool

output_file('html/attention_per_age.html')
file = '../data/customer_content.csv'

customers = pd.read_csv(file)

customer_data = ColumnDataSource(customers)

color_mapper = CategoricalColorMapper(
	factors=['FS_MOV_National_Merch_Surgeon.mp4',
       'FS_Stills_National_FoodPorn01.mp4', 'FS_Stills_National_Hat01.mp4',
       'FS_MOV_National_Hot_Girls_1.mp4',
       'FS_Stills_National_CTA_Cater.mov', 'Three Towers fat sals'],
    palette=['blue', 'green', 'crimson', 'yellow', 'cyan', 'purple'])

plot=figure(x_axis_label='attention time (seconds)', y_axis_label='age (years)', 
	tools='pan,wheel_zoom,box_zoom,reset,hover,save',
	title='Attention Time per Customer Age', toolbar_location=None)

plot.circle(x='attention_time', y='age_value', source=customer_data, size=10, 
	color=dict(field='file_name', transform=color_mapper), 
	legend='file_name')

hover = plot.select_one(HoverTool)
hover.tooltips = [('file_name', '@file_name'),
	('gender', '@gender'),
	('age_value', '@age_value'),
	('mustache', '@mustache'),
	('beard', '@beard'),
	('glasses', '@glasses')]

plot.legend.location = 'top_right'
plot.legend.background_fill_color = 'lightgrey'

show(plot)