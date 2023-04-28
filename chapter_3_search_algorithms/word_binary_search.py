def word_binary_search(array: list, word_to_find: str):
    array.sort()
    print(f'Array length: {len(array)}')
    print(f'Sorted array: {array}')
    start, end = 0, len(array) - 1
    iter_counter = 0

    while start <= end:
        iter_counter += 1
        mid = (start + end) // 2
        mid_first_char_ord = ord(array[mid][0])
        word_to_find_first_char_ord = ord(word_to_find[0])

        if array[mid] == word_to_find:
            print(f'We found it in {iter_counter} steps.')
            return print(f'"{word_to_find}" word index'
                         f' in sorted array is: {mid}')
        elif mid_first_char_ord < word_to_find_first_char_ord:
            start = mid + 1
        elif mid_first_char_ord > word_to_find_first_char_ord:
            end = mid - 1

        else:
            ord_counter, char_index = mid_first_char_ord, 1
            while (ord_counter + ord(array[mid][char_index])
                   == ord_counter + ord(word_to_find[char_index])):
                ord_counter += ord(array[mid][char_index])
                char_index += 1
            if (ord_counter + ord(array[mid][char_index])
                    < ord_counter + ord(word_to_find[char_index])):
                start = mid + 1
            else:
                end = mid - 1
    return print(f'"{word_to_find}" is not in array')


if __name__ == '__main__':
    print('This program sorts an array of words and then perform binary'
          ' search of needed word.')
    # Replace the list below with the next code to enter your own array separated
    # with spaces
    # array_of_words = input('Enter your array (separate words with spaces): ').split()
    array_of_words = ['word', 'dog', 'ball', 'world', 'book', 'hello',
                      'program', 'software', 'system', 'search', 'spam',
                      'eggs', 'biathlon', 'bamboo', 'basket', 'baobab',
                      'bamby', 'python', 'bash', 'github', 'cory', 'althoff',
                      'amazing', 'learning', 'science', 'laptop', 'cheese',
                      'list', 'word', 'binary', 'search', 'repository', 'git',
                      'koyote', 'roman', 'inozemtsev', 'map', 'library',
                      'quest', 'challenge', 'cat', 'work', 'fun', 'example',
                      'door', 'liquid', 'cup', 'mouse', 'camera', 'stack',
                      'pile', 'tree', 'leaf', 'leather', 'paper', 'order',
                      'button', 'terminal', 'enter', 'space', 'road', 'task',
                      'page', 'luck']
    needed_word = input('Enter a word from array above: ')
    word_binary_search(array_of_words, needed_word)
