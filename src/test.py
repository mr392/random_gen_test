import random

class RanGen:
  def __init__(self):
     pass

  @staticmethod
  def random_no_seed():
       random_num = random.uniform(1, 20)
       return random_num

  @staticmethod
  def random_with_seed():
       random.seed(6)
       random_num = random.uniform(1.1,20.5)
       return random_num











generate_number = RanGen()

msg = generate_number.random_with_seed()
print(msg)
















