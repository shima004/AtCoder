# itertools

## 累積和

```
ary = [1, 3, 5, 7, 9]
cumsum = itertools.accumulate(ary)
-> [1, 4, 9, 16, 25]
```

## 値が何個あるか

```
bi = [0,0,0,1,1,0,0,0,1,1,0,1]
gr = itertools.groupby(bi)
for key, group in gr:
  print(f'{key}: {list(group)}')

# 0: [0, 0, 0]
# 1: [1, 1]
# 0: [0, 0, 0]
# 1: [1, 1]
# 0: [0]
# 1: [1]
```

## 順列

```
print(list(itertools.permutations([1, 2, 3])))
# -> [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
```

## 組み合わせ

```
print(list(itertools.combinations([1, 2, 3], 2)))
# -> [(1, 2), (1, 3), (2, 3)]
```

## 直積

```
print(list(itertools.product([0,1], repeat=3)))
# -> [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
```
