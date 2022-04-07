import csv

with open("old_res.csv") as in_csv, open("new_res.csv") as out_csv:
            r1 = csv.writer(out_csv, delimiter=',')
            r2 = csv.reader(in_csv, delimiter=',')
            for i in r1:
                print i
