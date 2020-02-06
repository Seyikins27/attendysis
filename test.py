from biometrics import LoadCsv


def main():
    data=LoadCsv.LoadCsv("C:/Users/User/Documents/biom/att_log.csv")
    data.head()
    data.tail()


if __name__ == '__main__':
    main()

