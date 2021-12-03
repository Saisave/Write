from tkinter import *
import time






class WriteText:

   def Write(self, text, main):
      
      def waithere():
         var = IntVar()
         main.after(200, var.set, 1)
         
         main.wait_variable(var)

      full = text.split(".")
      print(full)
      comb = ""

      for full in full:
         waithere()
         comb += full
         self.config(text=comb)
