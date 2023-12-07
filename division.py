# try except block - try ctach block

class NegativeError(Exception):
    pass


try:
    n = int(input("Enter a numerator: "))
    d = int(input("Enter a denominator: "))

    if n < 0 or d < 0:
        raise NegativeError(" No negative numbers please")

    q = n / d

    print(q)

except ZeroDivisionError:
    print("Denominator cannot be zero!")

except ValueError:
    print("Please type numbers only!")

except Exception:
    print("Something went wrong :(")

except NegativeError as e:
    print(e)

else:
    # whenever try block is run successfully i will execute
    print("I am else block")

finally:
    # I will always run
    print("I am finally block")


print("The end of the program")

# file handling example
# try:
    # open a file
    # try to do something
    # write into the file - may throw error
# except:
    # do something to handlt the error
# finally:
     # close the file