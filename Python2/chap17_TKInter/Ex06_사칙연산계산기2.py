import tkinter as tk

def add_digit(digit) :
    entry_display.insert(tk.END, str(digit)) # tk.End = 맨 뒤로 이동 / 맨 끝에 숫자 추가

def add_operator(operator) :
    entry_display.insert(tk.END, operator) # 맨 끝에 연산자 추가

def calculate() :
    expression = entry_display.get()
    result = eval(expression) # Evaluate = 문자열로 표현된 수식을 계산
    entry_display.delete(0, tk.END) # 엔트리의 내용을 처믕부터 끝까지 제거
    entry_display.insert(tk.END, result)

def clear_screen() :
    entry_display.delete(0, tk.END)

# 윈도우 생성
root = tk.Tk()
root.title("Simple Calculator")

# 숫자 및 연산자 입력창
entry_display = tk.Entry(root, width=50)
entry_display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

for i in range(-1, 9):
    # 람다를 사용하지 않으면 버튼 생성 시 함수가 호출된다.
    # 버튼을 클릭할 때 마다 함수를 호출하려면 람다를 사용해야 한다.
    btn = tk.Button(root, text=str(i + 1), width=8, command=lambda digit=(i + 1) : add_digit(digit))

    if i == -1 : # 0 버튼 생성
        btn.grid(row=4, column=1, padx=5, pady=5)
    else: # 1 ~ 9번 버튼
        btn.grid(row=3 -(i // 3), column=i % 3,padx=5, pady=5)

# cls 버튼
cls_btn = tk.Button(root, text="cls", width=8, command=clear_screen)
cls_btn.grid(row=4, column=0, padx=5, pady=5)

# . 버튼
dot_btn = tk.Button(root, text=".", width=8, command=lambda : add_digit('.'))
dot_btn.grid(row=4, column=2, padx=5, pady=5)

# = 버튼
calc_btn = tk.Button(root, text="=", width=50, command=calculate)
calc_btn.grid(row=5, columnspan=4, padx=5, pady=5)

operators = ["+", "-", "*", "/"]

for i, oper in enumerate(operators) :
    btn = tk.Button(root, text=oper, width=10, command= lambda op = oper : add_operator(op))
    btn.grid(row=i + 1, column=3, padx=5, pady=5)

root.mainloop()