def sort_dictionary(dictionary):
        temp = []
        dictionary = dict(sorted(dictionary.items(), key=lambda x:x[1][1]))
        for key in dictionary:
                temp.append((key, dictionary[key][0]))
        return temp
