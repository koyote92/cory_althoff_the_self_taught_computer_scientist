def word_binary_search(array, word_to_find):
    array.sort()
    print(f'Array length: {len(array)}')
    print('Sorted array:')
    print(array)
    start = 0
    end = len(array) - 1
    iter_counter = 0
    while start <= end:
        iter_counter += 1
        mid = (start + end) // 2
        if array[mid] == word_to_find:
            print(f'We found it in {iter_counter} steps.')
            return print(f'{word_to_find} word index in sorted array is: {mid}')
        elif ord(array[mid][0]) < ord(word_to_find[0]):
            start = mid + 1
        elif ord(array[mid][0]) > ord(word_to_find[0]):
            end = mid - 1
        else:
            ord_counter, char_counter = ord(array[mid][0]), 1
            while (ord_counter + ord(array[mid][char_counter])
                   == ord_counter + ord(word_to_find[char_counter])):
                ord_counter += ord(array[mid][char_counter])
                char_counter += 1
            if (ord_counter + ord(array[mid][char_counter])
                    < ord_counter + ord(word_to_find[char_counter])):
                start = mid + 1
            else:
                end = mid - 1
    return


if __name__ == '__main__':
    print('This program sorts an array of words and then perform binary search '
          'of needed word.')
    # Replace the list below with next code to enter your array separated
    # with spaces
    # array = input('Enter your array (separate words with spaces): ').split()
    array = ['word', 'dog', 'ball', 'world', 'book', 'hello', 'program',
             'software', 'system', 'search', 'spam', 'eggs', 'biathlon',
             'bamboo', 'basket', 'baobab', 'bamby', 'python', 'bash',
             'github', 'cory', 'althoff', 'amazing', 'learning', 'science',
             'laptop', 'cheese', 'list', 'word', 'binary', 'search',
             'repository', 'git', 'koyote', 'roman', 'inozemtsev', 'map',
             'library', 'quest', 'challenge', 'cat', 'work', 'fun',
             'example', 'door', 'liquid', 'cup', 'mouse', 'camera',
             'stack', 'pile', 'tree', 'leaf', 'leather', 'paper', 'fox'
             'order', 'button', 'terminal', 'enter', 'space', 'road',
             'task', 'page', 'luck']
    word_to_find = input('Enter a word from array above: ')
    word_binary_search(array, word_to_find)
