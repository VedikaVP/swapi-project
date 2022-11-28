import random
class generate_number():
    """
    defining generate_number function to generate random 15 number in between 1 to 82.
    function will return a interger of lsit which contains 15 random number .
    """

    def random_list(self, count, min, max):
        list1 = []
        while len(list1) < count:
            number = random.randrange(min, stop = max)
            list1.append(number)
        return(list1)


