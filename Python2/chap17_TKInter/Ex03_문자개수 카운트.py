import tkinter as tk

def entry_char_count() :
    str = entry_box.get() # 엔트리 박스의 내용을 가져온다.
    str_len = len(str) # 문자열의 길이를 구한다.

    entry_label.config(text = f"Entry 문자열의 개수 : {str_len}")

def text_char_count() :
    # 1.0 : 첫 줄의 첫 글자 ~ 마지막 글자
    # 2.3 : 두 번 째 줄의 세 번 째 글자 ~ 마지막 글자
    # 8.0 : 여덟번 째 줄의 첫 번 째 글자
    str = text_box.get(1.0, tk.END)
    str_len = len(str)

    text_label.config(text = f"Text 문자열의 개수 : {str_len - 1}")



root = tk.Tk() # 메인창 생성

root.title("문자 개수 카운트")
root.geometry("500x500")
root.config(bg="lightblue")

entry_box = tk.Entry(root, width=60)# 한 줄 짜리 텍스트 상자
entry_box.pack(pady = 10) # Entry 화면에 띄운다

text_box = tk.Text(root, width=60) # 여러 줄을 입력 받을 수 있는 텍스트 상자
text_box.pack() # Text 화면에 띄우다

entry_button = tk.Button(root, text = "Entry 문자의 개수를 카운트", command = entry_char_count)
entry_button.pack(pady = 10)

text_btn = tk.Button(root, text = "Text 문자의 개수 카운트", command = text_char_count)
text_btn.pack()

entry_label = tk.Label(root, width = 30, )
entry_label.pack(pady = 10)

text_label = tk.Label(root, width = 30)
text_label.pack()

root.mainloop() # 윈도우를 실행