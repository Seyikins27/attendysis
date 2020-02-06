from csv import reader
import os


class LoadCsv:
    file = ""
    data=""

    def __init__(self, csv_file):
        self.file=csv_file
        if self.is_csv():
            open_file = open(self.file)
            read_file = reader(open_file)
            self.data = list(read_file)
        else:
            print("FIle is not a csv file, upload a csv file")

    def is_csv(self):
        file, extension = os.path.splitext(self.file)
        if extension == ".csv":
            return True
        return False

    def head(self):
        for items in self.data[0:6]:
            print(items)

    def tail(self):
        length=len(self.data)
        for items in self.data[length-5:length]:
            print(items)
