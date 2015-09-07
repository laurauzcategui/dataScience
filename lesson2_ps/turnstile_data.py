import csv
import pandas

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt

    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file.

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775

    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the
    Instructor Notes below for more details on the task.

    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy

    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file in the links below:

    Sample input file:
    https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt
    Sample updated file:
    https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt
    '''

    pathF = '/home/laura/Documents/DataScience/Nanodegree/dataScience/lesson2_ps/'
    for filename in filenames:
        f_in = open(pathF + filename,'rb')
        f_out = open(pathF + 'updated_' + filename, 'w')
        #f_in = open(filename,'rb')
        #f_out = open('update_' + filename, 'w')
        reader_in = csv.reader(f_in, delimiter=',')
        writer_out = csv.writer(f_out)
        for line in reader_in:
            #print line
            header = line[0:3]
            len_line = len(line[3:])
            y = 0
            for idx in range(3,len_line):
                line_last = []
                 line[idx+y+5-1]
                print header + line[y+idx:idx+y+5] + line_last
                writer_out.writerow(header + line[y+idx:idx+y+5])
                y += 4
                if y + 8 >= len_line:
                    break

file1 = 'turnstile_110528.txt'

fix_turnstile_data([file1])
