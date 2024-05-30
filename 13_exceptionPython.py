#2 ways to throw an error explicitely when condition is not matched

ItemInCart = 0
#2 item will be added in cart

# if ItemInCart !=2:
#     raise Exception("Product cart count not matching")
#     pass

#assert (ItemInCart == 2 )
#trycatch Block, write a code and don't stop test execution,

try:
    with open('test.txt', 'r') as reader:
        reader.read()

except Exception as e:
     print(e)

finally:
    print("Cleaning up resources")
