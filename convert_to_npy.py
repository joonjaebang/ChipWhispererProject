import os
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

NUM_POINTS = 25004

if __name__ == "__main__":
    traces = []
    plaintext = []
    
    traceDirectory = os.path.join(os.getcwd(), "traces")
    for dir in os.listdir(traceDirectory):
        subfileDirectory = os.path.join(traceDirectory, dir)
        print subfileDirectory
        if(os.path.isdir(subfileDirectory)):
            current_Sum = [0]*NUM_POINTS
            num_Trace = 0
            for file in os.listdir(subfileDirectory):
                if file == "meanData.txt":
                    os.remove(os.path.join(subfileDirectory, file))
                    continue;
                print file
                values = []
                for line in open(os.path.join(subfileDirectory, file), 'r').readlines()[3:]:
                    number = line.split()
                    try:
                        values.append(float(number[1]))
                    except ValueError:
                        values.append(0.0)
##                plt.plot(values, linewidth=0.1, c="r")
##                plt.ion()
##                plt.show()
                #if raw_input("Include this trace?: [Y/N]").lower() == 'y':
##                print len(current_Sum)
##                print len(values)
                current_Sum = [current_Sum[i] + values[i] for i in range(0, len(values))]
                num_Trace += 1
                plt.close()

            if(num_Trace != 0):
                average = [current_Sum[i]/num_Trace for i in range(len(current_Sum))]
                writeFile = open(os.path.join(subfileDirectory, 'meanData.txt'), 'w+')
                for item in average:
                    writeFile.write(str(item) + '\n')
                print "datafile created"
                traces.append(average)
                current_plaintext = [0]*16
                plaintext_byte = '0x' + dir
                for i in range(0, len(current_plaintext)):
                    current_plaintext[i] = int(plaintext_byte, 0)
                plaintext.append(current_plaintext)

    traces_np = np.array(traces)
    print "Shape of Traces_np: " + str(np.shape(traces_np))
    plaintext_np = np.array(plaintext)
    print "Shape of plaintext_np: " + str(np.shape(plaintext_np))
    np.save("traces.npy", traces_np)
    np.save("plaintext.npy", plaintext_np)
            
