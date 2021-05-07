import os, sys, csv

path = '.'

for fp in os.listdir(path):
    if (fp.endswith('csv')):
        csvlines = []
        csvheaders = []

        with open(fp, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for idx,line in enumerate(reader):
                if (idx == 0):
                    csvheaders = line
                elif (not line):
                    continue
                else:
                    csvlines.append(line)

        out = fp.replace(".csv", "_out.meg")
        with open(out, "w") as file:
            file.write("#mega\n")
            file.write("!Title: Concatenated Files;\n")
            file.write("!Format DataType=Distance DataFormat=LowerLeft NTaxa=" + str(len(csvlines)) + ";\n")
            file.write("\n\n")

            nhead = "["
            for i in range(1, len(csvheaders)):
                file.write("[" + str(i) + "] #" + csvheaders[i] + "\n")
                nhead += "\t" + str(i)
            nhead += "\t]"

            file.write("\n" + nhead + "\n")

            for j in range(1, len(csvlines)):
                nline = "[" + str(j+1) + "]"
                for k in range(1, j+1):
                    nline += " " + csvlines[j][k]
                file.write(nline + "\n")

        print(fp + " -> " + out)

print('Completed Run')