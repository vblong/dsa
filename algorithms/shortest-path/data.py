nodes = ['a', 'b', 'c', 'e', 'd']
edges = {
    'a': [
        ('b', 2),
    ],
    'b': [
        ('c', 5),
    ],
    'c': [
        ('b', 5),
        ('e', 1)
    ],
    'd': [
        ('e', 20),
    ],
    'e': [
        ('b', 2)
    ]
}