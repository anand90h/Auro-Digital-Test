import xml.etree.ElementTree as ET 

# Pass the path of the xml document 
tree = ET.parse('orders.xml') 

# get the parent tag 
root = tree.getroot() 

# print the root (parent) tag along with its memory location 
print(root) 

# print the attributes of the first tag  
print(root[0].attrib) 




import heapq


dic = {}

key_to_dic = {}

for child in root:
    
    print(child.tag, child.attrib)

# we can maintain a dictionary of the order books mapping to two heaps, one maxheap and one minheap
# for buy orders and sell orders. We have another dictionary of orderID to the order book. 
# Everytime an order comes, if it is a delete order we search for it in the heaps of the respective order book
# and if found we delete it.
# If it is an addorder, we add to the add order heap and run a while loop till the price of the top of sell book <= top of the buy book
# and keep removing orders from both till the condition is met.
