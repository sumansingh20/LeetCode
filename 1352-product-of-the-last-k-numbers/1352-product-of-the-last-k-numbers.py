class ProductOfNumbers:
    def __init__(self):
        self.products = [1]
    def add(self, num: int) -> None:
        if num == 0:
            self.products = [1]
        else:
            last = self.products[-1]
            self.products.append(last * num)
    def getProduct(self, k: int) -> int:
        n = len(self.products)
        if k >= n:
            return 0
        return self.products[n - 1] // self.products[n - 1 - k]