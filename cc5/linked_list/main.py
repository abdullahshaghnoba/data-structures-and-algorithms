from linked_list import LinkedList

if __name__=="__main__":
   linked_list1 = LinkedList()
   linked_list1.insert("A")
   linked_list1.insert("B")
   linked_list1.append("D")
   linked_list1.insert_before("D","C")
   linked_list1.insert_after("D","E")
   linked_list1.delete_node("k")
   print (linked_list1)   
   print (linked_list1.includes("C"))   
   print (linked_list1.includes("k"))   
   print (linked_list1.kthFromEnd(0))   