import turtle
def fractal(t,n,x,d,w):
    #TO DO ... 这个递归函数由你来完成 return
    if d==0:
        return
    else:
        for i in range(6):
            t.fd(x)
            fractal(t, n, x / 3, d - 1, w)
            t.lt(180)
            t.fd(x)
            t.rt(180-360/n)
        return fractal(t,n,x/3,d-1,w)

t=turtle.Pen()
t.color("skyblue")
t.speed(0)
t.hideturtle()
fractal(t,6,200,5,3)
turtle.mainloop()