from datetime import datetime

# Coupon Class
class Coupon:
    def __init__(self, coupon_id, rules, overall_limit, per_user_limit, expiry_date):
        self.coupon_id = coupon_id
        self.rules = rules  # Rules as a dictionary, e.g., {"age": ">18", "cart_value": ">1000"}
        self.overall_limit = overall_limit
        self.per_user_limit = per_user_limit
        self.expiry_date = expiry_date
        self.active = True
        self.used_count = 0
        self.user_usage = {}  # Tracks usage by each user

    def is_valid(self, user, cart_value):
        if cart_value< 100:
            return  False
        if not self.active:
            return False
        if datetime.now() > self.expiry_date:
            return False
        if self.used_count >= self.overall_limit:
            return False
        if self.user_usage.get(user.user_id, 0) >= self.per_user_limit:
            return False
        # Validate rules
        for rule, condition in self.rules.items():
            if not eval(f"{getattr(user, rule)} {condition}"):
                return False
        return True

    def use_coupon(self, user):
        if self.is_valid(user):
            self.used_count += 1
            self.user_usage[user.user_id] = self.user_usage.get(user.user_id, 0) + 1
            return True
        return False

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True


# Voucher Class
class Voucher:
    def __init__(self, voucher_id, assigned_user=None):
        self.voucher_id = voucher_id
        self.assigned_user = assigned_user  # None means unassigned
        self.used = False

    def is_available(self, user=None):
        if self.used:
            return False
        if self.assigned_user and self.assigned_user != user.user_id:
            return False
        return True

    def use_voucher(self):
        if self.is_available():
            self.used = True
            return True
        return False


# User Class
class User:
    def __init__(self, user_id, name, age):
        self.user_id = user_id
        self.name = name
        self.age = age


# Admin Class
class Admin:
    def __init__(self, admin_id, name):
        self.admin_id = admin_id
        self.name = name

    def create_coupon(self, coupon_id, rules, overall_limit, per_user_limit, expiry_date):
        return Coupon(coupon_id, rules, overall_limit, per_user_limit, expiry_date)

    def create_voucher(self, voucher_id, assigned_user=None):
        return Voucher(voucher_id, assigned_user)


# API Example
class CouponVoucherSystem:
    def __init__(self):
        self.coupons = {}  # Stores all coupons
        self.vouchers = {}  # Stores all vouchers

    def add_coupon(self, coupon):
        self.coupons[coupon.coupon_id] = coupon

    def add_voucher(self, voucher):
        self.vouchers[voucher.voucher_id] = voucher

    def get_available_coupons(self, user, cart_value):
        return [
            coupon for coupon in self.coupons.values()
            if coupon.is_valid(user, cart_value)
        ]

    def get_available_vouchers(self, user):
        return [
            voucher for voucher in self.vouchers.values()
            if voucher.is_available(user)
        ]
