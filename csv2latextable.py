#!/usr/bin/python
import argparse
import csv
import re

class Csv2LatexTable:
    def __init__(self, inputFile, delimiter, quotechar, tablepos, cap, reflable, underLine):
        self.inputFile = inputFile
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.tablePos  = tablepos 
        self.caption   = cap
        self.refLable  = reflable
        self.underLine = underLine

    def readCsv(self):
        with open(self.inputFile, "r") as csvfile:
            tablereader = csv.reader(csvfile, delimiter=self.delimiter, quotechar=self.quotechar)
            columnHeaders = tablereader.next()
            numColumn = len(columnHeaders)
            self.genTableHead(numColumn)
            
            print("  %s \\\\" % (' & '.join(columnHeaders[:numColumn])))
            print("  \\hline")
            
            for row in tablereader:
                #print(len(row))
                print("  %s \\\\" % re.sub('_', '\\_', ' & '.join(row[:numColumn]) ))
                if (self.underLine):
                    print("\\hline")
            
            self.genTableFooter()

    def genTableHead(self, numColumn):
        temp = 'c' + ('|c'*(numColumn-1)) + '|'
        print("""\\begin{table}[%s]
\\centering
 \\caption{%s}
 \\begin{tabular}{%s}""" % (self.tablePos, self.caption, temp))

    def genTableFooter(self):
        print(" \\end{tabular}")
        if (self.refLable != ""):
            print("\\label{%s}" % self.refLable)
        print("\\end{table}")



if __name__=="__main__":
    parser = argparse.ArgumentParser(
        description="""Csv to latex table converter.  """)
    parser.add_argument('-i', dest='inputFile', default="example1.csv", 
                        help="Csv file to read, default=example1.csv")    
    parser.add_argument('-d', dest='delimiter', default=";", 
                        help="Set csv delimiter, default=;")    
    parser.add_argument('-q', dest='quotechar', default='"', 
                        help='Set csv quotechar, default="')    
    parser.add_argument('-pos', dest='tablePos', default="htbp", 
                        help="Set table position, default=htbp")
    parser.add_argument('-caption', dest='caption', default="Generated table", 
                        help="Set table caption, default='Generated table'")   
    parser.add_argument('-lable', dest='refLable', default="", 
                        help="Set table reference lable, default=''")   
    parser.add_argument('--underline', dest='underLine', action='store_true', 
                        help="Add underline for each new entry")   

    args = parser.parse_args()

    c2lt = Csv2LatexTable(args.inputFile, args.delimiter, args.quotechar, args.tablePos, args.caption, args.refLable, args.underLine)
    c2lt.readCsv()
