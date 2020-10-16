import turtle as trtl

# draws a curve left 90 degrees
trtl.pendown()
for i in range(6):
  trtl.forward(10)
  trtl.left(15)
trtl.penup()

''''
draws the x- and y-axes 100 pixels long going in each  direction
'''
def draw_axes():
  # centers at origin
  trtl.goto(0,0)
  trtl.pendown()
  # draws the y-axis
  trtl.forward(100)
  trtl.backward(200)
  trtl.forward(100)
  trtl.left(90)
  # draws the x- axis
  trtl.forward(100)
  trtl.backward(200)
  trtl.pendown()
  # centers at orgin
  trtl.goto(0,0)

draw_axes()