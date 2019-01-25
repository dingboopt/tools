import pandas as pd
import subprocess
import sys
import numpy
import csv

if __name__=='__main__':
    file = sys.argv[1]
    print('file to analyze is %s' %file)
    result = subprocess.check_output(['readelf', '-Ws', file])
    print ("readelf -Ws "+file+"result is :")
    print (result)
    symbolArray = result.decode('utf-8').split('\n')[2:]
    print("first line:")
    print(symbolArray[0])
    write_file = "output.csv"
    with open(write_file, "w") as output:
        for line in symbolArray:
            splitLine = line.split() 
            if splitLine == []:
                continue
            print(splitLine[0])
            splitLine[0] = splitLine[0][:-1]
            csvLine = ','.join(splitLine[:8]) 
            print(csvLine)
            output.write(csvLine + '\n')  
    df = pd.read_csv("output.csv")
    print(df.head())
