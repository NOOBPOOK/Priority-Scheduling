#TAKE INPUT
process = []
old = []
print("Enter The Number of Processes")
n = int(input())
print("Which tecnique to use \n1.Non-Preemptive\n2.Preemptive")
g = int(input())
print("Enter Arrival Time, Burst Time and Priority Of Each Process")
for i in range(1,n+1):
    print(f"For P{i}")
    k = list(map(int,input().split()))
    process.append([i-1,k[0],k[1],k[2]])
    old.append([i-1,k[0],k[1],k[2]])
    
comp_time = 0
comp = list(range(n))
con = 0
que = []
prev_comp = 0

process.sort(key=lambda x:x[1])

if g == 1:
    print("\n\nGnatt chart is as follows:\n")
    while con < n:
        buffer = []
        for i in process:
            if i[1] in range(prev_comp,comp_time+1):
                buffer.append(i)
        for g in buffer:
            process.remove(g)
            que.append(g)

        if len(que) == 0:
            comp_time += 1
        
        else:
            prev_comp = comp_time
            mn = 1000
            op = que[0]
            for y in que:
                if y[3]<mn:
                    op = y
                    mn = y[3]
            comp_time += op[2]
            print(f"Time {prev_comp}-{comp_time} -->  Process {op[0]+1}")
            comp[op[0]] = comp_time
            que.remove(op)
            con += 1

    print("\n\nThe answer is:\n\n")
    print("-"*73)
    print("|Process    |Arrival    |Burst      |Priority   |TurnAround |Waiting    |")
    print("-"*73)
    wait = []
    turn = []
    for x in old:
        print(f"|Process {x[0]+1}" + " "*(3-len(str(x[0]))),end = "|")
        print(f"{x[1]}" + " "*(11-len(str(x[1]))),end = "|")
        print(f"{x[2]}" + " "*(11-len(str(x[2]))),end = "|")
        print(f"{x[3]}" + " "*(11-len(str(x[3]))),end = "|")
        llp = comp[x[0]]
        turn.append(llp - x[1])
        wait.append(llp - x[1] - x[2])
        print(f"{llp - x[1]}" + " "*(11-len(str(llp - x[1]))),end = "|")
        print(f"{llp - x[1] - x[2]}" + " "*(11-len(str(llp - x[1] - x[2]))),end = "|\n")
        print("-"*73)
                
    print(f"\nAverage TurnAround Time : {sum(turn)/n}")
    print(f"\nAverage Waiting Time : {sum(wait)/n}")

else:
    print(f"\n\nGnatt chart is as follows:\n")
    while con < n:
        print(f"Time {comp_time} --> ",end="")
        buffer = []
        for i in process:
            if i[1] in range(prev_comp,comp_time+1):
                buffer.append(i)
        for g in buffer:
            process.remove(g)
            que.append(g)

        if len(que) == 0:
            comp_time += 1
            print(f"Not Allocated")
            continue
        
        else:
            prev_comp = comp_time
            mn = 1000
            op = que[0]
            id = 0
            for y in que:
                if y[3]<mn:
                    op = y
                    mn = y[3]
                    id = que.index(y)
            print(f"Process {op[0]+1}")
            que[id][2] -= 1
            comp_time += 1
            if que[id][2] == 0:
                comp[op[0]] = comp_time
                que.remove(op)
                con += 1
    
    print("\n\nThe answer is:\n\n")
    print("-"*73)
    print("|Process    |Arrival    |Burst      |Priority   |TurnAround |Waiting    |")
    print("-"*73)
    wait = []
    turn = []
    for x in old:
        print(f"|Process {x[0]+1}" + " "*(3-len(str(x[0]))),end = "|")
        print(f"{x[1]}" + " "*(11-len(str(x[1]))),end = "|")
        print(f"{x[2]}" + " "*(11-len(str(x[2]))),end = "|")
        print(f"{x[3]}" + " "*(11-len(str(x[3]))),end = "|")
        llp = comp[x[0]]
        turn.append(llp - x[1])
        wait.append(llp - x[1] - x[2])
        print(f"{llp - x[1]}" + " "*(11-len(str(llp - x[1]))),end = "|")
        print(f"{llp - x[1] - x[2]}" + " "*(11-len(str(llp - x[1] - x[2]))),end = "|\n")
        print("-"*73)
                
    print(f"\nAverage TurnAround Time : {sum(turn)/n}")
    print(f"\nAverage Waiting Time : {sum(wait)/n}")
    
