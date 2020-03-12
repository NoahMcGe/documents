import turtle

def circlefill(t):
	print("circle")
	t.down()
	t.begin_fill()
	t.color("#ff0000")
	for i in range (1,20):
		t.forward(10)
		t.rt(18)
	t.end_fill()
	
def circle(t):
	print("circle")
	t.down()
	t.color("#ff0000")
	for i in range (1,20):
		t.forward(10)
		t.rt(18)
		
def matrix():
	print("matrix")

def square(t,x,y):
	t.pendown()
	t.begin_fill()
	tcolor = "#0000ff"
	t.color(tcolor)
	t.forward(70)
	t.rt(90)
	t.forward(70)
	t.rt(90)
	t.forward(70)
	t.rt(90)
	t.forward(70)
	t.end_fill()

def arcR(t,x,y,l,tn,h):
	#x, y l(length) tn(turn value)
	t.down()
	t.seth(h)
	for i in range (1,10):
		t.forward(l)
		t.rt(tn)
	
def main():
	x = -400; y = 0
	w = turtle.Screen()
	w.setup(1000, 700)
	w.clear()
	w.bgcolor("#ffffff")
	t = turtle.Turtle()
	t.penup
	t.goto(0,0)
	tcolor = "#ff0000";t.color(tcolor)
	t.forward(100);t.back(100)
	arcR(t,x,y,40,13,0)
	tcolor = "#00ff00";t.color(tcolor)
	t.forward(100);t.back(100)
	arcR(t,x,y,40,13,90)
	tcolor = "#0000ff";t.color(tcolor)
	t.forward(100);t.back(100)
	arcR(t,x,y,40,13,180)
	tcolor = "#00ffff";t.color(tcolor)
	t.forward(100);t.back(100)
	arcR(t,x,y,40,13,270)
	'''
	t.speed(5)
    t.color("#000000")
    t.forward(50)
    square(t,x,y)
    t.penup()
    t.goto(-100,100)
    circlefill(t)
	'''
	w.exitonclick()

if __name__ == '__main__':
	main()
	
'''
#apt install python3-tk
	


wn = turtle.Screen()   # create a turtle
t = turtle.Turtle()
t.color('green')      # set the color
t.forward(50)         # draw a green line of leng
t.up()                # lift up the tail
t.forward(50)         # move forward 50 without drawing
t.right(90)           # change direction to the right, left works too
t.down()              # put the tail down
t.backward(100)       # draw a green line 100 units long
wn.exitonclick()
'''
