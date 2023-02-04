#Create a file called app.py

#code example

text_file = open('001_helloworld.py'),'rb')

my_code = text_file.read()

exec(my_code)
