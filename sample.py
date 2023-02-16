from turtle import Screen,Turtle
import time
import random
screen = Screen()
screen.setup(width = 600,height = 600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
Up = 90
Down = 270
Right = 0
Left = 180

# creating snake
class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
            
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segments.append(new_segment)
        
    def extend(self):
        self.add_segment(self.snake_segments[-1].position())
        
    def move_snake(self):
        for seg in range(len(self.snake_segments)-1,0,-1):
            x_cor = self.snake_segments[seg-1].xcor()
            y_cor = self.snake_segments[seg-1].ycor()
            self.snake_segments[seg].goto(x_cor,y_cor)
        self.head.forward(20)
        
    def up(self):
        if(self.head.heading()!= Down):
            self.head.setheading(Up)
            
    def down(self):
        if(self.head.heading()!= Up):
            self.head.setheading(Down)
            
    def right(self):
        if(self.head.heading()!= Left):
            self.head.setheading(Right)
            
    def left(self):
        if(self.head.heading()!= Right):
            self.head.setheading(Left)
			
class Food(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color("blue")
		self.penup()
		self.shapesize(stretch_wid = 0.5,stretch_len = 0.5)
		self.speed("fastest")
		
	def refresh(self):
		random_x = random.randint(-280,280)
		random_y = random.randint(-280,280)
		self.goto(random_x,random_y)
		
		
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update()
        
    def increase(self):
        self.score+=5
        self.clear()
        self.update()
        
    def update(self):
        self.write(f"score:{self.score}",align = "center",font = ("Arial",24,"normal"))
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align = "center",font = ("Arial",24,"normal"))

snake_obj = Snake()
food = Food()
score = Scoreboard()
screen.onkey(snake_obj.up,"Up")
screen.onkey(snake_obj.down,"Down")
screen.onkey(snake_obj.left,"Left")
screen.onkey(snake_obj.right,"Right")
game_is_on = True

while(game_is_on):
    screen.update()
    time.sleep(0.1)
    snake_obj.move_snake()
    if(snake_obj.head.distance(food)<15):
        snake_obj.extend()
        food.refresh()
        score.increase()
        
    if(snake_obj.head.xcor()>280 or snake_obj.head.xcor()<-280 or snake_obj.head.ycor()>280 or snake_obj.head.ycor()<-280):
        game_is_on = False
        score.game_over()
        
    for seg in snake_obj.snake_segments:
        if(snake_obj.head==seg):
            pass
            
        elif(snake_obj.head.distance(seg)<10):
            game_is_on = False
            score.game_over()
            
            
            
            
screen.exitonclick()