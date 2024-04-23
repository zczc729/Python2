import tkinter as tk
import tkinter.messagebox as mb

def button_click() :
    mb.showwarning("경고를 무시한 당신", "당신은 프로그램의 고수 입니다.")

# 메인창 생성
root = tk.Tk()
root.title("나의 첫 번 째 앱 프로그램") # 윈도우 제목 표시줄
root.geometry("200x100") # 윈도우 크기 설정
lab1 = tk.Label(root, text = "절대로 클릭 하지 마세요.")
lab1.pack(pady=10) # 화면에 보여준다.
btn1 = tk.Button(root, text = "클릭", command = button_click)
btn1.pack()

# 윈도우 실행 : 프로그램이 종료 될 때 까지 사용자 입력에 응답
root.mainloop()