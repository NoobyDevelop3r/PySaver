import time
print("PySaver is now starting")
time.sleep(2)
iew = input("Waiting for you to write some code")
try:
    with open('script.PySaverSaved', 'w') as f:
        print("Creating saved file...")
        time.sleep(1)
        print("Putting the code inside it...")
        time.sleep(4)
        print("Making the size of the file...")
        time.sleep(0.5)
        print("Putting the final piece...")
        time.sleep(2)
        print("Code is succesfully saved!")
        f.write(iew)
except FileNotFoundError:
    print("The 'docs' directory does not exist")
time.sleep(2)
print("Goodbye!")
time.sleep(1)
exit
