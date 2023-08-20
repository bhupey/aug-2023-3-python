#Given a list a = [(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)], sort the list based on the last item of each tuple inside the list.
a = [(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)]
def get_last(element):
    return element[-1]
a.sort(key=get_last)
print(a)