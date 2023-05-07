#p5.js는 javascript언어를 사용하여 그림을 그리고, 에니메이션을 만들고, 사용자와 상호작용할 수 있도록 해주는 javascript의 부품 중 하나이다. pyp5js는 이 p5.js를 파이썬에서 사용할 수 있게 해주는 도구이다.
from browser import document, window, alert
def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)
  screen_width = 700
  screen_height = 500
  x = []
  y = []
  dy = []
  dx = []
  g = 9.8
  
  def setup():
    screen_width = 700
    screen_height = 500
    p.createCanvas(screen_width, screen_height)
  
  def draw():
    p.background(200)
    p.noStroke()
    p.fill(0)
    p.rect(0, screen_height - 100, screen_width, 100)
    p.fill('orange')
    
    for i in range(len(x)):
      dy[i] += g * 0.1
      y[i] += dy[i]
      x[i] += dx[i]
      if y[i] > screen_height - 100:
        y[i] = screen_height - 100
        dy[i] = 0
        dx[i] = 0
      p.circle(x[i],y[i],30)
  
  
  def mousePressed(self):
    p_x = 200
    x.append(p.mouseX)
    y.append(p.mouseY)
    dy.append(p.mouseY - p.pmouseY)
    dx.append(p.mouseX - p.pmouseX)
  
  p.setup = setup
  p.draw = draw
  p.mousePressed = mousePressed
  
    
myp5 = window.p5.new(sketch)
