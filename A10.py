
#for i in 'abcde'[::-1]:   
#    print(i)    
# for i in range(startwert, schrittweite, stopp):

#Falls die Uhrzeit kleiner als 7 Uhr ist , soll die Konsole "Schlafzeit ausgeben werden"
from tkinter import S


time= float(input("Uhrzeit"))
s = 7
m = 12
if time <= s:
    print("Schlafzeit")
else:
    if not time == m:
        print("Have a nice day")
if time == m:
    print("Mittagessen")     
    