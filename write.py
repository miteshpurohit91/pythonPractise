#Read the file and store all the lines in list
#reverse list
#write the list back to the file


with open('test.txt', 'r') as reader:
   content = reader.readlines() #[abc,bcd,cde,def,efg,fgh]
   reversed(content) # [fgh,efg,def,cde,bcd,abc]
   with open('test.txt', 'w') as writer:
       for line in reversed(content):
           writer.write(line)


