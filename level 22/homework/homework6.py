def longest_string(string):
    longest=""
    for i in string:
        if len(i) > len(longest):
            longest=i
    print(f"the longest string is{longest}")


string_list=["gia, nodo, kia"]
longest_string(string_list)
