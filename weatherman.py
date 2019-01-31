#! /usr/bin/env python3

# TODO: Review code with PEP 8 convention.

import sys, os, re


# ---- Start Functions ----#

def is_report_number_valid(report_number):
    return report_number == '1' or report_number == '2'

def is_data_dir_path_valid(data_dir):
    return os.path.exists(data_dir) and os.path.isdir(data_dir)

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

    # file_names = os.listdir(data_dir)
    # for file_name in file_names:
        # print(file_name)

    file = open(data_dir + os.path.sep + 'lahore_weather_2005_May.txt', 'r')
    file_content = file.read()

    

    find_comment_block_regex = re.compile(r'<!--.*-->')
    weather_data = file_content.split('\n')
    weather_data = list(filter(('').__ne__, weather_data))
    weather_data = list(filter(lambda i: not find_comment_block_regex.search(i), weather_data))
    #print(weather_data)

    nested_list_of_file_content = []
    for list_item_from_file in weather_data:
        nested_list_of_file_content.append(list_item_from_file.split(','))
    print(nested_list_of_file_content)

    print('\n\n\n#########')


    nested_list_of_file_content = nested_list_of_file_content[1:]#no need of titles for the time.
    #0, 1, 3, 7, 9

    year = []# Need to revisit it; It will always contain same value; So, why we need to create list and find max value in it?
    max_temperature_each_day = []
    min_temperature_each_day = []
    max_humidity_each_day = []
    min_humidity_each_day = []
    print('Year[0]   MAX Temp[1]   MIN Temp[3]   MAX Humidity[7]   MIN Humidity[9]')
    for list_item in nested_list_of_file_content:
        year.append(list_item[0].split('-')[0])#Need to revise it.
        max_temperature_each_day.append(int(list_item[1]))
        min_temperature_each_day.append(int(list_item[3]))
        max_humidity_each_day.append(int(list_item[7]))
        min_humidity_each_day.append(int(list_item[9]))
        #print(list_item[9])
        #print(list_item[0].split('-')[0], list_item[1], list_item[3], list_item[7], list_item[9], sep='   ')

    #print(min_humidity_each_day)
    
    print(max(year), max(max_temperature_each_day), min(min_temperature_each_day), max(max_humidity_each_day), min(min_humidity_each_day), sep='   ')




    

if __name__ == "__main__":
    main()






