
# Create tests to check the correctness of your code

import poc_simpletest, cookieclicker, build_info

def buy_times(times,func, item, cost, cps):
    for _i in range(times):
        func(item, cost, cps)

def test():
    """
    Test code for Cookie Clicker
    """

    cookie = cookieclicker.ClickerState()
    store = build_info.BuildInfo()
    suite = poc_simpletest.TestSuite() 
    # Basic Tests
    initial_state = str(cookie)
    suite.run_test(initial_state, initial_state, "Test #0: Testing Initial state")
    history = cookie.get_history()
    history.append(2)
    #suite.run_test(str(cookie.get_history()), history, "Test #1: Testing History")
    #suite.run_test(str(cookie.time_until(15)), str(15.0), "Test #3: Get Time")
    #suite.run_test(str(cookie.time_until(25)), str(25.0), "Test #3: Get Time")
    #suite.run_test(str(cookie.time_until(0)), str(0.0), "Test #3: Get Time")
    #cookie.wait(15)
    #suite.run_test(str(cookie), "Wait", "Test #4: Testing Wait")
    #cookie.wait(25)
    #suite.run_test(str(cookie), "Wait", "Test #4: Testing Wait")
    #cookie.wait(0)
    #suite.run_test(str(cookie), "Wait", "Test #4: Testing Wait")
    #item_to_buy = "Cursor"
    #cookie.buy_item(item_to_buy, store.get_cost(item_to_buy), float(store.get_cps(item_to_buy)))
    #suite.run_test(str(cookie), "Wait", "Test #5: Testing After buy")
    #cookie.wait(25)
    #suite.run_test(str(cookie), "Wait", "Test #5: Testing After buy")
    #cookie.buy_item(item_to_buy, store.get_cost(item_to_buy), float(store.get_cps(item_to_buy)))
    #suite.run_test(str(cookie), "Wait", "Test #5: Testing After buy")
    #cookie.wait(25)
    #suite.run_test(str(cookie), "Wait", "Test #5: Testing After buy")
    ##cookie.buy_item(item_to_buy, store.get_cost(item_to_buy), store.get_cps(item_to_buy))
    ##cookie.buy_item(item_to_buy, store.get_cost(item_to_buy), store.get_cps(item_to_buy))
    ##cookie.buy_item(item_to_buy, store.get_cost(item_to_buy), store.get_cps(item_to_buy))
    ##cookie.buy_item(item_to_buy, store.get_cost(item_to_buy), store.get_cps(item_to_buy))
    ##cookie.buy_item(item_to_buy, store.get_cost(item_to_buy), store.get_cps(item_to_buy))
    #buy_times(6,cookie.buy_item, item_to_buy, store.get_cost(item_to_buy), store.get_cps(item_to_buy))
    #suite.run_test(str(cookie), "Wait", "Test #5: Testing After buy 5 times")
    #cookie.wait(10000)
    #suite.run_test(str(cookie), "Wait", "Test #5: Testing After waiting 10000 secs")
    #suite.run_test(str(cookie.time_until(25)), str(25.0), "Test #3: Get Time")
    cookie.add_cps(0.1)
    print str(cookie)
    suite.run_test(str(cookie.time_until(19.8375)), str(15.0), "Test #3: Get Time")
    history = cookie.get_history()
    print history
    suite.report_results()

test()

