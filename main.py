import glob
import pandas


def main():
    while True:
        files = glob.glob("gps/*.csv")

        if len(files) != 0:
            print("Files found:")

            for num, fileName in enumerate(files):
                print(str(num) + " -> " + fileName)

            print()

            option = int(input("Please enter the number of the file you would like to read in: "))

            if option < 0 or option > len(files) - 1:
                print("Not a valid option.")
            else:
                data = pandas.read_csv(files[option], usecols=["latitude", "longitude"])

                latitude = data["latitude"]
                longitude = data["longitude"]

                prefix = input("Please enter a prefix: ")
                delimiter = input("Please enter a delimiter: ")
                postfix = input("Please enter a postfix: ")
                print()

                with open("output.txt", "w") as f:
                    for index in range(len(latitude)):
                        f.write(prefix + str(latitude[index]) + delimiter + str(longitude[index]) + postfix + "\n")

        else:
            print("Could not find any csv files.\n")


if __name__ == '__main__':
    main()
