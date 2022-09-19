import traceback

def boxPrint(symbolH, height, symbolW, width):
    if len(symbolH) != 1 or len(symbolW) != 1:
        raise Exception("Symbols need to be of length 1.")
    if height < 2 or width < 2:
        raise Exception("Height and Width needs to be at leat 2.")
    print(symbolH * width)
    for i in range(height-2):
        print(symbolW + " " * (int(width) - 2) + symbolW)
    print(symbolH * width)

try:
    boxPrint("**",5,"**",5)
except:
    errorFile = open("error_log.txt","a")
    errorFile.write(traceback.format_exc())
    errorFile.close()
    pass

boxPrint("*",5,"*",5)

import logging

logging.basicConfig(filename=".//pyFiles//box-logging.txt",level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logging.disable(logging.DEBUG)

logging.debug("Starting debugging")
def factorial(n):
    logging.debug("Number: %s" % (n))
    total = 1
    for i in range(1,n + 1):
        logging.debug("Itteration: %s" % (i))
        total *= i
        logging.debug("Total: %s" % (total))
    return total

print(factorial(5))
logging.debug("Ending debugging")
