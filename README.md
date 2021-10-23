# python_advanced_exam
Problem 1 - Aladdin's Gifts

First, you will receive a sequence of integers representing the materials for every wedding present. After that, you will be given another sequence of integers – Genie magic level for every aim to make a gift.
Your task is to mix materials with magic levels so you can make presents, listed in the table below.
To make a present, you should take the last integer of materials and sum it with the first magic level value. If the result is between or equal to the numbers described in the table above, you make the corresponding gift and remove both materials and magic value. Otherwise:
    • If the product of the operation is under 100:
        ◦ And if it is an even number, double the materials, and triple the magic, then sum it again. 
        ◦ And if it is an odd number, double the sum of the materials and the magic level. Then, check again if it is between or equal to any of the numbers in the table above.
    • If the product of the operation is more than 499, divide the sum of the material and the magic level by 2. Then, check again if it is between or equal to any of the numbers in the table above.
    • If, however, the result is not between or equal to any of the numbers in the table above after performing the calculation, remove both the materials and the magic level.
Stop crafting gifts when you are out of materials or magic level.
You have succeeded in crafting the presents when you've crafted either one of the pairs - a gemstone and a sculpture or gold and jewellery.

Problem 2 - Ball in the Bucket

You are at the funfair to play different games and test your skills. Now you are playing ball in the bucket game.
You will be given a matrix with 6 rows and 6 columns representing the board. On the board, there will be points (integers) and buckets marked with the letter "B". Rules of the game:
    • You can throw a ball only 3 times.
    • When you hit a bucket (position marked with 'B'), you score the sum of the points in the same column.
    • You can hit a bucket only once. If you hit the same bucket again, you do not score any points. 
    • If you hit outside a bucket (hit a number on the board) or outside the board, you do not score any points. 
After the board state, you are going to receive the information for every throw on a separate line. The coordinates’ information of a hit will be in the format: "({row}, {column})".
Depending on how many points you have collected, you win one of the following:
Football
100 to 199 points
Teddy Bear
200 to 299 points
Lego Construction Set
300 and more points

Your job is to keep track of the scored points and to check if you won a prize. 

Problem 3 - Shopping List

Write a function called shopping_list which will receive an integer number representing the budget in leva and a different number of keywords. Each key represents the product (string), and each value will be a tuple with the product's price (integer or float number) at the first position and quantity (integer) at the second position.
Your job is to return which products you bought with the given budget. You only buy a product if you can buy all of its quantity.
You could only start shopping if you have at least 100 leva budget. Otherwise, you should stop the program and return "You do not have enough budget.".
Also, you are carrying a basket that cannot hold more than 5 types of products. You should stop buying products:
    • if you reach the allowed amount of types of products (no matter their quantity)
    • if you did not reach the allowed amount, but you do not have more products on the shopping list
You should always buy products successively!
For each product (all its quantity) you succeeded to buy, return a string on a new line in the following format:
"You bought {product_name} for {total_price} leva."
Note: Submit only the function in the judge system
Input
    • There will be no input, and just parameters passed to your function
Output
    • The function should return strings on separate lines containing the bought products and their price in the format described above.
    • The total price should be formatted to the second decimal point.
