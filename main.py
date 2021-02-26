import tkinter


multiNum = 0.0
roomH = 0
W1Width = 0
W2Width = 0
W3Width = 0
W4Width = 0
roomArea = 0


def setLux():
    global multiNum
    multiNum = 1.75

def setStan():
    global multiNum
    multiNum = 1.00

def setEcon():
    global multiNum
    multiNum = 0.45

def setUC():
    global multiNum
    multiNum = multiNum + 0.5

def setDems():
    global roomArea
    # print(RH.get() + ' ' + W1W.get() + ' ' + W2W.get() + ' ' + W3W.get() + ' ' + W4W.get())
    W1A = int(int(W1W.get())*int(RH.get()))
    W2A = int(int(W2W.get())*int(RH.get()))
    W3A = int(int(W3W.get())*int(RH.get()))
    W4A = int(int(W4W.get())*int(RH.get()))
    roomArea = W1A + W2A + W3A + W4A
    price = roomArea * multiNum
    print('Summary: £' + str(price))

def isbnv():
    global num
    isbn_num = isbn_tb.get()
    d1 = int(isbn_num[0]) * 1
    d2 = int(isbn_num[1]) * 2
    d3 = int(isbn_num[2]) * 3
    d4 = int(isbn_num[3]) * 4
    d5 = int(isbn_num[4]) * 5
    d6 = int(isbn_num[5]) * 6
    d7 = int(isbn_num[6]) * 7
    d8 = int(isbn_num[7]) * 8
    d9 = int(isbn_num[8]) * 9
    if isbn_num[9] == 'Z':
        d10 = 10
    else:
        d10 = int(isbn_num[9])
        d10 = d10 * 10
        d11 = (d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10)
        num = d11 % 11
    if num == 0:
        return True
    else:
        print("ISBNError", "Please Enter a valid ISBN number")
        return False


window = tkinter.Tk()
window.title("Interior Decorator")

tkinter.Label(window, text = "Name").grid(row = 0)
tkinter.Entry(window).grid(row = 0, column = 1)

tkinter.Label(window, text = "Address").grid(row = 4)
tkinter.Entry(window).grid(row = 4, column = 1)

tkinter.Label(window, text = "Paint Types").grid(row = 6, column = 0)
luxCheck = tkinter.Checkbutton(window, text = "Luxury", command = setLux).grid(row = 7, column = 0)
stanCheck = tkinter.Checkbutton(window, text = "Standard", command = setStan).grid(row = 8, column = 0)
econCheck = tkinter.Checkbutton(window, text = "Economy", command = setEcon).grid(row = 9, column = 0)

tkinter.Label(window, text = "Extras").grid(row = 6, column = 1)
undercoatCheck = tkinter.Checkbutton(window, text = "Undercoat", command = setUC).grid(row = 7, column = 1)

tkinter.Label(window, text = "ISBN").grid(row = 11, column = 0)
isbn_tb = tkinter.Entry(window)
isbn_tb.grid(row = 11, column = 1)
buttoncheck = tkinter.Button(window, text = "CHECK ISBN", fg = "red", command = isbnv).grid(row = 11, column = 2)

tkinter.Label(window, text = "Room Dimensions").grid(row = 12, column = 0)

tkinter.Label(window, text = "Room Height (2-6m): ").grid(row = 14, column = 0)
RH = tkinter.Entry(window)
RH.grid(row = 14, column = 1)
tkinter.Label(window, text = "Wall 1 Width (1-25m): ").grid(row = 15, column = 0)
W1W = tkinter.Entry(window)
W1W.grid(row = 15, column = 1)
tkinter.Label(window, text = "Wall 2 Width (1-25m): ").grid(row = 16, column = 0)
W2W = tkinter.Entry(window)
W2W.grid(row = 16, column = 1)
tkinter.Label(window, text = "Wall 3 Width (1-25m): ").grid(row = 17, column = 0)
W3W = tkinter.Entry(window)
W3W.grid(row = 17, column = 1)
tkinter.Label(window, text = "Wall 4 Widtht (1-25m): ").grid(row = 18, column = 0)
W4W = tkinter.Entry(window)
W4W.grid(row = 18, column = 1)

buttonSetDem = tkinter.Button(window, text = "Work Out Price", fg = "red", command = setDems).grid(row = 19)


window.mainloop()