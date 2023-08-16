from gde.models import *

# manages the contents of the shopping cart for different types of items
# by interacting with the cart data stored in the session.
# It allows users to add, remove, adjust quantities, and clear items from their
# cart while shopping on the web application.


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def add_videogame(self, videogame):
        if videogame.videogame_name not in self.cart.keys():
            self.cart[videogame.videogame_name] = {
                "name": videogame.videogame_name,
                "quantity": 1,
                "price": str(videogame.unit_price),
                "image": videogame.photo.url,
            }
        else:
            for key, value in self.cart.items():
                if key == videogame.videogame_name:
                    value["quantity"] += 1
                    break
        self.save()

    def add_dlc(self, dlc):
        if dlc.dlc_name not in self.cart.keys():
            self.cart[dlc.dlc_name] = {
                "name": dlc.dlc_name,
                "quantity": 1,
                "price": str(dlc.unit_price),
                # "image": dlc.photo.url,
            }
        else:
            for key, value in self.cart.items():
                if key == dlc.dlc_name:
                    value["quantity"] += 1
                    break
        self.save()

    def add_package(self, package):
        if package.package_name not in self.cart.keys():
            self.cart[package.package_name] = {
                "name": package.package_name,
                "quantity": 1,
                "price": str(package.unit_price),
                # "image": package.photo.url,
            }
        else:
            for key, value in self.cart.items():
                if key == package.package_name:
                    value["quantity"] += 1
                    break
        self.save()

    def remove_videogame(self, videogame):
        if videogame.videogame_name in self.cart:
            del self.cart[videogame.videogame_name]
        self.save()

    def remove_dlc(self, dlc):
        if dlc.dlc_name in self.cart:
            del self.cart[dlc.dlc_name]
        self.save()

    def remove_package(self, package):
        if package.package_name in self.cart:
            del self.cart[package.package_name]
        self.save()

    def decrease_videogame(self, videogame):
        for key, value in self.cart.items():
            if key == videogame.videogame_name:
                value["quantity"] -= 1
                if value["quantity"] < 1:
                    self.remove_videogame(videogame)
                    break
                self.save()
                break

    def decrease_dlc(self, dlc):
        for key, value in self.cart.items():
            if key == dlc.dlc_name:
                value["quantity"] -= 1
                if value["quantity"] < 1:
                    self.remove_dlc(dlc)
                    break
                self.save()
                break

    def decrease_package(self, package):
        for key, value in self.cart.items():
            if key == package.package_name:
                value["quantity"] -= 1
                if value["quantity"] < 1:
                    self.remove_package(package)
                    break
                self.save()
                break

    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True
