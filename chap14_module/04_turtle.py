import random
import turtle # 그래픽에 관련된 모듈

# 사각형 그리기

# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)
# turtle.done()

# 별 그리기

# for i in range(5):
#     turtle.forward(100)
#     turtle.right(144)
# turtle.done()

# 원 그리기

# turtle.begin_fill()
# turtle.fillcolor("skyblue")
# turtle.circle(100)
# turtle.end_fill()
# turtle.done()

# 랜덤으로 패턴 그리기

# for i in range(100):
#     turtle.speed(0)
#     turtle.forward(random.randint(5,100))
#     turtle.setheading(random.randint(0, 360))
# turtle.done()

# 마우스 클릭으로 그림 그리기

# def draw(x, y):
#     turtle.pendown() # 마우스 클릭한 위치로
#     turtle.goto(x, y) # 이동

# turtle.onscreenclick(draw)
# turtle.done()

# def draw(x, y):
#     turtle.goto(x, y)

# def clear_screen():
#     turtle.clear()

# turtle.speed(0)
# turtle.shape('turtle')
# turtle.color('skyblue')

# # c 키를 누를때 화면 지우기
# turtle.onkey(clear_screen, 'c')
# turtle.listen() # 키 이벤트 수신 시작
# turtle.onscreenclick(draw)

# turtle.mainloop()