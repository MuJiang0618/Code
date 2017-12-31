from graphics import*
win=GraphWin("Click me!")
for i in range(10):
	p=win.getMouse()    #注意大小写
	print(p.getX(),p.getY())    #注意getX和getY都是函数,要加()   