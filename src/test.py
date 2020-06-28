import random

class RanGen:
  def __init__(self):
     pass

  @staticmethod
  def random_no_seed():
       random_num = random.uniform(1, 20)
       return random_num

  @staticmethod
  def random_with_seed(seed):
       random.seed(6)
       random_num = random.uniform(1.1,20.5)
       return random_num

  @staticmethod
  def list_generator(seed):

      random_list = []
      list_seed = seed
      random.seed(list_seed)


      for i in range(0, 100):
          random_num = random.uniform(0, 100)
          random_list.append(random_num)
      return random_list

  @staticmethod
  #attach CSV reader?
  def random_item():
      # used above function for testing
      test_list = RanGen.list_generator(12)

      choice = random.choice(test_list)
      return choice

  @staticmethod
  def random_seed_choice():
      # used above function for testing
      test_list = RanGen.list_generator(12)

      random.seed(6)
      choice = random.choice(test_list)
      return choice

  @staticmethod
  #for seed and not seed
  def n_items_no_seed(choices, seed = None):

      if seed is not None:
          random.seed(seed)






      number_of_choices = choices

      test_list = RanGen.list_generator(seed)

      sample = random.choices(test_list, k=number_of_choices)
      return sample


generate_number = RanGen()

# change to what func you want to test
msg = generate_number.n_items_no_seed(10, 100)

print(msg)















