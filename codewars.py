# 1:
import itertools
import re


def numbers(str_arr):
    str_arr = re.sub('[^0-9]', '', str_arr)
    a = (min(str_arr))
    b = str_arr.replace(max(str_arr), '')
    return str(max(b)) + str(a)


print numbers('1234ds8s9')


# --------------------
# 2:
def move(letter):
    if letter.lower() == 'z':
        return unichr(97)
    return unichr(ord(letter.lower()) + 1)


def num(s):
    result = ''
    for ch in s:
        if ch.isalpha():
            if ch.lower() == 'z' or ch.lower() == 'd' or ch.lower() == 'h' or ch.lower() == 'n':
                if ch == 'z':
                    new_ch = unichr(97)
                else:
                    new_ch = unichr(ord(ch.lower()) + 1)
                result += ch.replace(ch, new_ch.upper())
            else:
                result += ch.replace(ch, unichr(ord(ch.lower()) + 1))
        else:
            result += ch

    return result


print num('z4a c')


# --------------
# 3:
def word(str_arr):
    str_arr = str_arr.split(' ')
    sort = sorted(str_arr, key=len)
    return str(sort[-1]).strip(',')


print word("one two three longggg")


# 1
"""dano vsi parni i odne ne parne chisla abo navpaki(minimum 3), znaiti tse chislo"""


def find_outlier(*integers):
    odd_arg, even_arg = [], []
    if len(integers) < 3:
        return None
    for i in integers:
        even_arg.append(i) if (i % 2 != 0) else odd_arg.append(i)
    return odd_arg[0] if (len(odd_arg) < len(even_arg)) else even_arg[0]


print find_outlier(2, 2, 4, 7)


# 2
"""dano vsi parni i odne ne parne chisla abo navpaki, znaiti indexs tsogo chisla(index: 1,2,3,..)"""


def iq_test(numbers):
    numbers = numbers.split(' ')  # n = [int(i)%2 for i in n.split()] (au use this...easier)
    odd_arg, even_arg = [], []
    for i in numbers:
        even_arg.append(i) if (int(i) % 2 != 0) else odd_arg.append(i)
    result = odd_arg[0] if (len(odd_arg) < len(even_arg)) else even_arg[0]
    return numbers.index(result) + 1


print iq_test('10 2 4 61 8')


# 3
"""chisla trivoni"""


def fibo(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))

    return signature[:n]


print (fibo([1, 1, 1], 6))


# 4
"""verniti chisla do 'm' / vsi chisla"""


def printer_error(s):
    errors = 0
    for i in s:
        errors += 1 if (i > chr(109)) else 0
    return str(errors) + "/" + str(len(s))


print printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")


# 5
"""Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built 
with the sides of given length and false in any other case. """


def is_triangle(a, b, c):
    return True if (a + b > c and a + c > b and b + c > a) else False


print is_triangle(1, 2, 2)


# 6
"""Given an array, find the int that appears an odd number of times. There will always be only one integer that 
appears an odd number of times. """


def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


print find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])

# 7
"""Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
    Rules for a smiling face:
        -Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
        -A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
        -Every smiling face must have a smiling mouth that should be marked with either ) or D.
    No additional characters are allowed except for those mentioned.
    Valid smiley face examples:
        :) :D ;-D :~)
    Invalid smiley faces:
        ;( :> :} :] """


def count_smileys(arr):
    start_ch, middle_ch, end_ch = [':', ';'], ['-', '~'], [')', 'D']
    count_of_smileys = 0
    for smile in arr:
        if smile.startswith(start_ch[0]) == 1 or smile.startswith(start_ch[1]) == 1:
            if smile.endswith(end_ch[0]) == 1 or smile.endswith(end_ch[1]) == 1:
                if len(smile) == 3:
                    if smile[1:2].count(middle_ch[0]) == 1 or smile[1:2].count(middle_ch[1]) == 1:
                        count_of_smileys += 1
                elif len(smile) == 2:
                    count_of_smileys += 1
    return count_of_smileys


print count_smileys([';)', ':-D', ':-*D'])

# 8
"""You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create 
the text that should be displayed next to such an item. Implement a function likes :: [String] -> String, which must take in input array, containing the 
names of people who like an item. It must return the display text as shown in the examples:"""


def likes(names):
    l_t = ' like this'
    if len(names) >= 0:
        if len(names) == 0:
            return 'no one' + ' likes this'
        elif len(names) == 1:
            return names[0] + ' likes this'
        elif len(names) == 2:
            return names[0] + ' and ' + names[1] + l_t
        elif len(names) == 3:
            return names[0] + ', ' + names[1] + ' and ' + names[2] + l_t
        else:
            return names[0] + ', ' + names[1] + ' and ' + str(len(names)-2) + ' others' + l_t


print (likes([]))
print (likes(['Peter']))
print (likes(['Jacob', 'Alex']))
print (likes(['Max', 'John', 'Mark']))
print (likes(['Alex', 'Jacob', 'Mark', 'Max']))


# 9
"""Build Tower by the following given argument:
number of floors (integer and always greater than 0). For example, a tower of 3 and 6 floors looks like below
3 floors            6 floors
[                   [
  '  *  ',            '     *     ', 
  ' *** ',            '    ***    ',
  '*****'             '   *****   ', 
]                     '  *******  ', 
                      ' ********* ', 
                      '***********'
                    ]"""


def tower_builder(n_floors):
    tower = []
    floor = 1
    if n_floors > 0:
        while floor < n_floors+1:
            next_floor = (floor * '**')
            if len(next_floor) % 2 == 0:
                tower.append(next_floor[0:-1])
            else:
                tower.append(next_floor)
            floor += 1
    size = len(tower)
    floor_size = 0
    while floor_size < n_floors:
        tower[floor_size] = tower[floor_size].replace(tower[floor_size], str((size-1)*' ') + tower[floor_size] + str((size-1)*' '))
        floor_size += 1
        size = size-1

    return tower


print (tower_builder(5))


# 10
"""Write simple .camelCase method  for strings. All 
words must have their first letter capitalized without spaces. 
For instance: 
    camelcase("hello case") => HelloCase
    camelcase("camel case word") => CamelCaseWord"""


def camel_case(string):
    string = string.split(' ')
    if string.count('') > 0:
        string.remove('')
    count, result = 0, ''

    while len(string) > count:
        string.append(string[0][0].upper() + string[0][1:])
        string.remove(string[0])
        count += 1
    for i in string:
        result += i

    return result  # easy solution) all fuck is: -> return string.title().replace(' ', '') <-


print camel_case("test case ")


# 11
"""A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence 
"The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is 
irrelevant). Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore 
numbers and punctuation. """


def is_pangram(s):
    i = 97   # can use 'string.ascii_lowercase' as alphabet
    while 123 > i:
        if s.lower().count(unichr(i)) != 0:
            i += 1
        else:
            return False
    return True


print (is_pangram("The quick, brown fox jumps over the lazy dog!"))


# 12
"""A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.
He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).
His mother looks out of a window 1.5 meters from the ground.
How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?

Three conditions must be met for a valid experiment:
*Float parameter "h" in meters must be greater than 0
*Float parameter "bounce" must be greater than 0 and less than 1
*Float parameter "window" must be less than h.
If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

Note:
The ball can only be seen if the height of the rebounding ball is stricty greater than the window parameter.

Example:
* h = 3, bounce = 0.66, window = 1.5, result is 3
* h = 3, bounce = 1, window = 1.5, result is -1 

(Condition 2) not fulfilled)."""


def bouncingBall(h, bounce, window):

    if h > 0 and 0 < bounce < 1 and window < h:
        count = 1
        while h >= window:
            h = h*bounce
            if h > window:
                count += 2
        return count
    else:
        return -1


print bouncingBall(30, 0.66, 1.5)


# 13
"""Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  "" """


def order(sentence):  # easy answer return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))
    if len(sentence) > 0:
        sentence = sentence.split(' ')
        new_sen, result, i = [], '', 0
        while i < 10:
            for word in sentence:
                new_sen.insert(int(re.sub('[^0-9]', '', word))-1, word)
            sentence = new_sen
            new_sen = []
            i += 1
        for ch in sentence:
            result += ch + ' '

        return result[0:-1]
    else:
        return ''


print (order("o6over on8e 4come or1 nex7t b3ut las5t tak2e"))


# 14
"""The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:
*It must start with a hashtag (#).
*All words must have their first letter capitalized.
*If the final result is longer than 140 chars it must return false.
*If the input or the result is an empty string it must return false.

Examples:
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false"""


def generate_hashtag(s):
    return '#' + s.title().replace(' ', '') if (0 < len(s) < 140) else False


print (generate_hashtag('Codewars'))  # Codewars, 'Should handle a single word.'


# 15
"""Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you 
help him to find out, how many cakes he could bake considering his recipes? Write a function cakes(), which takes the 
recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake 
(integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 
200). Ingredients that are not present in the objects, can be considered as 0. Examples: 

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})"""


def cakes(recipe, available):
    count = []
    for need_type, need_count in recipe.items():
        i = available.get(need_type)
        if i is None:
            return 0
        count.append(int(i/need_count))
    return min(count)


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print cakes(recipe, available)  # expected 2


# 16
"""John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper a list of distances 
between these towns. ls = [50, 55, 57, 58, 60]. John is tired of driving and he says to Mary that he doesn't want to 
drive more than t = 174 miles and he will visit only 3 towns. 

Which distances, hence which towns, they will choose so that the sum of the distances is the biggest possible

to please Mary and John- ?
Example:

With list ls and 3 towns to visit they can make a choice between: [50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,
60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60]. 

The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

The biggest possible sum taking a limit of 174 into account is then 173 and the distances of the 3 corresponding towns is [55, 58, 60].

The function chooseBestSum (or choose_best_sum or ... depending on the language) will take as parameters t (maximum 
sum of distances, integer >= 0), k (number of towns to visit, k >= 1) and ls (list of distances, all distances are 
positive or null integers and this list has at least one element). The function returns the "best" sum ie the biggest 
possible sum of k distances less than or equal to the given limit t, if that sum exists, or otherwise nil, null, 
None, Nothing, depending on the language. With C++, C, Rust, Swift, Go, Kotlin return -1. 

Examples:

ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163

xs = [50] choose_best_sum(163, 3, xs) -> nil (or null or ... or -1 (C++, C, Rust, Swift, Go)

ys = [91, 74, 73, 85, 73, 81, 87] choose_best_sum(230, 3, ys) -> 228"""


def choose_best_sum(t, k, ls):
    correct_distant = []
    for i in itertools.combinations(ls, k):
        total_distance = sum(i)
        if total_distance <= t:
            correct_distant.append(total_distance)

    return max(correct_distant) if len(correct_distant) > 0 else None


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(choose_best_sum(880, 8, xs), 876)
print(choose_best_sum(230, 4, xs), 230)
print(choose_best_sum(430, 5, xs), 430)
print(choose_best_sum(10, 1, xs), None)


# 17
"""Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
For example:
* domain_name("http://github.com/carbonfive/raygun") == "github"
* domain_name("http://www.zombie-bites.com") == "zombie-bites"
* domain_name("https://www.cnet.com") == "cnet" """


def domain_name(url):
    standard_start = ['http://www.', 'https://www.', 'http://', 'https://', 'www.']
    for starts in standard_start:
        if url.__contains__(starts):
            url = url.replace(starts, '')
    return url[:url.index('.')]


print (domain_name("http://google.com"), "google")
print (domain_name("http://google.co.jp"), "google")
print (domain_name("www.xakep.ru"), "xakep")
print (domain_name("https://youtube.com"), "youtube")


# 18
"""In this kata, you will write a function that returns the positions and the values of the "peaks" (or local maxima) 
of a numeric array. For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since 
arr[3] equals 5). The output will be returned as an object with two properties: pos and peaks. Both of these 
properties should be arrays. If there is no peak in the given array, then the output should be {pos: [], peaks: []}. 
Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in 
other languages) All input arrays will be valid integer arrays (although it could still be empty), so you won't need 
to validate the input. The first and last elements of the array will not be considered as peaks (in the context of a 
mathematical function, we don't know what is after and before and therefore, we don't know if it is a peak or not). 
Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] does not. In case of a plateau-peak, 
please only return the position and value of the beginning of the plateau. For example: pickPeaks([1, 2, 2, 2, 
1]) returns {pos: [1], peaks: [2]} (or equivalent in other languages) 

Have fun!"""


def pick_peaks(arr):  # work in 90% cases
    pos = []
    peaks = []
    i = 1
    while i < len(arr) - 1:
        if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
            pos.append(i)
            peaks.append(arr[i])
        elif arr[i+1]:
            if arr[i - 1] < arr[i] == arr[i + 1] >= arr[i+2]:
                for x in range(arr[i], arr[-1]):
                    if arr[x+1]:
                        if arr[x] < arr[x+1]:
                            return {'pos': [], 'peaks': []}
                if arr[-1] == arr[i]:
                    break
                pos.append(i)
                peaks.append(arr[i])
        i += 1

    return {'pos': pos, 'peaks': peaks}


print (pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]), {"pos": [3, 7], "peaks": [6, 3]})
print (pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]), {"pos": [3, 7], "peaks": [6, 3]})
print (pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]), {"pos": [3, 7, 10], "peaks": [6, 3, 2]})
print (pick_peaks([2, 1, 3, 1, 2, 2, 2, 2, 1]), {"pos": [2, 4], "peaks": [3, 2]})
print (pick_peaks([2, 1, 3, 1, 2, 2, 2, 2]), {"pos": [2], "peaks": [3]})
