import os
for i in os.listdir('E:/安全帽/安全帽1/'):
    f = open('E:/安全帽/label/' + i.split('.')[0] + '.txt', 'w')

    f.write('')