import subprocess
import sys

if __name__=='__main__':
    file = sys.argv[1]
    print('file to analyze is %s' %file)
    result = subprocess.check_output(['readelf', '-Ws', file])
    print ("readelf -Ws "+file+"result is :")
    print (result)
    symbolArray = result.decode('utf-8').split('\n')[3:]
    print("first line:")
    print(symbolArray[0])
