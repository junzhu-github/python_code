import tkinter as tk

# ------------------------------------------------------
'''
window = tk.Tk()
window.title('my window')
window.geometry('500x300')

# 这里是窗口的内容

#l = tk.Label(window, text='OMG! this is TK!', bg='green', font=('Arial', 12), width=15, height=2)

var = tk.StringVar()
l = tk.Label(window, 
    textvariable = var,    # 标签的文字
    bg ='green',     # 背景颜色
    font = ('Arial', 15),     # 字体和字体大小
    width = 20, height = 10)  # 标签长宽

l.pack()    # 固定窗口位置


on_hit = False
def hit_me():
	global on_hit
	if on_hit == False:
		on_hit = True
		var.set('you hit me')
	else:
		on_hit = False
		var.set('...')

b = tk.Button(window,
	text = 'hit me',
	width = 15,height = 5,
	command = hit_me)
b.pack()


window.mainloop()
'''
# ------------------------------------------------------

window = tk.Tk()
window.title('my window')
window.geometry('500x300')

e = tk.Entry(window,show = None)
e.pack()


def insert_point():
	var = e.get()
	t.insert('insert',var)


def insert_end():
	var = e.get()
	t.insert('end',var)


b1 = tk.Button(window,
	text = 'insert point',
	width = 15,height = 2,
	command = insert_point)
b1.pack()

b2 = tk.Button(window,
	text = 'insert end',
	width = 10,height = 2,
	command = insert_end)
b2.pack()

t = tk.Text(window,height = 2)
t.pack()

window.mainloop()