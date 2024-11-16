class ShopManager:
    def __init__(self):
        self.shop_open = False
        self.is_openable = False

    def open_shop(self):
        self.shop_open = True

    def close_shop(self):
        self.shop_open = False

    def is_shop_open(self):
        return self.shop_open

    def is_openable(self):
        return self.is_openable

    def set_openable(self, openable):
        self.is_openable = openable
