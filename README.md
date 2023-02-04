# p
Public Private Repository

How to public private code
How to private public code

1.- helloworld.py
#Create a file called helloworld.py

#code example for an instruction
print('Hello World')

2.- app.py
#Create a file called app.py

#code example 
text_file = open('helloworld.py'),'rb')
my_code = text_file.read()

exec(my_code)

3.- encodeandzip.py
#Execute this file to create a ofuscated code
import zlib, base64

text_file = open('helloworld.py'),'rb')
my_code = text_file.read()
#step one
compressed_data = zlib.compress(my_code, zlib.Z_BEST_COMPRESSION)
gzipped_data = base64.b64encode(compressed_data).decode()

f = open('zipped.txt'),'wb')
f.write(compressed_data)
f.close()

4.- testing.py
#testing the code
fichero = open('zipped.txt','rb')
compressed_data_fromFile = fichero.read()
gzipped_data_fromFile = base64.b64encode(compressed_data_fromFile).decode()
exec(zlib.decompress(base64.b64decode(gzipped_data_fromFile)))

5.- frominternet.py 
#submit que file to github
import urllib.request
#download and decode
url="https://github.com/inforland/p/zipped.txt"
text = urllib.request.urlopen(url).read()
compressed_data_fromFile = text
gzipped_data_fromFile = base64.b64encode(compressed_data_fromFile).decode()

exec(zlib.decompress(base64.b64decode(gzipped_data_fromFile)))
