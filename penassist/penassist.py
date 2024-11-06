import sys

def main(args):
    if "--create-config" in sys.argv:
        createConfig()
    else: 
        print("work in progress")


def createConfig():
    print("creating a new configuration")

if __name__ == "__main__":
    main(sys.argv)