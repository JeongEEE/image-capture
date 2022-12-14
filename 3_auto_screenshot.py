# 화면 자동으로 스크린샷 찍는 로직

from PIL import ImageGrab
import time

time.sleep(5) # 5초 대기

for i in range(1, 11): # 2초 간격으로 10개 이미지 저장
	img = ImageGrab.grab() # 현재 스크린 이미지를 가져옴
	img.save("image{}.png", format(i)) # 파일로 저장
	time.sleep(2)
