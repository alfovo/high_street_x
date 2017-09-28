# Since this data is not real, I'm not validating it at the moment. For a later script, I 
# would like to include validations for true/false characteristics like mustache, glasses 
# or beard, handle outliers, and make sure that there aren't duplicate start periods in the data

import pandas as pd

# force dates and times to match up between dataframes by setting 
# year, month, day, hour and minutes to '2017-08-21 00:30'
def make_fake_datetime_matching(dt):
	return dt.to_pydatetime().replace(hour=0, minute=30, year=2017, month=8, day=21)

# make data more readable and fun! 
# I'm assuming 1 and 2 indicate the number of X chromosomes
def convert_gender(gender):
	return 'female' if gender == 1 else 'male'

# Based on the gender breakdown, I'm assuming 1 is yes and 2 is no
def convert_characteristics(characteristic):
	if characteristic == 1:
		return True
	else:
		return False


# since the data doesn't match up we'll have to fake it for experimentation purposes
# create 'fake_start_time' with fake datetimes
# drop 'fake_start_time' duplicates and set it up as index
# (presumably there will be no start time duplicates with real data, 
# but since this is faked, we'll work with what we've got for now)
def setup_df(df, start_time):
	df['fake_start_time'] = df[start_time].map(lambda x: make_fake_datetime_matching(x))
	df.drop_duplicates(subset='fake_start_time', inplace=True)
	df.set_index('fake_start_time')
	return df

# load and parse cms data
# set up cms dataframe
cms_headers = ['start_time', 'end_time', 'zone', 'media_type', 'file_name']
dtypes = {'start_time': 'str', 'end_time': 'str', 'zone': 'str', 'media_type': 'str', 'file_name': 'str'}
parse_dates = ['start_time', 'end_time']
cms_df = pd.read_csv("data/cms_data.csv", names=cms_headers, dtype=dtypes, parse_dates=parse_dates, skiprows=1)

cms_df = setup_df(cms_df, 'start_time')

# load and parse ava data
# set up ava dataframe
parse_dates = ['period_start']
ava_df = pd.read_csv("data/ava_data.csv", parse_dates=parse_dates, skiprows=15)

ava_df = setup_df(ava_df, 'period_start')
ava_df['gender'] = ava_df['gender'].map(lambda x: convert_gender(x))
ava_df['mustache'] = ava_df['mustache'].map(lambda x: convert_characteristics(x))
ava_df['beard'] = ava_df['beard'].map(lambda x: convert_characteristics(x))
ava_df['glasses'] = ava_df['glasses'].map(lambda x: convert_characteristics(x))

# join dataframes on their fake_start_times
result = pd.merge(ava_df, cms_df, on=['fake_start_time'])

# export to csv
result.to_csv('data/customer_content.csv')
