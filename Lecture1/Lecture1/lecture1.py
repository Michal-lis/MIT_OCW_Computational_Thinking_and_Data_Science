class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCalories(self):
        return self.calories

    def density(self):
        return self.getValue() / self.getCalories()

    # str for std.out.write object
    def __str__(self):
        return self.name + ': <' + str(self.value) \
               + ', ' + str(self.calories) + '>'

    # repr for presenting a list of elements
    def __repr__(self):
        return self.name + ': <' + str(self.value) \
               + ', ' + str(self.calories) + ', ' + str("%.4f" % self.density()) + '>'


def buildMenu(names, values, calories):
    """names, values, calories lists of same length.
       name a list of strings
       values and calories lists of numbers
       returns list of Foods"""
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                         calories[i]))
    return menu


def greedy(items, maxCalories, keyFunction):
    """Assumes items a list, maxCalories >= 0,
         keyFunction maps elements of items to numbers"""

    # key - a function to be called on each list element prior to making comparisons
    itemsCopy = sorted(items, key=keyFunction,
                       reverse=True)
    print(itemsCopy)
    result = []
    totalValue, totalCalories = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCalories + itemsCopy[i].getCalories()) <= maxCalories:
            result.append(itemsCopy[i])
            totalCalories += itemsCopy[i].getCalories()
            totalValue += itemsCopy[i].getValue()
    return (result, totalCalories, totalValue)


def testGreedy(items, constraint, keyFunction):
    taken, calories, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    print('Total calories of items taken =', calories)
    for item in taken:
        print('   ', item)


def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    # pass a function as the third argument

    print('\nUse greedy by Calories to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits,
               lambda x: 1 / Food.getCalories(x))
    # lambda great for one liners
    print('\nUse greedy by density to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.density)


names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 750)
