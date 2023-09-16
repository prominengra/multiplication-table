import tkinter as tk
ui=tk.Tk()
ui.title('try to be pro')
ui.minsize(height=500,width=500)
def watch_this():
    nm=int(ju_input.get())
    if nm==0:
        output_label.configure(text='ผิดที่ไว้ใจ')
        return
    output= ''
    for i in range(1,13):
        output += str(nm) + ' x '+str(i)
        output += ' = ' + str(nm * i) + '\n'
    output_label.configure(text=output)
th_label=tk.Label(master=ui, text='Calculator')
th_label.pack(pady=20)

ju_input=tk.Entry(master=ui, width=15)
ju_input.pack()

ku_button=tk.Button(
    master=ui, text='Let go',
    command=watch_this, width=10,height=1
)
ku_button.pack()

output_label=tk.Label(master=ui,)
output_label.pack(pady=20)

ui.mainloop()