from Lib.loginLib import loginLib

def main():
    while True:
        print("=" *130)
        print("\t\t\t\t\t\tWELCOME TO CLINIC MANAGEMENT SYSTEM")
        print("=" *130)
        loginLib.login()

if __name__ == "__main__":
    main()
    