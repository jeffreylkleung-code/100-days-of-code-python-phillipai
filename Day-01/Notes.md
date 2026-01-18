Understanding variables and data types
FreeCodeCamp

Declaring a variable
name = 'Jeffrey'
- Cannot start with a number
- Can contain, characters, numbers and underscores
- case sensitive
- cannot be reserved words, e.g. if, class, def

Print
print('Hello world') 
- This will ouput "Hello world" into the terminal

print('Hello', 'World!')
- will contain a space
- Outputs 'Hello World!'
print('Hello'+ 'World!')
- Outputs 'HelloWorld!'
- will not contain a space
Using , and + is different in string manipulation

data types
- string: sequence of characters; String_var = "Hello World"
- integer: Whole numbers; Integer_var = 2
- float: Number with decimal point; Float_var = 2.2
- boolean: true or false; Boolean_var = true
- none: litterally nothing, absence of a value; None_var = none

Collections data type
These data types can contain a collection of elements or variables
data types is declared different with brackets, e.g. (), {}, []
- Set: unordered collection of unique elements; Set_var = {7, 2, 7}
- Dictionary: collection of key-value pairs; Dictionary_var = {'Hamburger': 5, 'fries': 2}
- Tuple: an immutable ordered colelction; Tuple_var = (7, 2, 7)
    - immutable: fixed, unchangeable value
- list: an ordered collection of elements that supports different data types; my_list = [1, 1.1, True, 'hello world']
- Range: sequence of numbers, often used in loops; Range_var = range(5)

Type function
- returns the type of a variable
print(type(string_var))
- outputs <class 'str'>

isinstance function
- checks if a variable matches a specific data type
    isinstance('Hello world', str) 
    - outputs True

