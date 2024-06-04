import json
f=open("tf_ass.txt","w")
s="""
Date,Product,Quantity,Sale_Amount
2023-01-05,Shoes,2,120.00
2023-01-10,T-Shirt,3,45.00
2023-01-15,Jeans,1,60.00
2023-02-03,Hat,2,20.00
2023-02-07,Shoes,1,60.00
2023-02-15,Jeans,2,120.00
2023-03-02,T-Shirt,4,60.00
2023-03-12,Hat,1,10.00
2023-03-20,Shoes,3,180.00
2023-04-05,Jeans,1,60.00
2023-04-10,T-Shirt,2,30.00
2023-04-18,Hat,1,10.00
2023-05-01,Shoes,2,120.00
2023-05-08,T-Shirt,3,45.00
2023-05-15,Jeans,1,60.00
2023-06-03,Hat,2,20.00
2023-06-07,Shoes,1,60.00
2023-06-15,Jeans,2,120.00
2023-07-02,T-Shirt,4,60.00
2023-07-12,Hat,1,10.00
2023-07-20,Shoes,3,180.00
2023-08-05,Jeans,1,60.00
2023-08-10,T-Shirt,2,30.00
2023-08-18,Hat,1,10.00
2023-09-01,Shoes,2,120.00
2023-09-08,T-Shirt,3,45.00"""    #docstring
f.write(s)
f.close()

with open('tf_ass.txt','r') as file:
    file_content=file.read()

content_write=file_content
json_path='ass_json'
with open(json_path,'w') as json_file:
    lines=content_write.strip().split('\n')
    headers=lines[0].split(',')
    data=[]
    for line in lines[1:]:
        values=line.split(',')
        entry=dict(zip(headers,values))
        data.append(entry)
    json.dump(data,json_file,indent=4)                                               #dump()-allows to store json data directly into a file(2 arg)

# read data form json fle
with open('ass_json','r') as json_read:
    data=json.load(json_read)

#operations on data
total_sales=sum(float(entry['Sale_Amount']) for entry in data)
avg_sales=total_sales/len(data)

#quantity sold for each product
product_sales={}
for entry in data:
    product=entry['Product']
    quantity=int(entry['Quantity'])
    if product  in product_sales:
        product_sales[product] += quantity
    else:
        product_sales[product]=quantity
most_sales=max(product_sales,key=product_sales.get)

output_path='output.txt'
with open(output_path,'w') as output_file:
    output_file.write('Total Sales Amount: ${:.2f} \n'.format(total_sales))
    output_file.write('Average Sale Amount:${:.2f} \n'.format(avg_sales))
    output_file.write('Most Popular Product:{} \n'.format(most_sales))
    for product, quantity in product_sales.items():
        output_file.write("- {}: {}\n".format(product, quantity))



