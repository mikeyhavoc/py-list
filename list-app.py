#!/usr/bin/env python

# App: List application
# author: Michael Williams
# Date: 2018-12-11
# version: 1.0.0


def welcome_prompt():
    print('*' * 30)
    print('Welcome to the List app')
    print('1. when ready you can enter an item.')
    print('2. Anytime you need help just type "help"')
    print('3. if you want to see the list at any time Enter "listing".')
    print('4. if you want to "delete" an item, enter "del [item name]"')
    print('5. once done, enter "done" and we will print out your list.')
    print('Happy Listing :)')
    print('*' * 30)


def help_screen():
    print('*' * 25)
    print('Help File')
    print('1. when ready you can enter an item.')
    print('2. Anytime you need help just type "help"')
    print('3. if you want to see the list at any time Enter "list".')
    print('4. if you want to "delete" an item, enter "del [item name]"')
    print('5. once done, enter "done" and we will print out your list.')
    print('*' * 25)


def item_list(lists):
    listing = lists.copy() # prints out full list.
    for item in listing:
        print(item)


def list_count(items):
    count = len(items)
    return count


def list_complete(items):
    listing = items.copy()
    for num, item in enumerate(listing):
        print('{}# {}'.format(num + 1, item))


def delete_item(item, items):
    if item in items:
        items.remove(item)
    else:
        print('{} not found'.format(item))


def master():
    items = list()
    welcome_prompt()
    while True:
        new_item = input('add > ').lower()
        if new_item == 'help':  # HELP | help info given.
            help_screen()
        elif new_item == 'list':  # LIST | serves listing so far.
            item_list(items)
            continue
        elif new_item.startswith('del'):
            new_string = new_item[3:]
            word = new_string.strip()
            delete_item(word, items)
            continue
        elif new_item == 'done':  # COMPLETE | serves number of items and items.
            list_complete(items)
            break

        else:
            items.append(new_item)
            num_items = list_count(items)
            print('you have {} items so far.'.format(num_items))


if __name__ == '__main__':
    master()
