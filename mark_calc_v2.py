print('')

mark = []
weight = []
category = []
final = [0,0,0,0,[],[],[],[]]
SECTIONS = [0.3, 0.2, 0.3, 0.2] # (Application, Communication, Knowledge, Thinking)
counter = 0
course_mark = 0

print('Mark? ')
while True:
    x = input()
    if x == '':
        break
    mark.append(int(x))

print('Weight? ')
while True:
    x = input()
    if x == '':
        break
    weight.append(float(x))

print('Category? ')
while True:
    x = input()
    if x == '':
        break
    elif x == 'A':
        category.append(0)
    elif x == 'C':
        category.append(1)
    elif x == 'K':
        category.append(2)
    elif x == 'T':
        category.append(3)

while counter < len(mark):
    final[category[counter]] += mark[counter] * weight[counter] / 100
    final[category[counter]+4].append(weight[counter])
    counter += 1

for i in range(4):
    final[i] = final[i] / sum(final[i+4]) * 100
    course_mark += final[i] * SECTIONS[i]

if len(mark) == len (weight) and len(weight) == len(category):
    print(f'\nApplication: {final[0]}')
    print(f'Communication: {final[1]}')
    print(f'Knowledge: {final[2]}')
    print(f'Thinking: {final[3]}')
    print(f'\nPERCENTAGE: {course_mark}')
else:
    print('ERROR ERROR ERROR')

print('')
