import random


def random_no_seed():
       random_num = random.uniform(1, 20)
       return random_num


def random_with_seed(seed):
       random.seed(6)
       random_num = random.uniform(1.1,20.5)
       return random_num


def list_generator(seed):

      random_list = []
      list_seed = seed
      random.seed(list_seed)


      for i in range(0, 100):
          random_num = random.uniform(0, 100)
          random_list.append(random_num)
      return random_list


  #attach CSV reader?
def random_item():
      # used above function for testing
      test_list = list_generator(12)

      choice = random.choice(test_list)
      return choice


def random_seed_choice():
      # used above function for testing
      test_list = list_generator(12)

      random.seed(6)
      choice = random.choice(test_list)
      return choice


  #for seed and not seed
def n_items_no_seed(choices, seed = None):

      if seed is not None:
          random.seed(seed)

      number_of_choices = choices

      test_list = list_generator(seed)

      sample = random.choices(test_list, k=number_of_choices)
      return sample




# change to what func you want to test
msg = n_items_no_seed(10, 100)

print(msg)















