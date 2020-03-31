from threading import Thread, Condition

fruits = ['Apple', 'Mango', 'Orange']
basket = []
# create Condition object
condition = Condition()


class ShopKeeper(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for i in range(3):
            # Get the lock
            condition.acquire()
            # Insert a fruit in basket
            basket.append(fruits[i])
            # display status
            print(basket[0]+' is kept')
            # notify the waiting thread - customer
            condition.notify()
            # keep shop keeper thread in waiting state
            condition.wait()
            # Release the lock
            condition.release()


class Customer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for i in range(3):
            # Get the lock
            condition.acquire()
            # check that basket is empty or not
            if len(basket) == 0:
                print('Pls wait...')
                condition.wait()
            # consume the item
            print(basket[0]+' is consumed')
            # empty the basket
            basket.clear()
            # Notify the waiting Shop keeper thread
            condition.notify()
            # Keep the customer thread in waiting
            if i < 2:
                condition.wait()
            # Release the lock
            condition.release()


# create producer thread - Shop keeper
shopKeeper = ShopKeeper()
# create consumer thread - Customer
customer = Customer()
# change status of both threads to ready to run state
customer.start()
shopKeeper.start()
