import os, sys, time

def choice():
    print("This script will delete all .exe and .msi files in your downloads folder")
    time.sleep(1)
    confirmation = input("Would you like to continue(Y/N)? ")
    if confirmation == "Y":
        main()
    elif confirmation == "N":
        sys.exit("Canceled")
    else:
        sys.exit("Invalid parameters")


def main():
    removed = int(0)
    failed = int(0)
    for file in os.listdir("C:/users/" + os.getlogin() + "/Downloads"):
        if file.lower().endswith(".exe"):
            try:
                os.remove("C:/users/" + os.getlogin() + "/Downloads/" + file)
                print(file + " removed")
                removed += 1
                time.sleep(0.2)
            except:
                print("failed to remove " + file)
                failed += 1
                time.sleep(0.2)
        
        elif file.lower().endswith(".msi"):
            try:
                os.remove("C:/users/" + os.getlogin() + "/Downloads/" + file)
                print(file + " removed")
                removed += 1
                time.sleep(0.2)
            except:
                print("failed to remove " + file)
                failed += 1
                time.sleep(0.2)
    removed = str(removed)
    failed = str(failed)
    time.sleep(1)
    print("Removed " + removed + " files")
    print("Failed to remove " + failed + " files")
    time.sleep(15)

choice()