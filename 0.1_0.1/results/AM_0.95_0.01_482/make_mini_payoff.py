# built-in module(s)
from multiprocessing import Pool
import sys


# not built-in
try:
    import pandas as pd

except ImportError as ie:
    print(ie.name + " cannot be imported!")
    sys.exit(1)

def make_automaton():
    hogeCsv = pd.read_csv( "hogegoge.csv", encoding="utf_8", header=None)
    payoff = pd.read_csv("payoff_0.10_0.10.csv", encoding="utf_8", header=None)
    writerows2 = []
    writerow = list(hogeCsv.iloc[0])
    writerow = writerow[2:len(writerow)]
    HEADER = writerow
    HEADER.insert(0, "")
    for t in range(1, len(writerow)):
        writerows = []
        writerows.append(writerow[t])
        for n in range(1, len(writerow)):
            writerows.append(payoff.iloc[int(writerow[t]), int(writerow[n])])
        writerows2.append(writerows)
    output_df = pd.DataFrame(writerows2, columns=HEADER)
    output_df.to_csv("payoff"+ str(len(writerow)-1) + "×" + str(len(writerow)-1) + ".csv", index=False)

if __name__ == '__main__':
    make_automaton()