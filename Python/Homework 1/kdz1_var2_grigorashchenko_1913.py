# Global constants indicating indices in the linked list node
VALUE = 0
NEXT = 1
PREV = 2


# Linear singly linked list with head and tail
def add_to_back_2(value, head, tail):
    item = [value, None]
    if head is None:
        head = item
    else:
        tail[NEXT] = item
    tail = item
    return head, tail


def add_to_front(value, head, tail):
    item = [value, None]
    if head is None:
        head = tail = item
        return head, tail
    item[NEXT] = head
    head = item
    return head, tail


def print_elements_one_by_one(head):
    if head is None:
        return None
    else:
        newlist = []
        newlist.append(head[VALUE])
        headcopy = list.copy(head[NEXT])
        while headcopy[NEXT] != None:
            newlist.append(headcopy[VALUE])
            headcopy = list.copy(headcopy[NEXT])
        newlist.append(headcopy[VALUE])
        return newlist


def get_an_element_by_index(index):
    if head is None:
        return None
    elif index == 0:
        return head[VALUE]
    else:
        headindex = 1
        headcopy2 = list.copy(head[NEXT])
        while headindex <= index:
            if headindex == index:
                return headcopy2[VALUE]
            else:
                if headcopy2[NEXT] == None:
                    return 'Your index is out of range'
                    break
                headcopy2 = list.copy(headcopy2[NEXT])
                headindex = headindex + 1


def remove_an_element_from_the_front(head):
    if head is None:
        return None
    else:
        headcopy4 = list.copy(head)
        a = headcopy4[NEXT]
        b = a[VALUE]
        head[VALUE] = b
        c = a[NEXT]
        head[NEXT] = c
        return head, tail


def remove_an_element_from_the_end(head, tail):
    if head is None:
        return None
    else:
        newlist = []
        newlist.append(head[VALUE])
        headcopy5 = list.copy(head[NEXT])
        while headcopy5[NEXT] != None:
            newlist.append(headcopy5[VALUE])
            headcopy5 = list.copy(headcopy5[NEXT])
        index = len(newlist)-1
        head = tail = [newlist[index], None]
        index = index - 1
        while index >= 0:
            head = [newlist[index], head]
            index = index - 1
        return head, tail


def search_for_a_value(val):
    if head is None:
        return 'The list is empty'
    else:
        answer = 'False'
        if head[VALUE] == val:
            answer = 'True'
        else:
            headcopy3 = list.copy(head[NEXT])
            while headcopy3[NEXT] != None:
                if headcopy3[VALUE] == val:
                    answer = 'True'
                    break
                headcopy3 = list.copy(headcopy3[NEXT])
                if headcopy3[VALUE] == val:
                    answer = 'True'
                    return answer


# Head and tail (variations 2, 4, 6, 8)
# At the beginning, the linked list is empty, head and tail point nowhere
head = tail = None

# Start adding new elements

head, tail = add_to_back_2(40, head, tail)
head, tail = add_to_back_2(50, head, tail)
head, tail = add_to_back_2(60, head, tail)

head, tail = add_to_front(30, head, tail)
head, tail = add_to_front(20, head, tail)
head, tail = add_to_front(10, head, tail)

print('Head of the list: ', head, ', tail of the list: ', tail)

print('All the elements of the list: ', print_elements_one_by_one(head))

# Enter the index number
print('An element with the chosen index: ', get_an_element_by_index(0))

# Enter the value that you're going to search for
print('"Search for a value"', search_for_a_value(40))

print('The list without the front element: ', remove_an_element_from_the_front(head))

print('The list without the last element: ', remove_an_element_from_the_end(head, tail))
