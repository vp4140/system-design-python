class Coupon:
    def __init__(self,id,rules={},date =None):
        self.coupon_id = id
        self.coupon_rules = {}
        self.expiry_date = date
        self.active = False

class User:
    def __init__(self,user_id,user_name):
        self.user_id = user_id,
        self.user_name = user_name

class Admin:
    def __init__(self,user_id,user_name):
        self.user_id = user_id,
        self.user_name = user_name

class Voucher:
    def __init__(self,id, asssigned:User):
        self.voucher_id = id
        self.asssigned = asssigned

class VocherManagement:
    def __init__(self):

        self.voucher_list :[Voucher]= []
        self.coupon_list:[Coupon] = []

    def available_Vouchers(self,voucher:Voucher):
        #Users can get avaiable vochers
        list_id = []
        for ele in self.voucher_list:
            list_id.append(ele.voucher_id)
        return list_id
    def use_Voucher(self,vocher_id):
        for ele in self.voucher_list:
            if self.voucher_list





