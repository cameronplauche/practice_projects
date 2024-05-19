#Find PI to the Nth Digit - Enter a number and have the program
#generate PI up to that many decimal places. Keep a limit to how far the program will go.

def main():
    pi = '3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647'
    n = int(input("Enter digit: "))
    pi_list = list(pi)
    if n < 1: print("")
    elif n > len(pi_list): print(f"That digit is too large, enter a digit that is smallar than {len(pi_list)}")
    elif n == 1: print("3")
    else:
        print("3.", end = "")
        for char in pi_list[2:n + 1]:
            print(char, end = "")
    print("")

main()


