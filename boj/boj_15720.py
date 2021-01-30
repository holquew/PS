b, c, d = map(int, input().split())
burger = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))

worst = sum(burger) + sum(side) + sum(drink)
best = 0
count = min(min(len(burger), len(side)), len(drink))

for i in range(count): 
    best += (max(burger) * 0.9 + max(side) * 0.9 + max(drink) * 0.9)
    burger.remove(max(burger))
    side.remove(max(side))
    drink.remove(max(drink))

best += sum(burger) + sum(side) + sum(drink)

print(worst, int(best), sep='\n')

