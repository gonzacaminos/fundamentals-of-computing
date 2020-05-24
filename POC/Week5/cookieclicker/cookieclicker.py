"""
Cookie Clicker Simulator
"""

#import simpleplot

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)

import build_info as provided
import math
# Constants
SIM_TIME = 10000000000.0
#SIM_TIME = 100.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):

        self.total_cookies = 0.0
        self.current_cookies = 0.0
        self.time = 0.0
        self.cps = 1.0
        self.history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """

        return str( ("Total CK:", self.total_cookies, "Current CK:", self.get_cookies(), "Time:", self.get_time(), "CPS:", self.get_cps()) )

    def get_total_cookies(self):
        """ 
        Gets the total of cookies generated over the game
        """
        return self.total_cookies

    def add_total_cookies(self, cookies):
        """ 
        Adds to the total amount of cookies
        """

        self.total_cookies += cookies

    def set_cookies(self,cookies):
        """
        Sets current amount of cookies
        """

        self.current_cookies = cookies   

    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return float(self.current_cookies)
    
    def add_cps(self, cps):
        """
        Add to the current CPS
        """
        self.cps += cps


    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return float(self.cps)
    
    def add_time(self,time):
        """"
        Add to the time of the game
        """
        self.time += float(time)

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return float(self.time)
    
    def add_history(self, item, cost_item):
        self.history.append((self.get_time(), item, cost_item, self.get_total_cookies()))

        return

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self.history[:]

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        remaining = cookies - self.get_cookies()
        
        return float(int(math.ceil(remaining/self.get_cps())))
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if(time > 0):

            self.add_time(time)
            cookies = self.get_cps() * time
            self.set_cookies(self.get_cookies() + cookies)
            self.add_total_cookies(cookies)

        return    
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if(self.get_cookies()>=cost):
            self.set_cookies(self.get_cookies()-cost)
            self.add_cps(additional_cps)
            self.add_history(item_name, cost)


        return
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    clicker = ClickerState()
    build_info = build_info.clone()
    time = 0

    while time <= duration:
        time = clicker.get_time()
        to_buy = strategy(clicker.get_cookies(), clicker.get_cps(), clicker.get_history(), duration -time , build_info)
        
        if(to_buy == None):
            break

        cost = build_info.get_cost(to_buy)
        time_until = clicker.time_until(cost)
        if(time+time_until > duration):
            break  

        clicker.wait(time_until)
        clicker.buy_item(to_buy, cost, build_info.get_cps(to_buy))
        build_info.update_item(to_buy)


    time_left = duration - clicker.get_time()

    if(time_left > 0.0):
        # if there's time left let 'em bake the last ones
        clicker.wait(time_left)

    #print clicker.get_history()

    return clicker


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    return None

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    return None

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
run()
    

