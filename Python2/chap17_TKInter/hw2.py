import tkinter as tk


def clr_num():
    result_label.config(text="")

root = tk.Tk()
root.title("사칙 연산 계산기")
root.geometry("600x400")
root.config(bg="lightblue")

result_label = tk.Label(root, padx=5, pady=5)
result_label.grid(row=0, columnspan=4, padx=5, pady=5)

for i in range(10) :
    btn_i = tk.Button(root, text=i)
    col_list = [2, 0, 1]

    if i == 0:
        btn_i.grid(row=4, column=1, padx=5, pady=5)
    else :
        btn_i.grid(row=(4-((i+2)//3)), column=col_list[i%3], padx=5, pady=5)


operator = ["+", "-", "x", "/"]
for i in range(len(operator)) :
    oper_btn = tk.Button(root, text=operator[i])
    oper_btn.grid(row=i+1, column=3, padx=5, pady=5)

clr_btn = tk.Button(root, text="clr", command=clr_num)
clr_btn.grid(row=4, column=0, padx=5, pady=5)

point_btn = tk.Button(root, text=".")
point_btn.grid(row=4, column=2, padx=5, pady=5)

root.mainloop()