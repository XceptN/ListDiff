import sys
import csv

def csvline2list(file_path):
    with open(file_path, "r", newline='') as csvlinefile:
        csvline_reader = csv.reader(csvlinefile)
        for row in csvline_reader:
            return row
    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ListDiff.py <file1> <file2>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    list1 = csvline2list(file1)
    list2 = csvline2list(file2)
    difference = [item for item in list2 if item not in list1]
    
    for item in difference:
        print(item, end=",")
    
    print("\b \b", end="\n" )
    