def label_top(source, target_source, value, top_values):
    if source == target_source:
        if value in top_values:
            return 'Top'
        else:
            return 'Other'
    else:
        return value

def get_last_name(text):
    if text=='Johann Strauss II':
        return 'Strauss II'
    else:
    	return text.split(' ')[-1]

def make_dash_zero(num):
    if num==0:
        return '-'
    else:
        return str(int(num))

def shorten_opera_name(text):
		try:
			return works_dict[text]
		except:
			return text

def make_dash_zero_float(num):
    if num==0:
        return '-'
    else:
        return str(num)

def get_season(row):
    year = row.date_start.year
    if row.date_start.month<9: year -= 1
    return year