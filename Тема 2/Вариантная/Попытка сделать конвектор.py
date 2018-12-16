# конвертер валют https://www.youtube.com/watch?v=XBChPUgpoNs
# Галкин Антон |  ИВТ | 3 курс | 1 подгруппа

from tkinter import *
import requests

link = "https://openexchangerates.org/api/latest.json?app_id=60da2bd9b3064714b2c5f2e8b00fbd40"
date = requests.get(link)
rates = date.json()['rates']

def cfKzt():

    tenge = float(KZT.get())
    dollar = tenge/rates['KZT']
    euro = dollar/rates['EUR']
    USD.set(round(dollar, 4))
    EUR.set(round(euro, 4))

def cfUsd():
   dollar = USD.get()

def cfEur():
    pass


wn = Tk()
wn.title("Converter")
wn.geometry("400x300")

#kzt
labelKzt = Label(text = "KZT: ")
labelKzt.grid(row=0, column=0)

KZT = StringVar()
enKzt = Entry(textvariable = KZT)
enKzt.grid(row=0, column=1)

b = Button(text="CONVERT", command=cfKzt)
b.grid(row=0, column=2)

#usd
labelUsd = Label(text = "USD: ")
labelUsd.grid(row=1, column=0)

USD = StringVar()
enUsd = Entry(textvariable = KZT)
enUsd.grid(row=1, column=1)

b = Button(text="CONVERT", command=cfUsd)
b.grid(row=1, column=2)


#eur
labelEur = Label(text = "KZT: ")
labelEur.grid(row=2, column=0)

EUR = StringVar()
enEur = Entry(textvariable=EUR)
enEur.grid(row=2, column=1)

b = Button(text="CONVERT", command=cfEur)
b.grid(row=2, column=2)