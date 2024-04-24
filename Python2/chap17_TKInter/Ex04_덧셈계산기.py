import tkinter as tk

def plus_result_btn() :
    try :
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        result_label.config(text=f"{num1} + {num2} = {num1 + num2}")
    except ValueError :
        result_label.config(text = "숫자 데이터만 입력 가능합니다.")



root = tk.Tk() # 메인창 생성
root.title("간단한 덧셈 계산기")
root.geometry("400x100")
root.config(bg="lightblue")


entry_num1 = tk.Entry(root, width=10)
entry_num1.grid(row=0, column=0, padx=10, pady=10) # 격자 무늬로 나눠 화면에 띄운다


entry_num2 = tk.Entry(root, width=10)
entry_num2.grid(row=0, column=1, padx=10, pady=10) # 격자 무늬로 나눠 화면에 띄운다

plus_btn = tk.Button(root, text = "더하기", command=plus_result_btn)
plus_btn.grid(row=0, column=2, padx=10, pady=10)

result_label = tk.Label(root, width=30, height=2)
result_label.grid(row=1, columnspan=3) 

root.mainloop() # 윈도우 실행