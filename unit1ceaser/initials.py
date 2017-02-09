def get_initials(fullname):
    namelist = fullname.split()
    init = ""
    for aname in namelist:
        init = init + aname[0]
    return (init.upper())


def main():
    user_input = input("What is your full name?")
    print (get_initials(user_input))

if __name__ == "__main__":
    main()     