import sys           # System
import subprocess    # Subprocess

if __name__=="__main__":

    f = open(sys.argv[1]) # input file
    f.close()

    for i in range (-15,16,1): # range(min,max,step)
        cmd = ("./train -B 1 -c "+ str( 2**i ) + " " + sys.argv[1] + " model_c" + str(i) )
        print ( cmd.strip().split(" ") )
        subprocess.call( cmd.strip().split(" ") )    # Pythonコマンド実行
