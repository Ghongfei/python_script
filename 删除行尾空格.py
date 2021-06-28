import os
import shutil
for txtfile in os.listdir('C:/Users/Administrator/Desktop/output2_'):
    # if txtfile.split('.')[1] == 'txt':
    #     f = open('C:/Users/Administrator/Desktop/output2/' + txtfile)
    #
    #
    #
    #     fout = open('C:/Users/Administrator/Desktop/output2_/' + txtfile, 'w')
    #     for line in f:
    #         print(line)
    #         fout.write(line.strip() + '\n')

    size = os.path.getsize('C:/Users/Administrator/Desktop/output2_/' + txtfile)
    if size == 0:
        shutil.move('C:/Users/Administrator/Desktop/output2_/' + txtfile, 'C:/Users/Administrator/Desktop/output2__/' + txtfile)

