#!/usr/bin/python

import math

recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }


def recipe_batches(recipe, ingredients):
  # pass
  # print(len(recipe))
  # print(len(ingredients))
  num_of_times = 0
  can_still_bake = True

  if len(recipe) > len(ingredients):
          return 0
  else:
    while can_still_bake:
      for key in recipe:
              # print(recipe.values())
        if key in ingredients:
          if recipe[key] <= ingredients[key]:
            ingredients[key] = ingredients[key] - recipe[key]
          else:
            # return batch
            can_still_bake = False
        else:
          # return batch
          can_still_bake = False
      if can_still_bake:
        num_of_times += 1
  return num_of_times



# print(recipe_batches(recipe, ingredients))
print(recipe_batches(
  { 'milk': 2, 'sugar': 40, 'butter': 20 },
  { 'milk': 5, 'sugar': 120, 'butter': 500 }))


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))