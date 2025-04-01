def checking(word):
 with open("practice.txt","r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("found")
    else:
        print("not found")

def chk_by_line(word):
      data =  True
      line_no = 1
      with open("practice.txt","r") as f:
         while data == True:
            data = f.readline()
            if (word in data):
               print(line_no)
               return
            line_no += 1
      
      return -1
 
 
 
word = "learning"
print(chk_by_line(word))
            