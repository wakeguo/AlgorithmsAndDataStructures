import turtle
import random


def tree(branchLen, t):
    if branchLen > 5:
        step = random.randrange(15, 29)
        angle = random.randrange(10, 45)

        if branchLen < 30:
            t.color('green')
        # t.pensize(branchLen/5)
        t.pensize(max(4, branchLen/step*5))
        t.fd(branchLen)
        t.right(angle)
        tree(branchLen-15, t)
        t.left(2*angle)
        tree(branchLen-15, t)

        t.right(angle)
        t.bk(branchLen)
        t.color('brown')




def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('brown')
    tree(95, t)
    myWin.exitonclick()


main()