def left_join(H1, H2):
    """
    takes two hashmaps and left join them together in the first object
    arguments: two hashmaps
    returns: the first hashmap but left joined with the second hashmap
    """
           
    for key in H1:
        
        if key in H2:
            H1[key] = [H1[key] , H2[key]]
        else:
            H1[key] = [H1[key], "null"]
        
    return H1

if __name__ == "__main__":
    H1 = {"color": "black",
          "name": "abdullah"
          }
    H2 = {"color": "red",
          "namee": "abdullah"
          }
    print(left_join(H1, H2))