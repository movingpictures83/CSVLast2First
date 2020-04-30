import sys
import numpy
import random
import PyPluMA

class CSVLast2FirstPlugin:
   def input(self, filename):
      self.csvfile = open(filename, 'r')

   def run(self):
      self.newlines = []
      for line in self.csvfile:
         contents = line.split(',')
         contents = [contents[len(contents)-1].strip(),] + contents[0:len(contents)-1]
         newline = ""
         for j in range(len(contents)):
            newline += contents[j]
            if (j != len(contents)-1):
               newline += ','
         self.newlines.append(newline)


   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      for i in range(len(self.newlines)):
         filestuff2.write(self.newlines[i])
         if (i != len(self.newlines)-1):
            filestuff2.write('\n')



