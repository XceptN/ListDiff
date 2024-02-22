import sys,csv

def csvline2list(file_path):
    with open(file_path, "r", newline='') as csvlinefile:
        for row in csv.reader(csvlinefile):
            return row
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ListDiff.py <file1> <file2>")
        sys.exit(1)

    list1 = csvline2list(sys.argv[1])
    list2 = csvline2list(sys.argv[2])
    difference = [item for item in list2 if item not in list1]
    for item in difference:
        print(item, end=",")
    
    print("\b \b", end="\n" )
    