import re


class DataPackage:

    def __init__(self, package, package_composite):
        self.package = package
        self.package_composite = package_composite

    def price_of_package(self):
        price = self.package_composite(self)
        return price

    def __repr__(self):
        statement = " : {}"
        return statement.format(self.price_of_package())


def Transmission(order):
    package = order.package
    try : 
        if package["Transmission"] == "ship":
            return "Ship"
        elif package["Transmission"] == "air":
            return "Air"
    except:
        return "-"



def Repackag(order):
    package = order.package
    try : 
        if package["Repackag"] == "re":
            return "Repackkag"
        elif package["Repackag"] == "notre":
            return "Don't Repackkag"
    except:
        return "-"

def Weight(order):
    package = order.package
    try : 
        if package["Weight"] == "5kg":
            return "5 kg"
        elif package["Weight"] == "10kg":
            return "10 kg"
        elif package["Weight"] == "15kg":
            return "15 kg"
        elif package["Weight"] == "20kg":
            return "20 kg"
        elif package["Weight"] == "20kgup":
            return "20 kg up"
    except:
        return "-"


def PriceInvoice(order):
    package = order.package
    try : 
        if package["PriceInvoice"] == "invoice":
            return "Tax"
        elif package["PriceInvoice"] == "uninvoice":
            return "none Tax"
    except:
        return "-"
