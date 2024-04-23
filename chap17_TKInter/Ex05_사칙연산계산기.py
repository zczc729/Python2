import tkinter as tk

# 버튼, 라벨 등등 모두 위젯이라 한다.
# ttk 모듈 : tkinter의 확장판, 기본 위젯을 확장하고 향상시킨 모듈
from tkinter import ttk # Theme tk

def calculator() :
    try :
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        # oper = operator_combo.get()
        oper = select_oper.get()

        result = 0
        if oper == "+" :
            result = num1 + num2
        elif oper == "-" :
            result = num1 - num2
        elif oper == "x" :
            result = num1 * num2
        elif oper == "/" :
            result = num1 / num2
            
        result_label.config(text=f"연산 결과 = {result:.6f}")
    except ValueError :
        result_label.config(text="숫자 데이터만 입력 받을수 있습니다.")
    except ZeroDivisionError :
        result_label.config(text="0으로는 나눌수 없습니다.")

root = tk.Tk() # 메인창 생성
root.title("사칙 연산 계산기")
root.geometry("400x150")
root.config(bg="lightblue")

entry_num1 = tk.Entry(root, width=10)
entry_num1.grid(row=0, column=0, columnspan=2,padx=5, pady=5)

entry_num2 = tk.Entry(root, width=10)
entry_num2.grid(row=0, column=2, columnspan=2, padx=5, pady=5)

# 연산자 선택을 위한 콤보 박스 생성
# operators = ["+", "-", "x", "/"]
# operator_combo = ttk.Combobox(root, values=operators, width=5)
# operator_combo.current(0) # 디폴트 값이 0번째 값으로 설정
# operator_combo.grid(row=0, column=2, padx=5, pady=5)

# 연산자 선택을 위한 라디오 버튼 생성
operators = ["+", "-", "x", "/"]
select_oper = tk.StringVar() # 선택된 콤보 박스의 문자열을 얻어온다.
print("select : ",select_oper)

for i, oper in enumerate(operators) :
    radio_btn = ttk.Radiobutton(root, text=oper, value=oper, variable=select_oper)
    radio_btn.grid(row=1, column=i, padx=5, pady=5)


# 게산 버튼 생성
oper_btn = tk.Button(root, text="계산", command=calculator, width=28)
oper_btn.grid(row=2, columnspan=3, padx=5, pady=5)

# 게산 결과를 출력할 레이블 생성
result_label = tk.Label(root, width=28)
result_label.grid(row=3, columnspan=3, padx=5, pady=5)


root.mainloop() # 윈도우 실행