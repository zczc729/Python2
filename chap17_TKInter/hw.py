import tkinter as tk

def cal_btn_click(cal_num) :
    print(cal_num)
    try :
        if cal_num == 1 :
            num1 = float(enter_num1.get())
            num2 = float(enter_num2.get())

            if num1.is_integer() and num2.is_integer():
                num1 = int(num1)
                num2 = int(num2)
                result_label.config(text=f"결과 : {num1} + {num2} = {num1 + num2}")
            else :
                result_label.config(text=f"결과 : {num1} + {num2} = {num1 + num2}")

        elif cal_num == 2 :
            num1 = float(enter_num1.get())
            num2 = float(enter_num2.get())

            if num1 < num2 :
                result_label.config(text="결과값은 음수가 나올수 없습니다.")
            else :
                if num1.is_integer() and num2.is_integer():
                    num1 = int(num1)
                    num2 = int(num2)
                    result_label.config(text=f"결과 : {num1} - {num2} = {num1 - num2}")
                else :
                    result_label.config(text=f"결과 : {num1} - {num2} = {num1 - num2}")

        elif cal_num == 3 :
            num1 = float(enter_num1.get())
            num2 = float(enter_num2.get())

            if num1.is_integer() and num2.is_integer():
                num1 = int(num1)
                num2 = int(num2)
                result_label.config(text=f"결과 : {num1} X {num2} = {num1 * num2}")
            else :
                result_label.config(text=f"결과 : {num1} X {num2} = {num1 * num2}")

        elif cal_num == 4 :
            num1 = float(enter_num1.get())
            num2 = float(enter_num2.get())

            if num1 < num2 :
                result_label.config(text="작은 수에서 큰 수를 나눌 수 없습니다.")
            else :
                if num1.is_integer() and num2.is_integer():
                    num1 = int(num1)
                    num2 = int(num2)
                    num3 = num1 / num2

                    if num3.is_integer():
                        result_label.config(text=f"결과 : {num1} X {num2} = {int(num1 / num2)}")
                    else :
                        result_label.config(text=f"결과 : {num1} X {num2} = {num1 / num2}")
    except ValueError :
        result_label.config(text="잘못 입력 하셨습니다.")



root = tk.Tk()
root.title("사칙 연산 계산기")
root.geometry("400x300")
root.config(bg="pink")

enter_num1 = tk.Entry(root, width=10)
enter_num1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

enter_num2 = tk.Entry(root, width=10)
enter_num2.grid(row=0, column=2, columnspan=2, padx=5, pady=5)

plus_btn = tk.Button(root, text="+", command=lambda : cal_btn_click(1))
plus_btn.grid(row=1, column=0, padx=5, pady=5)

minus_btn = tk.Button(root, text="-", command=lambda : cal_btn_click(2))
minus_btn.grid(row=1, column=1, padx=5, pady=5)

mul_btn = tk.Button(root, text="X", command=lambda : cal_btn_click(3))
mul_btn.grid(row=1, column=2, padx=5, pady=5)

div_btn = tk.Button(root, text="/", command=lambda : cal_btn_click(4))
div_btn.grid(row=1, column=3, padx=5, pady=5)

result_label = tk.Label(root, text="결과 : ")
result_label.grid(row=2, columnspan=4, pady=5)

root.mainloop()