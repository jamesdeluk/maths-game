import random
from time import time

print('\nWelcome!\n')

round=1

while True:
    print('Select mode:')
    print('[1] Addition')
    print('[2] Subtraction')
    print('[3] Multiplication')
    print('[4] Division')
    print('[5] Divisible?')
    print('[6] Shuffle (default)')
    print('\n')
    choice=input('Choice: ')
    print('\n')
    score=0
    total_time=0
    start=0.0

    print(f'Round {round}\n')

    if choice == '1':
        rounds=input('Number of rounds [default 10]:\t')
        if rounds == '':
            r=10
        else:
            r=int(rounds)
        first=input('First number [default 1-9999]:\t')
        if first == '':
            f1=1
            f2=9999
        else:
            f1=int(first.split('-')[0])
            f2=int(first.split('-')[1])
        second=input('Second number [default 1-9999]:\t')
        if second == '':
            s1=1
            s2=9999
        else:
            s1=int(second.split('-')[0])
            s2=int(second.split('-')[1])
        tol=input('Tolerance % [default ±0]:\t')
        if tol == '':
            t1=1
            t2=1
        else:
            t1=((100-float(tol))/100)
            t2=((100+float(tol))/100)
        start=time()
        print('\n')
        for i in range(r):
            a=random.randint(f1,f2)
            b=random.randint(s1,s2)
            c=a+b
            ans=input(f'{i+1}: {a} + {b} = ')
            if ans == '':
                print(f'Incorrect: {a} + {b} = {c}\n')
            elif ans == 'end':
                break
            elif ans == c:
                print('Perfect!\n')
                score+=1
            elif float(ans)*t1 <= c <= float(ans)*t2:
                print('Correct\n')
                score+=1
            else:
                print(f'Incorrect: {a} + {b} = {c}\n')
        end=time()
        session_time=end-start
        total_time+=session_time
        print(f'Score: {score} / {r}')
        print(f'{int(((session_time)/60)*10)/10} minutes')
        if score > 0:
            print(f'{int(((session_time)/score)*10)/10} seconds per correct answer')
        print('\n')
    elif choice == '2':
        rounds=input('Number of rounds [default 10]:\t')
        if rounds == '':
            r=10
        else:
            r=int(rounds)
        first=input('First number [default 1-9999]:\t')
        if first == '':
            f1=1
            f2=9999
        else:
            f1=int(first.split('-')[0])
            f2=int(first.split('-')[1])
        second=input('Second number [default 1-9999]:\t')
        if second == '':
            s1=1
            s2=9999
        else:
            s1=int(second.split('-')[0])
            s2=int(second.split('-')[1])
        tol=input('Tolerance % [default ±0]:\t')
        if tol == '':
            t1=1
            t2=1
        else:
            t1=((100-float(tol))/100)
            t2=((100+float(tol))/100)
        start=time()
        print('\n')
        for i in range(r):
            a=random.randint(f1,f2)
            b=random.randint(s1,s2)
            c=a-b
            ans=input(f'{i+1}: {a} - {b} = ')
            if ans == '':
                print(f'Incorrect: {a} - {b} = {c}\n')
            elif ans == 'end':
                break
            elif ans == c:
                print('Perfect!\n')
                score+=1
            elif float(ans)*t1 <= c <= float(ans)*t2:
                print('Correct\n')
                score+=1
            else:
                print(f'Incorrect: {a} - {b} = {c}\n')
        end=time()
        session_time=end-start
        total_time+=session_time
        print(f'Score: {score} / {r}')
        print(f'{int(((session_time)/60)*10)/10} minutes')
        if score > 0:
            print(f'{int(((session_time)/score)*10)/10} seconds per correct answer')
        print('\n')
    elif choice == '3':
        rounds=input('Number of rounds [default 10]:\t')
        if rounds == '':
            r=10
        else:
            r=int(rounds)
        first=input('First number [default 3-99]:\t')
        if first == '':
            f1=3
            f2=99
        else:
            f1=int(first.split('-')[0])
            f2=int(first.split('-')[1])
        second=input('Second number [default 3-99]:\t')
        if second == '':
            s1=3
            s2=99
        else:
            s1=int(second.split('-')[0])
            s2=int(second.split('-')[1])
        tol=input('Tolerance % [default ±0]:\t')
        if tol == '':
            t1=1
            t2=1
        else:
            t1=((100-float(tol))/100)
            t2=((100+float(tol))/100)
        start=time()
        print('\n')
        for i in range(r):
            a=random.randint(f1,f2)
            b=random.randint(s1,s2)
            c=a*b
            ans=input(f'{i+1}: {a} * {b} = ')
            if ans == '':
                print(f'Incorrect: {a} * {b} = {c}\n')
            elif ans == 'end':
                break
            elif float(ans) == float(c):
                print('Perfect!\n')
                score+=1
            elif float(ans)*t1 <= c <= float(ans)*t2:
                print('Correct\n')
                score+=1
            else:
                print(f'Incorrect: {a} * {b} = {c}\n')
        end=time()
        session_time=end-start
        total_time+=session_time
        print(f'Score: {score} / {r}')
        print(f'{int(((session_time)/60)*10)/10} minutes')
        if score > 0:
            print(f'{int(((session_time)/score)*10)/10} seconds per correct answer')
        print('\n')
    elif choice == '4':
        rounds=input('Number of rounds [default 10]:\t')
        if rounds == '':
            r=10
        else:
            r=int(rounds)
        first=input('First number [default 99-999]:\t')
        if first == '':
            f1=99
            f2=999
        else:
            f1=int(first.split('-')[0])
            f2=int(first.split('-')[1])
        second=input('Second number [default 2-19]:\t')
        if second == '':
            s1=2
            s2=19
        else:
            s1=int(second.split('-')[0])
            s2=int(second.split('-')[1])
        tol=input('Tolerance % [default ±1]:\t')
        if tol == '':
            t1=0.99
            t2=1.01
        else:
            t1=((100-float(tol))/100)
            t2=((100+float(tol))/100)
        print('\n')
        start=time()
        for i in range(r):
            a=random.randint(f1,f2)
            b=random.randint(s1,s2)
            c=a/b
            ans=input(f'{i+1}: {a} / {b} = ')
            if ans == '':
                print(f'Incorrect: {a} / {b} = {c}\n')
            elif ans == 'end':
                break
            elif float(ans) == float(c):
                print('Perfect!\n')
                score+=1
            elif float(ans)*t1 <= c <= float(ans)*t2:
                print(f'Correct [{a/b}]\n')
                score+=1
            else:
                print(f'Incorrect: {a} / {b} = {c}\n')
        end=time()
        session_time=end-start
        total_time+=session_time
        print(f'Score: {score} / {r}')
        print(f'{int(((session_time)/60)*10)/10} minutes')
        if score > 0:
            print(f'{int(((session_time)/score)*10)/10} seconds per correct answer')
        print('\n')
    elif choice == '5':
        rounds=input('Number of rounds [default 10]:\t\t')
        if rounds == '':
            r=10
        else:
            r=int(rounds)
        dividend=input('Dividend range [default 99-999]:\t')
        if dividend == '':
            f1=99
            f2=999
        else:
            f1=int(dividend.split('-')[0])
            f2=int(dividend.split('-')[1])
        divisor=input('Divisor range [default 2-9]:\t\t')
        if divisor == '':
            s1=2
            s2=9
        else:
            s1=int(divisor.split('-')[0])
            s2=int(divisor.split('-')[1])
        print('\n')
        start=time()
        for i in range(r):
            a=random.randint(f1,f2)
            b=random.randint(s1,s2)
            c=a/b
            ans=input(f'{i+1}: Is {a} perfectly divisible by {b}? [y/n]: ')
            if ans == '':
                print(f'{a} / {b} = {c}\n')
            elif ans == 'end':
                break
            elif a%b == 0.0 and ans == 'y':
                print(f'Correct: {a} / {b} = {int(c)} r {a%b}\n')
                score+=1
            elif a%b == 0.0 and ans == 'n':
                print(f'Incorrect: {a} / {b} = {int(c)} r {a%b}\n')
            elif a%b != 0.0 and ans == 'y':
                print(f'Incorrect: {a} / {b} = {int(c)} r {a%b}\n')
            elif a%b != 0.0 and ans == 'n':
                print(f'Correct: {a} / {b} = {int(c)} r {a%b}\n')
                score+=1
            else:
                print(f'Incorrect: {a} / {b} = {int(c)} r {a%b}\n')
        end=time()
        session_time=end-start
        total_time+=session_time
        print(f'Score: {score} / {r}')
        print(f'{int(((session_time)/60)*10)/10} minutes')
        if score > 0:
            print(f'{int(((session_time)/score)*10)/10} seconds per correct answer')
        print('\n')
    elif choice == 'end':
        print('End\n')
    else:
        start=time()
        r=25
        for i in range(r):
            func=random.randint(0,3)
            if func==0:
                a=random.randint(1,9999)
                b=random.randint(1,9999)
                c=a+b
                ans=input(f'{i+1}: {a} + {b} = ')
                if ans == '':
                    print(f'Incorrect: {a} + {b} = {c}\n')
                elif ans == 'end':
                    break
                elif int(ans) == c:
                    print('Perfect!\n')
                    score+=1
                else:
                    print(f'Incorrect: {a} + {b} = {c}\n')
            elif func==1:
                a=random.randint(1,9999)
                b=random.randint(1,9999)
                c=a-b
                ans=input(f'{i+1}: {a} - {b} = ')
                if ans == '':
                    print(f'Incorrect: {a} - {b} = {c}\n')
                elif ans == 'end':
                    break
                elif int(ans) == c:
                    print('Perfect!\n')
                    score+=1
                else:
                    print(f'Incorrect: {a} - {b} = {c}\n')
            elif func==2:
                a=random.randint(3,99)
                b=random.randint(3,99)
                c=a*b
                ans=input(f'{i+1}: {a} * {b} = ')
                if ans == '':
                    print(f'Incorrect: {a} * {b} = {c}\n')
                elif ans == 'end':
                    break
                elif float(ans) == float(c):
                    print('Perfect!\n')
                    score+=1
                else:
                    print(f'Incorrect: {a} * {b} = {c}\n')
            elif func==3:
                a=random.randint(99,999)
                b=random.randint(2,19)
                c=a/b
                ans=input(f'{i+1}: {a} / {b} = ')
                if ans == '':
                    print(f'Incorrect: {a} / {b} = {c}\n')
                elif ans == 'end':
                    break
                elif float(ans) == float(c):
                    print('Perfect!\n')
                    score+=1
                elif float(ans)*0.99 <= c <= float(ans)*1.01:
                    print(f'Correct [{a/b}]\n')
                    score+=1
                else:
                    print(f'Incorrect: {a} / {b} = {c}\n')
        end=time()
        session_time=end-start
        total_time+=session_time
        print(f'Score: {score} / {r}')
        print(f'{int(((session_time)/60)*10)/10} minutes')
        print(f'Avg {int(((session_time)/r)*10)/10} seconds per answer')
        if score > 0:
            print(f'Avg {int(((session_time)/score)*10)/10} seconds per correct answer')
        print('\n')
    play=input("Play again? [y/n]: ")
    if play == 'n':
        break
    else:
        round+=1
        print('\n')
        continue

print('\nThanks!')
print(f'Total time: {int(((total_time)/60)*10)/10} minutes\n')