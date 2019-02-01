#! /usr/bin/env python3

# TODO: Review code with PEP 8 convention.

import sys, os, re, pprint, operator


# ---- Start Functions ----#

def is_report_number_valid(report_number):
    return report_number == '1' or report_number == '2'

def is_data_dir_path_valid(data_dir):
    return os.path.exists(data_dir) and os.path.isdir(data_dir)

def get_formatted_file_names(data_dir):
    '''
    Sample Data:
    {
	"1997": [
		"lahore_weather_1997_Apr.txt",
		"lahore_weather_1997_Aug.txt",
		"lahore_weather_1997_Dec.txt"
	],
	"2001": [
		"lahore_weather_2001_Apr.txt",
		"lahore_weather_2001_Aug.txt",
		"lahore_weather_2001_Dec.txt"
	],
	"2002": [
		"lahore_weather_2002_Jan.txt",
		"lahore_weather_2002_Jul.txt",
		"lahore_weather_2002_Jun.txt"
	]
    }
    '''
    formatted_file_names = {}
    file_names = os.listdir(data_dir)
    for file_name in file_names:
        if file_name.split("_")[2] not in formatted_file_names:
            formatted_file_names[file_name.split("_")[2]] = [file_name]
        else:
            formatted_file_names[file_name.split("_")[2]].append(file_name)
    return formatted_file_names

def combine_weather_data_for_a_year(data_dir, single_year_file_names):
    formatted_weather_data_of_single_year = []
    find_comment_block_regex = re.compile(r'<!--.*-->')
    for file_name in single_year_file_names:
        file = open(data_dir + os.path.sep + file_name, 'r')
        single_file_content = file.read()
        file.close()



        
        weather_data = single_file_content.split('\n')
        weather_data = list(filter(('').__ne__, weather_data))
        weather_data = list(filter(lambda i: not find_comment_block_regex.search(i), weather_data))
        

        nested_list_of_file_content = []
        for list_item_from_file in weather_data:
            nested_list_of_file_content.append(list_item_from_file.split(','))
        #print(nested_list_of_file_content)

        #print('\n\n\n#########')


        nested_list_of_file_content = nested_list_of_file_content[1:]#no need of titles for the time.
        #0, 1, 3, 7, 9

        formatted_weather_data_of_single_year.extend(nested_list_of_file_content)
    return formatted_weather_data_of_single_year

def single_year_temprature_result(single_year_weather_data):
    year = []# Need to revisit it; It will always contain same value; So, why we need to create list and find max value in it?
    max_temperature_each_day = []
    min_temperature_each_day = []
    max_humidity_each_day = []
    min_humidity_each_day = []
    #print('Year[0]   MAX Temp[1]   MIN Temp[3]   MAX Humidity[7]   MIN Humidity[9]')
    for per_day_weather_data in single_year_weather_data:
        year.append(int(per_day_weather_data[0].split('-')[0]))#Need to revise it.
        max_temperature_each_day.append(int(per_day_weather_data[1] or 0))
        min_temperature_each_day.append(int(per_day_weather_data[3] or 0))
        max_humidity_each_day.append(int(per_day_weather_data[7] or 0))
        min_humidity_each_day.append(int(per_day_weather_data[9] or 0))

    return [max(year), max(max_temperature_each_day), min(min_temperature_each_day), max(max_humidity_each_day), min(min_humidity_each_day)]

def single_year_hottest_day(single_year_weather_data):
    max_temperature_each_day_with_date = []
    for per_day_weather_data in single_year_weather_data:
        max_temperature_each_day_with_date.append([per_day_weather_data[0], int(per_day_weather_data[1] or 0)])
    #print('Year[0]   MAX Temp[1]')
    max_temperature_day = sorted(max_temperature_each_day_with_date, key=operator.itemgetter(1), reverse=True)
    return max_temperature_day[0]

def formatted_temprature_result(yearly_temprature_results):
    print('Year'.ljust(15)+'MAX Temp'.ljust(15)+'MIN Temp'.ljust(15)+'MAX Humidity'.ljust(15)+'MIN Humidity')
    print('-'.ljust(72, '-'))
    for yearly_result in yearly_temprature_results:
        print(str(yearly_result[0]).ljust(15)+str(yearly_result[1]).ljust(15)+str(yearly_result[2]).ljust(15)+str(yearly_result[3]).ljust(15)+str(yearly_result[4]))
        
    
def format_date_str(date):
        date = date.split('-')
        date.reverse()
        return '/'.join(date)

def formatted_hottest_day_result(yearly_hottest_days):
    print('Year'.ljust(15)+'Date'.ljust(15)+'Temp')
    print('-'.ljust(34, '-'))
    for yearly_result in yearly_hottest_days:
        print(str(yearly_result[0]).split('-')[0].ljust(15)+str(format_date_str(yearly_result[0])).ljust(15)+str(yearly_result[1]))

# ---- End Functions ---- #


def main():
    # Check if required arguments are present.

    # argv[0] will alway contain file name.

    # argv[1] will have first command line argument.
    # In our case, it will be report#

    # argv[2] will have second command line argument.
    # In our case, it will be data_dir

    if len(sys.argv) != 3:
        print('Usage: weatherman [report#] [data_dir]')
        sys.exit()
        
    # It means, all required arguments are present.
    report_number = sys.argv[1]
    data_dir = sys.argv[2]

    if not is_report_number_valid(report_number) or not is_data_dir_path_valid(data_dir):
        print('Error! Invalid argument(s)')
        sys.exit()

    # It means, all required arguments are valid.
    print('Congratulations! Valid Arguments.')

    formatted_file_names_dictionary = get_formatted_file_names(data_dir)
    #pprint.pprint(formatted_file_names_dictionary)

    yearly_temprature_results = []
    yearly_hottest_days = []
    for year_as_dic_key in formatted_file_names_dictionary.keys():
        single_year_weather_data = combine_weather_data_for_a_year(data_dir, formatted_file_names_dictionary[year_as_dic_key])
        if report_number == '1':
            yearly_temprature_results.append(single_year_temprature_result(single_year_weather_data))
        elif report_number == '2':
            yearly_hottest_days.append(single_year_hottest_day(single_year_weather_data))

    if report_number == '1':
        formatted_temprature_result(yearly_temprature_results)
    elif report_number == '2':
        formatted_hottest_day_result(yearly_hottest_days)

if __name__ == "__main__":
    main()






