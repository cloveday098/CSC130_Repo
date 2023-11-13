def main():
    filename = input("filename: ")
    try:
        infile = open(filename, 'r')
    except Exception as killme:
        print(killme)
        print("Go ahead and kill me")
main()