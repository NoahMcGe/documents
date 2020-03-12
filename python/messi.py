import turtle
def circlefill(t,x,y,r):
	print("one circle")
	t.penup()
	t.goto(x-r,y+r+70)
	t.down()
	t.begin_fill()
	t.color("#ffffff")
	for i in range (1,40):
		t.forward(40)
		t.rt(9)
	t.end_fill()

def ball(t):
	s = 50
	circlefill(t,0,0,s)
	h = [2,5,8,7,2,2]
	k = [3,4,1,-4,-3,3]
	x = 0; y = 0
	i = 0
	t.penup()
	s = 20
	t.begin_fill()
	t.color("#000000")
	while (i < 6):
		x = x
		t.goto(h[i]*s,k[i]*s)
		t.down()
		i = i + 1
	t.end_fill()
	t.penup()
	t.goto(-100,0)
	t.write("Messi", font=("Arial", 24, "normal"))
	
def main():
	w = turtle.Screen()
	w.setup(800, 800)
	w.clear()
	w.bgcolor("#ff2200")
	t = turtle.Turtle()
	ball(t)
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
