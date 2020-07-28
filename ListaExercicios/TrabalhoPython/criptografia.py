from collections import deque
import pdb


class CircularList:

    def __init__(self, iterable):
        self.values = deque(iterable, len(iterable))

    def shift(self):
        """Performs a right shift. Elements are wrapped around"""
        e = self.values.popleft()
        self.values.append(e)

    def __getitem__(self, index):
        return self.values[index]

    def __repr__(self):
        return str(self.values)

    def __len__(self):
        return len(self.values)

    def full_shift(self):
        """Generator to perform a complete shift through the list,
       yielding an iterable for each combination"""
        circ = CircularList(self.values)
        yield list(circ)
        for _ in range(len(self.values) - 1):
            circ.shift()
            yield list(circ)


def alphabet_shuffle(anchor, alphabets):
    if (len(alphabets[0]) == 0):
        return alphabets
    childs = []
    for alphabet in alphabets:
        new_anchor = alphabet.pop()
        sub_alphabet = alphabet
        shifted_subs = list(CircularList(sub_alphabet).full_shift())
        childs.extend(alphabet_shuffle(new_anchor, shifted_subs))
    return [[anchor] + child for child in childs]


# sigma = [s for s in 'kycbat']
sigma = [s for s in 'abcdefghijklmnopqrstuvwxyz']
encoded_str = 'Sotvadetos'

shuffles = [shuffled[1:] for shuffled in alphabet_shuffle('', list(CircularList(sigma).full_shift()))]
mappers = [{element: image for element, image in zip(sigma, shuffle)} for shuffle in shuffles]
outputs = {''.join(mapper[char] for char in encoded_str) for mapper in mappers}


def printall(output_set):
    for string in sorted(output_set):
        print(string)


printall(outputs)