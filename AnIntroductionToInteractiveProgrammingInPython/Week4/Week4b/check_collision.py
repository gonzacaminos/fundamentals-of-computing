
import simplegui

point = [10,20]
rect = [[50,50], [180,50], [180,140], [50,140]]

def run(): 
    
    #while (point[1] <= rect[0][1] or point[1] <= rect[2][1]):
        
        print "Run"
        print ""
        
        if( (point[0] >= rect[0][0] and point[0] <= rect[1][0]) and (point[1] >= rect[0][1] and point[1] < rect[2][1])):
             print "collide"
             timer.stop()
        else:
             print "not collide"
                
                
        point[0] += 3
        point[1] += 0.7        
        
def draw_handler(canvas):
     canvas.draw_polygon([ rect[0], rect[1], rect[2], rect[3]], 1, 'Yellow', 'Orange')
     canvas.draw_point(point, 'Red')
  

frame = simplegui.create_frame("canvas", 400,400)
frame.set_draw_handler(draw_handler)


timer = simplegui.create_timer(100, run)

frame.start()
           
timer.start()
           