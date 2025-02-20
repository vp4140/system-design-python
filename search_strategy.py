#we are building search startegy in amazom
# String
# productId;
# String
# title, description;
# String
# images[];
# double
# price;
# double
# averageRating;
from typing import List
from abc import ABC,abstractmethod

class Product:
    def __init__(self,productId,title,price,averageRating):
        self.productId = productId
        self.title = title
        self.price = price
        self.averageRating = averageRating

    def __repr__(self):
        return f"Product({self.productId}, {self.title}, ${self.price}, Rating: {self.averageRating})"

    def __str__(self):
        return f"{self.title}-{self.price}-{self.averageRating}"


class SearchStrategy(ABC):
    @abstractmethod
    def search(self,products,query:int):
        pass
class SearchByPrice(SearchStrategy):

    def search(self,products:List[Product],query:int):
        print("Searching by price")
        ans = [ele for ele in products if ele.price == query ]
        return ans



class SearchByRating(SearchStrategy):

        def search(self, products: List[Product], query: int):
            print("Searching by rating")
            ans = [ele for ele in products if ele.averageRating == query]
            return ans

class StrategyContext:
    def __init__(self,strategy:SearchStrategy):
        self.strategy = strategy
    def assign_strategy(self,strategy:SearchStrategy):
        self.strategy = strategy
    def search(self,products:List[Product],query:int):
        return self.strategy.search(products,query)


if __name__ == "__main__":
    print("I am here")
    p1 = Product(1,"Vishal",10,2)
    p2 = Product(2,"Rahul",15,3)
    p3 = Product(3,"neel",10,2)

    products = [p1,p2,p3]
    s = SearchByPrice()
    context = StrategyContext(s)
    print(context.search(products,10))
    print(context.assign_strategy(SearchByRating()))
    print((context.search(products,3)))