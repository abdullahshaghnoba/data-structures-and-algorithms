from linked_list import LinkedList

if __name__=="__main__":
   linked_list1 = LinkedList()
   linked_list1.insert("A")
   linked_list1.insert("B")
   linked_list1.append("E")
   linked_list1.insert_before("E","C")
   linked_list1.insert_after("E","F")
   linked_list1.delete_node("A")
   print (linked_list1)   
   print (linked_list1.includes("C"))   
   print (linked_list1.includes("A"))   