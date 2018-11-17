# Week 8 Review

## Assessing your Problem Solutions
Recall, your work involves more than just correctness. Specifically, we will look for:

* appropriate separation of concerns (including classes)
* appropriate use of function interfaces (i.e., using parameters and return values, not using variables declared as part of a script to make them accessible in all function scopes)
* comments explaining the why behind more difficult areas of code
* documentation of classes/modules for explaining their purpose and usage
* good function, parameter, and variable names that communicate the purpose and make the program more readable
* Please keep in mind there is no single correct answer for how you design the program: there are many good approaches that are worth full credit.

## 1 [unique_list.py]
A unique list has no repeated items. For example, the list ['orange', 'juice', 'futures'] is unique because each item only appears one time. However, the list ['sell','mortimer','sell'] is not unique because the string 'sell' appears more than one time.

Write a program named `unique_list` where a user inputs a series of positive integers and, when finished, it reports whether or not the sequence of numbers input is unique or not. For example:
```
This program tests if the sequence of positive numbers you input are unique
Enter -1 to quit
Enter the first number: 9
Next: 5
Next: 3
Next: 6
Next: 23
Next: -1
The sequence [9, 5, 3, 6, 23] is unique!
```
```
This program tests if the sequence of positive numbers you input are unique
Enter -1 to quit
Enter the first number: 83
Next: 20
Next: 593
Next: 28
Next: 20
Next: 51
Next: -1
The sequence [83, 20, 593, 28, 20, 51] is NOT unique!
```

## 2 [vending_status_checker.py]
Modify the vending status checker to now also report on the status of the machines overall.

Our current vending status checker produces an inventory report. For each machine's inventory file it is counting how many of each beverage were stocked last time, how many of that beverage are currently in stock, and how many slots the beverage occupies (i.e., each slot holds 8 beverages). Your goal is to modify the program such that it can also produce a machines' sales report, something like this:

```
Label           Pct Sold   Sales Total  
REID_1F            52.40% $  230.25
REID_2F            42.02% $  138.25
REID_3F            52.07% $  214.75
```

This report contains three fields: the label of the vending machine, what percentages of the beverages it was last stocked with are sold, and how many total dollars of sales has this generated.

You will need to create a new dictionary where the keys are the vending machine labels, and the values are a new type of object called a `MachineStatus`. For each instance, the `MachineStatus` class should store:

* the label of a vending machine
* the total amount of beverages the vending machine was previously stocked with
* the total amount of beverages currently in stock in the vending machine
* the total income of the machine from the last time it was stocked until now (note: beverages have different prices, so you cannot simply multiply the change in stock times $1.50 to get the total income)

Three major modifciations to `vending_status_checker.py` are necessary:

* adding the `MachineStatus` class
* adding to the loop for counting beverages additional code for counting and updating a vending machine's `MachineStatus` object values
* enabling a user to choose the machines' sales report, not just the inventory report, and then display the report as shown in the following example

```
Would you like the (m)achine report or the (i)nventory report? m
Label           Pct Sold   Sales Total  
REID_1F            52.40% $  230.25
REID_2F            42.02% $  138.25
REID_3F            52.07% $  214.75
```

HINT: Start by making sure you understand how the counting is done for inventory, most importantly how the dictionary is used to go from the name a beverage to its `InventoryItem` object. Then create a new dictionary with vending machine labels as keys that maps to the vending machine's `MachineStatus` object. There should be only one `MachineStatus` object for each vending machine.
