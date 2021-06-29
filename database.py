# PROJECT DECEMBRE 2019
# PROJECT STAR MAP / DATABASE
# By Enguerran VIDAL

# This file contains the database handling functions.

###############################################################
#                           IMPORTS                           #
###############################################################

import csv


###############################################################
#                        FUNCTIONS                            #
###############################################################

def csv2txt(csv_file, txt_file):
    ''' Transforms a csv file into a txt file '''
    with open(txt_file, "w") as my_output_file:
        print(" Opened new txt file")
        with open(csv_file, "r") as my_input_file:
            print(" Opened old csv file")
            [my_output_file.write(",".join(row) + '\n') for row in csv.reader(my_input_file)]
        my_output_file.close()


def format_txt(txt_file, char1, char2):
    ''' Changes "char1" into "char2" throughout an entire .txt file.'''
    with open(txt_file, "r") as file:
        lines = file.readlines()
        file.close()
    with open(txt_file, "w") as file:
        n = len(lines)
        for i in range(n):
            lines[i] = lines[i].replace(char1, char2)
            file.write(lines[i])
        file.close()


def import_database(txt_file):
    ''' Returns the data from a .txt file transformed from a csv file'''
    with open(txt_file, "r") as file:
        lines = file.readlines()
        n = len(lines)
        for i in range(n):
            lines[i] = lines[i].split(',')
            m = len(lines[i])
            for j in range(m):
                if lines[i][j] == '' or lines[i][j] == '\n':
                    lines[i][j] = 'N'
    labels = lines[0]
    lines.pop(0)
    return labels, lines


def dat2csv(dat_file, csv_file):
    with open(dat_file) as infile, open(csv_file, "w") as outfile:
        csv_writer = csv.writer(outfile)
        prev = ''
        csv_writer.writerow(['ID', 'PARENT_ID'])
        for line in infile.read().splitlines():
            csv_writer.writerow([line, prev])
            prev = line
