from tkinter import *
root=Tk()
root.title(" Sudoku Game ")
#root.geometry("460x460")
sudoku_matrix=[]
for row in range(9):
    row_matrix=[]
    for column in range(9):
        row_matrix.append(StringVar)
    sudoku_matrix.append(row_matrix)

def get_show(self):
    for row in range(9):
         for column in range(9):
            sudoku_matrix[row][column]=number_entry_00
    print(sudoku_matrix)

number_entry_00=Entry(root,width=5,textvariable=sudoku_matrix[0][0])
number_entry_01=Entry(root,width=5,textvariable=sudoku_matrix[0][1])
number_entry_02=Entry(root,width=5,textvariable=sudoku_matrix[0][2])
number_entry_03=Entry(root,width=5,textvariable=sudoku_matrix[0][3])
number_entry_04=Entry(root,width=5,textvariable=sudoku_matrix[0][4])
number_entry_05=Entry(root,width=5,textvariable=sudoku_matrix[0][5])
number_entry_06=Entry(root,width=5,textvariable=sudoku_matrix[0][6])
number_entry_07=Entry(root,width=5,textvariable=sudoku_matrix[0][7])
number_entry_08=Entry(root,width=5,textvariable=sudoku_matrix[0][8])
number_entry_00.grid(row=0,column=0)
number_entry_01.grid(row=0,column=1)
number_entry_02.grid(row=0,column=2)
number_entry_03.grid(row=0,column=3)
number_entry_04.grid(row=0,column=4)
number_entry_05.grid(row=0,column=5)
number_entry_06.grid(row=0,column=6)
number_entry_07.grid(row=0,column=7)
number_entry_08.grid(row=0,column=8)
number_entry_10=Entry(root,width=5,textvariable=sudoku_matrix[1][0])
number_entry_11=Entry(root,width=5,textvariable=sudoku_matrix[1][1])
number_entry_12=Entry(root,width=5,textvariable=sudoku_matrix[1][2])
number_entry_13=Entry(root,width=5,textvariable=sudoku_matrix[1][3])
number_entry_14=Entry(root,width=5,textvariable=sudoku_matrix[1][4])
number_entry_15=Entry(root,width=5,textvariable=sudoku_matrix[1][5])
number_entry_16=Entry(root,width=5,textvariable=sudoku_matrix[1][6])
number_entry_17=Entry(root,width=5,textvariable=sudoku_matrix[1][7])
number_entry_18=Entry(root,width=5,textvariable=sudoku_matrix[1][8])
number_entry_10.grid(row=1,column=0)
number_entry_11.grid(row=1,column=1)
number_entry_12.grid(row=1,column=2)
number_entry_13.grid(row=1,column=3)
number_entry_14.grid(row=1,column=4)
number_entry_15.grid(row=1,column=5)
number_entry_16.grid(row=1,column=6)
number_entry_17.grid(row=1,column=7)
number_entry_18.grid(row=1,column=8)
number_entry_20=Entry(root,width=5,textvariable=sudoku_matrix[2][0])
number_entry_21=Entry(root,width=5,textvariable=sudoku_matrix[2][1])
number_entry_22=Entry(root,width=5,textvariable=sudoku_matrix[2][2])
number_entry_23=Entry(root,width=5,textvariable=sudoku_matrix[2][3])
number_entry_24=Entry(root,width=5,textvariable=sudoku_matrix[2][4])
number_entry_25=Entry(root,width=5,textvariable=sudoku_matrix[2][5])
number_entry_26=Entry(root,width=5,textvariable=sudoku_matrix[2][6])
number_entry_27=Entry(root,width=5,textvariable=sudoku_matrix[2][7])
number_entry_28=Entry(root,width=5,textvariable=sudoku_matrix[2][8])
number_entry_20.grid(row=2,column=0)
number_entry_21.grid(row=2,column=1)
number_entry_22.grid(row=2,column=2)
number_entry_23.grid(row=2,column=3)
number_entry_24.grid(row=2,column=4)
number_entry_25.grid(row=2,column=5)
number_entry_26.grid(row=2,column=6)
number_entry_27.grid(row=2,column=7)
number_entry_28.grid(row=2,column=8)
number_entry_30=Entry(root,width=5,textvariable=sudoku_matrix[3][0])
number_entry_31=Entry(root,width=5,textvariable=sudoku_matrix[3][1])
number_entry_32=Entry(root,width=5,textvariable=sudoku_matrix[3][2])
number_entry_33=Entry(root,width=5,textvariable=sudoku_matrix[3][3])
number_entry_34=Entry(root,width=5,textvariable=sudoku_matrix[3][4])
number_entry_35=Entry(root,width=5,textvariable=sudoku_matrix[3][5])
number_entry_36=Entry(root,width=5,textvariable=sudoku_matrix[3][6])
number_entry_37=Entry(root,width=5,textvariable=sudoku_matrix[3][7])
number_entry_38=Entry(root,width=5,textvariable=sudoku_matrix[3][8])
number_entry_30.grid(row=3,column=0)
number_entry_31.grid(row=3,column=1)
number_entry_32.grid(row=3,column=2)
number_entry_33.grid(row=3,column=3)
number_entry_34.grid(row=3,column=4)
number_entry_35.grid(row=3,column=5)
number_entry_36.grid(row=3,column=6)
number_entry_37.grid(row=3,column=7)
number_entry_38.grid(row=3,column=8)
number_entry_40=Entry(root,width=5,textvariable=sudoku_matrix[4][0])
number_entry_41=Entry(root,width=5,textvariable=sudoku_matrix[4][1])
number_entry_42=Entry(root,width=5,textvariable=sudoku_matrix[4][2])
number_entry_43=Entry(root,width=5,textvariable=sudoku_matrix[4][3])
number_entry_44=Entry(root,width=5,textvariable=sudoku_matrix[4][4])
number_entry_45=Entry(root,width=5,textvariable=sudoku_matrix[4][5])
number_entry_46=Entry(root,width=5,textvariable=sudoku_matrix[4][6])
number_entry_47=Entry(root,width=5,textvariable=sudoku_matrix[4][7])
number_entry_48=Entry(root,width=5,textvariable=sudoku_matrix[4][8])
number_entry_40.grid(row=4,column=0)
number_entry_41.grid(row=4,column=1)
number_entry_42.grid(row=4,column=2)
number_entry_43.grid(row=4,column=3)
number_entry_44.grid(row=4,column=4)
number_entry_45.grid(row=4,column=5)
number_entry_46.grid(row=4,column=6)
number_entry_47.grid(row=4,column=7)
number_entry_48.grid(row=4,column=8)
number_entry_50=Entry(root,width=5,textvariable=sudoku_matrix[5][0])
number_entry_51=Entry(root,width=5,textvariable=sudoku_matrix[5][1])
number_entry_52=Entry(root,width=5,textvariable=sudoku_matrix[5][2])
number_entry_53=Entry(root,width=5,textvariable=sudoku_matrix[5][3])
number_entry_54=Entry(root,width=5,textvariable=sudoku_matrix[5][4])
number_entry_55=Entry(root,width=5,textvariable=sudoku_matrix[5][5])
number_entry_56=Entry(root,width=5,textvariable=sudoku_matrix[5][6])
number_entry_57=Entry(root,width=5,textvariable=sudoku_matrix[5][7])
number_entry_58=Entry(root,width=5,textvariable=sudoku_matrix[5][8])
number_entry_50.grid(row=5,column=0)
number_entry_51.grid(row=5,column=1)
number_entry_52.grid(row=5,column=2)
number_entry_53.grid(row=5,column=3)
number_entry_54.grid(row=5,column=4)
number_entry_55.grid(row=5,column=5)
number_entry_56.grid(row=5,column=6)
number_entry_57.grid(row=5,column=7)
number_entry_58.grid(row=5,column=8)
number_entry_60=Entry(root,width=5,textvariable=sudoku_matrix[6][0])
number_entry_61=Entry(root,width=5,textvariable=sudoku_matrix[6][1])
number_entry_62=Entry(root,width=5,textvariable=sudoku_matrix[6][2])
number_entry_63=Entry(root,width=5,textvariable=sudoku_matrix[6][3])
number_entry_64=Entry(root,width=5,textvariable=sudoku_matrix[6][4])
number_entry_65=Entry(root,width=5,textvariable=sudoku_matrix[6][5])
number_entry_66=Entry(root,width=5,textvariable=sudoku_matrix[6][6])
number_entry_67=Entry(root,width=5,textvariable=sudoku_matrix[6][7])
number_entry_68=Entry(root,width=5,textvariable=sudoku_matrix[6][8])
number_entry_60.grid(row=6,column=0)
number_entry_61.grid(row=6,column=1)
number_entry_62.grid(row=6,column=2)
number_entry_63.grid(row=6,column=3)
number_entry_64.grid(row=6,column=4)
number_entry_65.grid(row=6,column=5)
number_entry_66.grid(row=6,column=6)
number_entry_67.grid(row=6,column=7)
number_entry_68.grid(row=6,column=8)
number_entry_70=Entry(root,width=5,textvariable=sudoku_matrix[7][0])
number_entry_71=Entry(root,width=5,textvariable=sudoku_matrix[7][1])
number_entry_72=Entry(root,width=5,textvariable=sudoku_matrix[7][2])
number_entry_73=Entry(root,width=5,textvariable=sudoku_matrix[7][3])
number_entry_74=Entry(root,width=5,textvariable=sudoku_matrix[7][4])
number_entry_75=Entry(root,width=5,textvariable=sudoku_matrix[7][5])
number_entry_76=Entry(root,width=5,textvariable=sudoku_matrix[7][6])
number_entry_77=Entry(root,width=5,textvariable=sudoku_matrix[7][7])
number_entry_78=Entry(root,width=5,textvariable=sudoku_matrix[7][8])
number_entry_70.grid(row=7,column=0)
number_entry_71.grid(row=7,column=1)
number_entry_72.grid(row=7,column=2)
number_entry_73.grid(row=7,column=3)
number_entry_74.grid(row=7,column=4)
number_entry_75.grid(row=7,column=5)
number_entry_76.grid(row=7,column=6)
number_entry_77.grid(row=7,column=7)
number_entry_78.grid(row=7,column=8)
number_entry_80=Entry(root,width=5,textvariable=sudoku_matrix[8][0])
number_entry_81=Entry(root,width=5,textvariable=sudoku_matrix[8][1])
number_entry_82=Entry(root,width=5,textvariable=sudoku_matrix[8][2])
number_entry_83=Entry(root,width=5,textvariable=sudoku_matrix[8][3])
number_entry_84=Entry(root,width=5,textvariable=sudoku_matrix[8][4])
number_entry_85=Entry(root,width=5,textvariable=sudoku_matrix[8][5])
number_entry_86=Entry(root,width=5,textvariable=sudoku_matrix[8][6])
number_entry_87=Entry(root,width=5,textvariable=sudoku_matrix[8][7])
number_entry_88=Entry(root,width=5,textvariable=sudoku_matrix[8][8])
number_entry_80.grid(row=8,column=0)
number_entry_81.grid(row=8,column=1)
number_entry_82.grid(row=8,column=2)
number_entry_83.grid(row=8,column=3)
number_entry_84.grid(row=8,column=4)
number_entry_85.grid(row=8,column=5)
number_entry_86.grid(row=8,column=6)
number_entry_87.grid(row=8,column=7)
number_entry_88.grid(row=8,column=8)

check_button=Button(root,text="Check",command=get_show)
check_button.grid(row=9,column=7,columnspan=3)



print(sudoku_matrix)

        







root.mainloop()