#  Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
#  Сколько журавликов сделал каждый ребенок, если известно,
#  что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
#   чем Петя и Сережа вместе?


s = int(input('ВВедите количество журавликов: '))
k = (s // 3) * 2
p = (s - k) // 2
c = p

print(
    f'Петя сделал {p} журавликов, Катя сделала {k} журавликов, Сережа сделал {c} журавликов')
