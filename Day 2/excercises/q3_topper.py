#we make a tuple with data of 10 students as [name, roll no, marks]  and print the topper
a=(('Aman kumar',1,23), ('Chandan kumar',2,45),('Praveen kumar',3,65) ,('Sonu Kumar',4,34)  , ('Piyush Pankaj',5,56) ,( 'MD raziulla',6,46) ,( 'Saurab kumar',7,99) , ('Sandli kumari',8,27) , ("Alok kumar ray",9,58)  ,("Himanshu raj",10,79))
maxa=0
topper_index=0
for i in range(10):
    if(maxa<a[i][2]):
        maxa=a[i][2]
        topper_index=i
print(f"{a[topper_index][0]} is the Topper with {a[topper_index][2]} marks")