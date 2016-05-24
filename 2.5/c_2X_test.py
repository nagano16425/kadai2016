import sys           # System
import subprocess    # Subprocess

if __name__=="__main__":

    f = open(sys.argv[1]) # input file
    f.close()
    g = open(sys.argv[2]) # test file
    g.close()

    for i in range (-15,16,1): # range(min,max,step)
        cmd = ("./predict " + sys.argv[2] + " model_c" + str(i) +" out_c" + str( i ) )
        print ( cmd.strip().split(" ") )
        subprocess.call( cmd.strip().split(" ") )    # Pythonコマンド実行
