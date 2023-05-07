from browser import document, window, alert


g=9.80665
speed=0.15

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)
  class Body:
    def __init__(self, x, y, radius, acceleration):
      self.x=x
      self.y=y
      self.radius=radius
      self.acceleration=acceleration
      self.velocity=0
  
    def update(self):
      self.velocity+=self.acceleration*speed
      self.y+=self.velocity*speed
      print(self.x,self.y,self.velocity,self.acceleration)
  
    def display(self):
      p.background(255)
      p.noStroke()
      p.fill('purple')
      p.circle(self.x,self.y,self.radius)
  
  def setup():
      p.createCanvas(500, 500)
      p.background(255)
      p.rectMode(p.CENTER)

  def draw():
    body.update()
    body.display()

  body=Body(250,0,30,g)
  p.setup = setup
  p.draw = draw
      
myp5 = window.p5.new(sketch)