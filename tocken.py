class Voucher:
    def __init__(self,id):
        self.availability=False
        self.id = id

        counter = 0
        def disable_coupon():
            self.availability = False
        def available_coupon():
            self.availability = True
class User:
    def __init__(self,name):
        self.name = name

class Admin:
    def __init__(self,name,id):
        self.name = name
        self.id = self.id

    def createCoupoun(self,id,limit):
        # create coup
        new_coupon = Coupon(id,limit)


        pass
class Coupon:
    limit = 0
    def __init__(self, coupon_id, rules, overall_limit, per_user_limit, expiry_date ):
        self.coupon_id = coupon_id
        self.rules = rules
        self.overall_limit = overall_limit
        self.per_user_limit = per_user_limit
        self.expiry_date = expiry_date
        self.active = True


        self.used_count = 0
        self.user_usage = {}

    def is_valid(self):
        pass


# class Game:
