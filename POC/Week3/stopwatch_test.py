import simplegui
 
count = 0
dot= 0
sec =0
minutes = 0

def format(t):
    a = t // 600
    b = ((t // 10 ) % 60) / 10
    c = ((t // 10 ) % 60) % 10
    d = t  % 10
    return str(a) +":"+ str(b) + str(c) +"."+ str(d)   

def format2(t):
    global dot, sec, minutes
    dot = (t % 10)
    if (t < 600):
        sec = (t // 10)
    else:
        sec = ((t % 600) // 10)
        minutes = (t // 600)
    if (sec < 10):
        str_sec = ('0' + str(sec))
    else:
        str_sec = str(sec)
    return ((((str(minutes) + ':') + str_sec) + '.') + str(dot))


def format3(run_time):
    global run_time_str, d_run_time
    bc_run_time = (run_time / 10)
    d_run_time = (run_time % 10)
    if (bc_run_time > 59):
        a_run_time = (bc_run_time / 60)
        bc_run_time = (bc_run_time - (60 * a_run_time))
    else:
        a_run_time = 0
    if (bc_run_time > 10):
        str_current_time = ((((str(a_run_time) + ':') + str(bc_run_time)) + '.') + str(d_run_time))
    else:
        str_current_time = (((((str(a_run_time) + ':') + '0') + str(bc_run_time)) + '.') + str(d_run_time))
    return str_current_time

def format4(t):
    if (t <= 9):
        A = '0'
        B = '0'
        C = '0'
    elif (len(str(t)) == 2):
        A = '0'
        B = '0'
        C = (t // 10)
    else:
        A = (t // 600)
        t = (t % 600)
        if (len(str(t)) == 3):
            B = ((t // 10) // 10)
            C = ((t // 10) % 10)
        elif (len(str(t)) < 3):
            if (t <= 59):
                B = '0'
                C = (t // 10)
            else:
                B = (((t % 60) // 10) % 10)
                C = (t // 10)
    D = (t % 10)
    return (((((str(A) + ':') + str(B)) + str(C)) + '.') + str(D))

def format5(t):
    a = (t // 600)
    b = (((t % 600) / 10) / 10)    
    c = '0'
    if (t > 10):
        c = str(t)[(-2)]
    d = str(t)[(-1)]
    formatedTime = (((((str(a) + ':') + str(b)) + c) + '.') + d)
    return formatedTime

def format6(t):
    D = (t % 10)
    tenth = (t / 10)
    if ((tenth >= 60) or (tenth <= 9)):
        B = 0
        C = (tenth % 10)
    else:
        B = (tenth / 10)
        C = (tenth % 10)
    A = (t / 600)
    return (((((str(A) + ':') + str(B)) + str(C)) + '.') + str(D))

def format7(t):
    return ((((str((t / 600)) + ':') + ('0' + str((t % 600)))[(-3):(-1)]) + '.') + str((t % 10)))

def time_handler():
    global count
    if(count > 1000):
        timer.stop()
        
    if(format7(count) is not format(count)):
        print count, format7(count), format(count)
    count += 1


timer = simplegui.create_timer(1, time_handler)

t = 0
timer.start()


TEST_CASES = [679,700,101,60, 10, 0]

