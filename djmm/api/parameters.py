import random
import math


class CreateTestParameters(object):

    def __init__(self):
        self.broker()
        self.buffer_test()
        self.buystop_percentage()
        self.diversify()
        self.duration()
        self.hold()
        self.margin()
        self.positions() # Calculate before quantity()
        self.profitlimitpercent()
        self.quantity() # Calculate before startcash()
        self.position()
        self.select_r()
        self.sellstoppercentage()
        self.sharebuffer()
        self.startquote() # Calculate before startcash()
        self.startcash()
        self.stoplosspercentage()
        self.swing()
        self.trailingpercentage()

    def broker(self):
        self.brokers = ("etrade", "free", "tradier")
        self.broker_rand = random.choice(self.brokers)
        self.broker = self.broker_rand

    def buffer_test(self):
        self.buffer_test_min = 0
        self.buffer_test_max = 5
        self.buffer_test_rand = random.randint(self.buffer_test_min, self.buffer_test_max)
        self.buffer_test = self.buffer_test_rand

    def buystop_percentage(self):
        self.buystop_percentage_min = 100
        self.buystop_percentage_max = 1000
        self.buystop_percentage_rand = random.randint(self.buystop_percentage_min, self.buystop_percentage_max)
        self.buystop_percentage = self.buystop_percentage_rand

    def diversify(self):
        self.diversify_min = "no"
        self.diversify_max = "yes"
        self.diversify_rand = random.choice([self.diversify_min, self.diversify_max])
        self.diversify = self.diversify_rand

    def duration(self):
        self.duration_min = 10
        self.duration_max = 240
        self.duration_rand = random.randint(self.duration_min, self.duration_max)
        self.duration = self.duration_rand

    def hold(self):
        self.hold_min = "no"
        self.hold_max = "yes"
        self.hold_rand = random.choice([self.hold_min, self.hold_max])
        self.hold = self.hold_rand

    def margin(self):
        self.margin_min = "no"
        self.margin_max = "yes"
        self.margin_rand = random.choice([self.margin_min, self.margin_max])
        self.margin = self.margin_rand

    def position(self):
        self.position_min = 1
        self.position_max = 9
        self.position_rand = random.randint(self.position_min, self.position_max)
        self.position = self.position_rand
        if(self.position >= self.quantity):
            self.position = self.quantity - 1
        if(self.position >= self.positions):
            self.position = self.positions - 1

    def positions(self):
        self.positions_min = 1
        self.positions_max = 9
        self.positions_rand = random.randint(self.positions_min, self.positions_max)
        self.positions = self.positions_rand

    def profitlimitpercent(self):
        self.profitlimitpercent_min = 110
        self.profitlimitpercent_max = 10000
        self.profitlimitpercent_rand = random.randint(self.profitlimitpercent_min, self.profitlimitpercent_max)
        self.profitlimitpercent = self.profitlimitpercent_rand

    def quantity(self):
        self.quantity_min = 2
        if(self.positions > 20):
            self.quantity_max = self.positions + 1
        else:
            self.quantity_max = 20
        self.quantity_rand = random.randint(self.quantity_min, self.quantity_max)
        self.quantity = self.quantity_rand

    def select_r(self):
        self.select_r_min = "no"
        self.select_r_max = "yes"
        self.select_r_rand = random.choice([self.select_r_min, self.select_r_max])
        self.select_r_rand = "no"
        self.select_r = self.select_r_rand

    def sellstoppercentage(self):
        self.sellstoppercentage_min = 1
        self.sellstoppercentage_max = 100
        self.sellstoppercentage_rand = random.randint(self.sellstoppercentage_min, self.sellstoppercentage_max)
        self.sellstoppercentage = self.sellstoppercentage_rand

    def sharebuffer(self):
        self.sharebuffer_min = 1
        self.sharebuffer_max = 2000
        self.sharebuffer_rand = random.randint(self.sharebuffer_min, self.sharebuffer_max)
        self.sharebuffer = self.sharebuffer_rand

    def startcash(self):
        min = 400
        qmin = math.ceil(self.startquote * 30)
        self.startcash_min = min if (qmin < min) else qmin
        self.startcash_max = 10000
        self.startcash_rand = random.randint(self.startcash_min, self.startcash_max)
        self.startcash = self.startcash_rand

    def startquote(self):
        min = 0.80
        max = 40
        self.startquote_min = min
        self.startquote_max = max
        min_100 = min * 100
        max_100 = max * 100
        self.startquote_rand = random.randint(min_100, max_100) / 100
        self.startquote = self.startquote_rand

    def stoplosspercentage(self):
        self.stoplosspercentage_min = 1
        self.stoplosspercentage_max = 100
        self.stoplosspercentage_rand = random.randint(self.stoplosspercentage_min, self.stoplosspercentage_max)
        self.stoplosspercentage = self.stoplosspercentage_rand

    def swing(self):
        self.swing_min = "no"
        self.swing_max = "yes"
        self.swing_rand = random.choice([self.swing_min, self.swing_max])
        self.swing = self.swing_rand

    def trailingpercentage(self):
        self.trailingpercentage_min = 1
        self.trailingpercentage_max = 100
        self.trailingpercentage_rand = random.randint(self.trailingpercentage_min, self.trailingpercentage_max)
        self.trailingpercentage = self.trailingpercentage_rand

# a = CreateTestParameters()
# print(a.stoplosspercentage)
