file_1 = open("dat.txt","r")
product_name = "";product_price = 0.0
total = 0.0;date = "";das = "-"
for line in file_1:
  product_name = line.rstrip()
  line = file_1.readline()
  product_price = line.rstrip()
  total += float(product_price)
  line = file_1.readline();date = line.rstrip()
  print("%-30s" % product_name,end="")
  print(":","%16.2f" % float(product_price),end="")
  print("%17s" % date)
print(das * 65);print("Total:",round(total,3))
file_1.close()