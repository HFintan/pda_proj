import re
import csv

#with open('My_Games', 'r') as in_file:
#    stripped = (line.strip() for line in in_file)
#    lines = (line.split("\n\n") for line in stripped if line)
#    with open('my_games.csv', 'w') as out_file:
#        writer = csv.writer(out_file)
#        writer.writerow(('Event', 'Date', 'White', 'Black', 'Result', 'WhiteElo', 'BlackElo', 'Variant', 'TimeControl', 'First Move', 'Second Move'))
#        writer.writerow(lines)

with open('My_Games', 'r') as input_file:
    my_games=[line.rstrip('\n') for line in input_file]
    #reader=csv.reader(input_file, delimiter='\n')
    with open('my_games.csv', 'w') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(('Event', 'Date', 'White', 'Black', 'Result', 'WhiteElo', 'BlackElo', 'Variant', 'TimeControl', 'First Move', 'Second Move'))
            for row in my_games:
                writer.writerow(row)
