from Attendysis import Attendysis


def main():
    data=Attendysis("C:/Users/User/Documents/biom/att_log.csv")
    print(data.length)
    print(data.columns(["ABOLAJI","43","23","BABCOCK UNIVERSITY","Babcock University"]))

if __name__ == '__main__':
    main()

