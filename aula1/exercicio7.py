from collections import Counter, defaultdict, OrderedDict, namedtuple
frase = "Esta Esta é uma frase que será contada e contada e contada e não sera contada."
contas = Counter(frase.split())
print(contas)
print(contas.most_common(3))