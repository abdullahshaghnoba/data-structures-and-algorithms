list = [
    {"title": "The aa", "year": 2018},
    {"title": "zz aa", "year": 2016},
    {"title": "dd", "year": 2020},
    {"title": "The bb", "year": 2016},
    {"title": "The cc", "year": 2010},
]



# def sort_numbers(list):
#     new_list = []
#     temp_list = []
#     for idx, item in enumerate(list):
#         year = item["year"]
#         index = idx
#         new_list.append((index,year))
#     new_list.sort(key=lambda tup: tup[1], reverse=True)
#     for idx, item in enumerate(new_list):
#         temp_list.append(list[item[0]])
#         # list[idx] = temp_list[idx]
#         print(temp_list[idx])
#     for idx, item in enumerate(list):
#         list[idx] = temp_list[idx]
#     return list


def sort_by_recent_year(list):
    """
    takes a list of dictionaries and sorts it by the year atribute in the dictionaries in decending order
    arguments : list of dictionaries
    returns: sorted list of dictionaries by the year atribute in the dictionaries in decending order
    """
    return sorted(list, key=lambda movie: movie["year"], reverse=True)




def sort_strings(list):
    """
    takes a list of dictionaries and sorts it by the title atribute in the dictionaries alphabitcaly
    arguments : list of dictionaries
    returns: sorted list of dictionaries by the title atribute in the dictionaries in alphabitcaly
    """

    def remove (movie):
        
            if movie.startswith(("A ", "An ", "The ")):
                movie = movie[movie.index(" ")+1:]
                # print(movie)
                return movie
            return movie
     

    list = sorted(list, key=lambda movie: remove(movie["title"]))

    return list



print(sort_strings(list))