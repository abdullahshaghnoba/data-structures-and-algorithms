# Code Challenge 26

---

## sort_by_recent_year function 
## takes a list of dictionaries and sorts it by the year atribute in the dictionaries in decending order
## arguments : list of dictionaries
## returns: sorted list of dictionaries by the year atribute in the dictionaries in decending order

---

## sort_strings function
## takes a list of dictionaries and sorts it by the title atribute in the dictionaries alphabitcaly
## arguments : list of dictionaries
##  returns: sorted list of dictionaries by the title atribute in the dictionaries in alphabitcaly


---

## Approach & Efficiency


### sort_by_recent_year function 
### takes a list of dictionaries and sorts it by the year atribute in the dictionaries in decending order
### arguments : list of dictionaries
### returns: sorted list of dictionaries by the year atribute in the dictionaries in decending order

---

### sort_strings function
### takes a list of dictionaries and sorts it by the title atribute in the dictionaries alphabitcaly
### arguments : list of dictionaries
### returns: sorted list of dictionaries by the title atribute in the dictionaries in alphabitcaly

## for both functions
## O(n*log(n)) Time performance --> because we depend on the input size **we have to loop through the given input with a loop and we use the built in sorted method that has time performance of n*log(n)**. 
## O(n) Space performance --> the size of memory taken depends on the input size.

## Solution:

def sort_by_recent_year(list):
   
    return sorted(list, key=lambda movie: movie["year"], reverse=True)




def sort_strings(list):
    

    def remove (movie):
        
            if movie.startswith(("A ", "An ", "The ")):
                movie = movie[movie.index(" ")+1:]
                # print(movie)
                return movie
            return movie
     

    list = sorted(list, key=lambda movie: remove(movie["title"]))

    return list