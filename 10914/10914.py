from browser import document, window, alert

s_speed=1/90
base=1150
pos=[100,100]
b_speed=0
gravity=9.8
history=[]

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)
  def setup():
    p.createCanvas(600, 1280)  # 캔버스 크기
    p.background(0)  # 검정 배경
    p.rectMode(p.CENTER)  # 입력한 좌표를 도형의 중심으로 하여 그리도록 설정

  def draw():
    global b_speed, gravity
    p.background(0)  # 화면 초기화

    """바닥 그리기"""
    p.stroke(255)  # 흰색 윤곽선
    p.strokeWeight(2)  # 펜 굵기 5
    p.line(0, base, 600, base)  # 바닥 선
    
    """공 위치 구하기"""
    # 속도 = 가속도 x 시간
    b_speed += gravity*s_speed   # 속도에 가속도 더하기
    
    # 거리 = 속도 x 시간
    pos[1] += b_speed  # 위치에 속도 더하기
    
    if pos[1] >= base:  # 혹시라도 공이 바닥보다 아래로 내려간다면
      pos[1] = base  # 바닥에 멈추기
      b_speed = 0  # 멈추기
    
    history.append((pos[0], pos[1]))  # 현재 위치 기록하기 (궤적)

    """공 그리기"""
    p.fill('red')  # 공 색상 설정
    p.ellipse(pos[0], pos[1], 50)# 타원(ellipse) 그리기

    """공 궤적(이동 기록) 그리기"""
    p.beginShape();  # 곡선 그리기 시작 (궤적)
    for i in history:  # 모든 궤적에 대하여, i: [x좌표, y좌표]
      p.vertex(i[0], i[1]);  # 점 찍기
    p.endShape();  # 곡선 그리기 끝

    """정보 나타내기"""
    p.textSize(32)  # 글씨 크기 설정
    p.textFont('Arial')
    p.text('위치: (%3.1f, %03.01f)' % (pos[0], pos[1]), 300, 50)
    p.text('속도: %3.1f' % b_speed, 300, 100)
    p.text('가속도: ' + str(gravity), 300, 150)
    p.text('시뮬레이션 속도: 1/90' , 300, 200)
    
  p.setup = setup
  p.draw = draw

myp5 = window.p5.new(sketch)
