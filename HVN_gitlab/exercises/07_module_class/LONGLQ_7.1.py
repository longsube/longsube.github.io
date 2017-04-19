class Trading:
    def  __init__(self, **goods):
        #goods{name:(price, quantity, size)}
        self.goods = goods
 
    def buyer(self,money, bags):
        return (money,bags)

    def buy(self, buyer, **goods_quantity):
        #goods_quantity{name:quantity}
        amount_money = 0
        amount_size = 0
        for k,v in goods_quantity.iteritems():
            if v > self.goods[k][1]:
                return "Not enough %s"%(k)
                break
            else:
                amount_money += (self.goods[k][0]*v)
                amount_size += (self.goods[k][2]*v)
        if amount_money > buyer[0]:
            return "Not enough money to buy"
            #    break
        elif amount_size > buyer[1]:
            return "Not enough bags for carrying"
            #    break
        else:
                #for i in 
            return "Buying success"


if __name__ == '__main__':
    trading = Trading(apple=(10000, 4, 3), milks=(40000, 3, 4), beef=(100000, 3, 5))
    bm = int(raw_input("Buyer money: >"))
    bb = int(raw_input("Buyer bags: >"))
    buyer = trading.buyer(bm, bb)
    a = int(raw_input("apple_amount: >"))
    m = int(raw_input("milks_amount: >"))
    b = int(raw_input("beef_amount: >"))
    print trading.buy(buyer, apple=a, milks=m, beef=b)



# Buyer money: >1000000
# Buyer bags: >100
# apple_amount: >2
# milks_amount: >2
# beef_amount: >2
# Buying success

