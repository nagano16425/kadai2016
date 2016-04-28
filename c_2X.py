import sys           # System
import subprocess    # Subprocess

def train():    # Training
    for i in range (mi,ma,step): # range(min,max,step)
        cmd = ("./train -B 1 -c "+ str( 2**i ) + " " + sys.argv[1] + " model_c" + str(i) )
        # print ( cmd.strip().split(" ") )          # Checking Command
        subprocess.call( cmd.strip().split(" ") )   # Called Command

def test():     # Testing
    for i in range (mi,ma,step): # range(min,max,step)
        cmd = ("./predict " + sys.argv[2] + " model_c" + str(i) +" out_c" + str( i ) )
        # print ( cmd.strip().split(" ") )          # Checking Command
        subprocess.call( cmd.strip().split(" ") )   # Called Command

if __name__=="__main__":

    f = open(sys.argv[1]) # train file
    f.close()

    g = open(sys.argv[2]) # test file
    g.close()

    mi = int(sys.argv[3])       # range min
    ma = int(sys.argv[4]) + 1   # range max
    step = int(sys.argv[5])     # range step

    train()               # Jump to Training
    test()                # Jump to Testing
