# template for "Stopwatch: The Game"

import simplegui

# define global variables

counter = 0
stops_num = 0
success_stops = 0
running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    a = t // 600
    b = ((t // 10 ) % 60) / 10
    c = ((t // 10 ) % 60) % 10
    d = t  % 10
    return str(a) +":"+ str(b) + str(c) +"."+ str(d)    
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    timer.start()
    global running
    running = True
    
def stop():
    
    global running 
    
    if running: 
        running = False
        timer.stop()
        global stops_num, success_stops
        stops_num +=1

        if ((counter// 10 ) % 60) / 10 > 0 and ((counter // 10 ) % 60) % 10 == 0:
            success_stops +=1            
        
    
def reset():    
    timer.stop()
    global counter, stops_num, success_stops, running
    counter = 0
    stops_num = 0
    success_stops = 0 
    running = 0
    
# define event handler for timer with 0.1 sec interval

def time_handler():
    global counter
    counter += 1
    print counter

# extra counters

def extra_counters():
    
    return str(stops_num) +"/"+ str(success_stops)

# define draw handler

def draw(canvas):
    canvas.draw_text(format(counter), (170, 200), 30, 'white')
    canvas.draw_text(extra_counters(), (360, 40), 20, 'white')

# create frame

frame = simplegui.create_frame('Frame', 400, 400)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, time_handler)

# register event handlers

frame.add_button("Start", start, 120)
frame.add_button("Stop", stop, 120)
frame.add_button("Reset", reset, 120)


# start frame
frame.start()

# Please remember to review the grading rubric
