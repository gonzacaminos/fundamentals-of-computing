# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [-2,-2]
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_vel = 0
paddle2_vel = 0
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
points = [0,0]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2] 
    h_velocity = random.randrange(120, 240) /60
    v_velocity = random.randrange(60, 180) /60
    if (direction == "LEFT"):
        ball_vel = [-h_velocity,-v_velocity]
    elif (direction == "RIGHT"):
        ball_vel = [h_velocity,-v_velocity] 


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global points
    points = [0,0]
    spawn_ball("LEFT")
    
def point_for(player):
    global points
    if player == 1:
        points[0] += 1
    if player == 2:
        points[1] += 1    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    canvas.draw_image(back, (300,200), (600, 400), (300,200), (600,400))
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw scores
    
    canvas.draw_text(str(points[0]), (WIDTH/2*1.5, 100), 60, '#464646', 'sans-serif')
    canvas.draw_text(str(points[1]), (WIDTH/2*0.5 -20, 100), 60, '#464646', 'sans-serif')

    # update ball
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
        
    if (ball_pos[1] <= BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
        
    elif (ball_pos[1] >= HEIGHT-BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]    
            
    # draw ball
    
    
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    canvas.draw_image(ball, (25,25), (50, 50), ball_pos, (50,50))

    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos -HALF_PAD_HEIGHT + paddle1_vel) >= 0 and (paddle1_pos +HALF_PAD_HEIGHT + paddle1_vel) <= HEIGHT:
        paddle1_pos += paddle1_vel
        
    if (paddle2_pos -HALF_PAD_HEIGHT + paddle2_vel) >= 0 and (paddle2_pos +HALF_PAD_HEIGHT + paddle2_vel) <= HEIGHT:
        paddle2_pos += paddle2_vel
    
    # draw paddles
    
    canvas.draw_polygon([(0, paddle1_pos - HALF_PAD_HEIGHT), (9, paddle1_pos - HALF_PAD_HEIGHT), (9, paddle1_pos + HALF_PAD_HEIGHT), (0, paddle1_pos + HALF_PAD_HEIGHT)], 1, 'Withe', "Withe")
    canvas.draw_polygon([(WIDTH-1, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH-9, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH-9, paddle2_pos + HALF_PAD_HEIGHT), (WIDTH, paddle2_pos + HALF_PAD_HEIGHT)], 1, 'Withe', "Withe")

    # determine whether paddle and ball collide  
    
    if (ball_pos[0] - BALL_RADIUS <= PAD_WIDTH ):
        
        if (ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT):
           
            ball_vel[0] += ball_vel[0]*0.1
            ball_vel[0] = - ball_vel[0] 
                     
            ball_vel[1] = ball_vel[1] + ball_vel[1]*0.1

        else:
            point_for(2)
            spawn_ball("RIGHT") 
        
    elif (ball_pos[0]  >= (WIDTH - PAD_WIDTH) - BALL_RADIUS ):
       
        if (ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT):

            ball_vel[0] += ball_vel[0]*0.1
            ball_vel[0] = - ball_vel[0] 
                     
            ball_vel[1] = ball_vel[1] + ball_vel[1]*0.1
            
        else:
            point_for(1)
            spawn_ball("LEFT")    
    
    print ball_vel
        
def keydown(key):
    
    global paddle1_vel, paddle2_vel, initial_dir, started
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 4
        
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 4
        
    if key == simplegui.KEY_MAP["up"]:
        
        paddle2_vel -= 4
        
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 4
          
def keyup(key):
    global paddle1_vel, paddle2_vel 
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel += 4
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel -= 4
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel += 4  
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel -= 4      



# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", new_game, 100)
ball = simplegui.load_image('http://s7.postimg.org/wiw2098af/ball.png')
back = simplegui.load_image('http://s27.postimg.org/6reru7ngz/back.jpg')

# start frame
new_game()
frame.start()
