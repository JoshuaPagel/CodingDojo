#1 Update values in dictionaries and lists
# 1) Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# 2) Change the last_name of the first student from 'Jordan' to 'Bryant'
# 3) In the sports_directory, change 'Messi' to 'Andres'
# 4) Change the value 20 in z to 30

x = [ [5,2,3], [15,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Bryant'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]

def iterateDictionary(key_name, some_list):
