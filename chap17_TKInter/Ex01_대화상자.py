import tkinter.messagebox as mb

answer = mb.askyesno("질문", "파이썬은 배우기 쉽나요?")

if answer == True :
    mb.showinfo("동의", "Life is too short, you need Python!")
else :
    mb.showinfo("비동의", "아직 익숙하지 않아서 그래요! 힘내세요!")