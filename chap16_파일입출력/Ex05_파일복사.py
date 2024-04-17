# t : 텍스트 모드 : 단순 글자만 저장이 가능 하다. t는 생략 가능하다.
# b : binary 모드 : 2진수로 이루어진 파일, 이미지, 영상, 사운드 등 (내부적으로 변동이 없음. 컴퓨터가 인식하는 2진법 형태로 저장함)

with open("myPicture.jpg", "rb") as fR, open("copy.jpg", "wb") as fW:
    # fW.write(fR.read()) 
    lines = fR.read()
    fW.write(lines)