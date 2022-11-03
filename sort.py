def sort_dictionary(dictionary):
        dictionary = sorted(dictionary.items(), key=lambda x:x[1][1])
        print(dictionary.values())
        return dictionary

def main():
    a = {'Tom' : (5464512, 24) , 'Sara' : (5446987, 32) , 'Mary' : (1557896, 20)}
    print(sort_dictionary(a))
main()
