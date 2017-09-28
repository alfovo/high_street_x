# Freelance work for [HighstreetX](https://highstreetx.com/)

## Contents
1. Two data files: `data/ava_data.csv` with customer profile information and `data/bai_data.csv` with content information.
2. A script, `customer_content_join.py`, that uses pandas to clean and combine the two data files into one, joining on the date and time of each entry and outputs `data/customer_content.csv`.
3. Several scripts in the `data_visualization` directory -- `attention_per_age.py` and `attention_per_file.py` -- that use [bokeh](https://bokeh.pydata.org/en/latest/) to create interactive charts of the data, stored in the html files: `attention_per_age.html` and `attention_per_file.html`.

## Use
After installing the requirements, you can run the `customer_content_join.py` script to generate the final data frame. Then you can run the `attention_per_age.py` and `attention_per_file.py` to generate html pages with charts.