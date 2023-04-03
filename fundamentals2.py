# Countdown - Create a function that accepts a number as an input.
# Return a new list that counts down by one, from the number (as the 0th element)
# down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

# def countDown(startingNr, endingNr):
#     myList = []
#     if (startingNr<=endingNr):
#         print('Numri i perfundimit duhet te jete me i vogel se numri i fillimit, ne menyre qe une te punoj!')
#     else:
#         for x in range (startingNr, endingNr-1 ,-1):
#             myList.append(x)
#         return myList



# print(countDown(10, int(input())))


# Print and Return - Create a function that will receive a list 
#with two numbers. Print the first value and return the second.

def printAndReturn(myList):
    if type(myList) is not list:
        print('please enter a list')
    else:
        print(myList[0])
        return myList[1]

# print(printAndReturn('s'))

#First Plus Length - 
# Create a function that accepts a list and 
# returns the sum of the first value in the list plus the list's length.

def printSum(myList):
    sum = 0
    elementi1 = myList[0]
    gjatesiaListes = len(myList)
    sum = elementi1 + gjatesiaListes
    return sum

# print(printSum([2,4,5,3334]))

# Values Greater than Second - 
# Write a function that accepts a list and creates a new list 
# containing only the values from the original list 
# that are greater than its 2nd value. 
# Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) 
# should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def greaterThanSecond(myList):
    if len(myList)<2:
        return False
    newList = []
    for i in range(len(myList)):
        if myList[i]>myList[1]:
            newList.append(myList[i])
    print(len(newList))
    return newList
# print(greaterThanSecond([4]))
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(maksimumi, expectedValue):
    newList = []
    for i in range(maksimumi):
        newList.append(expectedValue)
    return newList

# print(length_and_value(5,7))
# Change the value 10 in x to 15.  Done
# Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : [{"name": "Leo", "last_name": ['Antoine', 'Messi']}, 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


# print(sports_directory['soccer'][0]["last_name"][1])


# x[1][0] = 15
# print(x)
# students[0]['last_name'] = 'Bryant'
# print(students)
# sports_directory['soccer'][0] = "Andres"
# print(sports_directory)

z[0]['y'] = 30


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for key, value in dojo.items():
        print(f"{len(value)} {key}" )
        print(value)
        for items in value:
            print(items)
# printInfo(dojo)
# # output:

