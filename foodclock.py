#!/usr/bin/python3

import sqlalchemy

#TODO {time:[food1, food2...]}
class FoodType():
    milk = 'молочные продукты'
    fruit = 'фрукты'
    meat = 'мясо'
    fish = 'рыба'
    vegetable = 'овощи'
    nut = 'орехи'
    fastfood = 'фастфуд'
    water = 'вода'
    drink = 'напитки'
    alco = 'алкогольные напитки'
    oil = 'масло'
    spice = 'специи'

class Food():
    def __init__(self, name, food_type, proteins, fats, carbs, calories = -1):
        """
        Create food with params:
        name = name of the product

        food_type = type of product, FoodType.type (instead of type insert: 
        milk, fruit, meat, fish, vegetable, nut, fastfood, 
        water, drink, alco, oil, spice)
        
        proteins, fats, carbs

        calories = if not inserted, programm calculates it
        """
        if calories == -1:
            self.calories = proteins * 4 + fats * 9 + carbs * 4
        else:
            self.calories = calories
        
        self.name = name
        self.food_type = food_type

        self.proteins = proteins
        self.fats = fats
        self.carbs = carbs
    
    def energy(self, mass = 100):
        """
        Return list with proteins, fats, carbs and calories in amount(gr) of product
        """
        energy = [self.proteins, self.fats, self.carbs, self.calories]
        energy = map(lambda x: x / 100 * mass, energy)

        return energy

class Recipe():
    pass    

class Event():
    def __init__(self, ):


class EatEvent(Event):
    pass

class DailyRation():
    pass

def main():
    jogurt = Food('Йогурт Danone Натуральный', FoodType.milk, 3.5, 2.5, 4.7)
    print(jogurt.food_type, jogurt.food_type == FoodType.milk, jogurt.food_type == 'молочные продукты')
if __name__ == '__main__':
    main()