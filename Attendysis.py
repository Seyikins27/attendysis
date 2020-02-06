from csv import reader
import os


class Attendysis:
    file = ""
    data=""
    length=""

    def __init__(self, csv_file):
        self.file=csv_file
        if self.is_csv():
            open_file = open(self.file)
            read_file = reader(open_file)
            self.data = list(read_file)
            self.length=len(self.data)
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
        for items in self.data[self.length-5:self.length]:
            print(items)

    def load(self, start="", end=""):
        if(start=="" and end== ""):
            for items in self.data:
                print(items)

    def features(self):
        columns=[]
        for column in self.data[0]:
            columns.append(column)
        return columns  

    def columns(self,features=[]):
        for feature in features:
            if feature not in self.features():
                print("Feature ",feature," not found")
            else:
                print("Feature ",feature," found")              

