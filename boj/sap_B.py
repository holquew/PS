import sys
input = sys.stdin.readline

t = int(input())
for case in range(t): 
    main_index = -1
    r, p, d = map(int, input().split())
    names = []
    weights = []
    percentages = []
    for i in range(r): 
        name, weight, percentage = input().rstrip().split()
        if float(percentage) == 100.0: 
            main_index = i
        
        names.append(name)
        weights.append(float(weight))
        percentages.append(float(percentage))
    
    k = d/p
    scaled_weight = weights[main_index] * k
    new_percentages = [x*scaled_weight*0.01 for x in percentages]
    
    print(f'Recipe # {case+1}')
    for i in range(r): 
        print(f'{names[i]} {new_percentages[i]:.1f}')
    print('-'*40)


