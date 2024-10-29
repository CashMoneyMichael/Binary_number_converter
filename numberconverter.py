def decimalToBinary():

    num = int(input("Enter a regular number between 0 and 15: "))
    
    if num >= 0 and num <= 15:
        binary_str = bin(num)[2:].zfill(4)
        print(f"The 4-bit binary string of {num} is: {binary_str}")
    else:
        print("You did not follow directions, try again")

decimalToBinary()
