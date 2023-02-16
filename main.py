import csv
import datetime
import shutil
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import os
import seaborn as sn

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_hi('PyCharm')

    path = r'D:\overlap_data.csv'

    head, tail = os.path.split(path)

    xlsfileName = tail.split('.')[0]

    print(f"xls file Name {xlsfileName}")    

    WSDirName = "OverlapWorkSpace"

    if not os.path.exists(WSDirName):
        os.makedirs(WSDirName)

    # using now() to get current time
    current_time = datetime.datetime.now()

    newFolderName = f"{xlsfileName}_{current_time.year:04d}{current_time.month:02d}{current_time.day:02d}{current_time.hour:02d}{current_time.minute:02d}{current_time.second:02d}"
    newFolderPath = WSDirName + f"\\{newFolderName}"

    os.makedirs(newFolderPath)

    rawFileFolderPath = newFolderPath + f"\\RawFile"

    os.makedirs(rawFileFolderPath)

    # copy raw file
    shutil.copyfile(path, f"{rawFileFolderPath}\\{tail}")

    ColA = {}
    ColB={}

    #read csv

    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:                        
            # print(f'ColA {row[0]} ColB {row[1]}.')
            
            if row[0]!="":            
                #COlA
                sections = row[0].split(';') 
                for idx, oneSection in enumerate(sections):         
                    if oneSection in ColA:
                        print(f'ColA Already contains section {oneSection}.')
                    else:
                        ColA[oneSection]=(line_count,idx)
                        
            if row[1]!="":           
                #COlB
                sections = row[1].split(';')
                
                for idx, oneSection in enumerate(sections):         
                    if oneSection in ColB:
                        print(f'ColB Already contains section {oneSection}.')
                    else:
                        ColB[oneSection]=(line_count,idx)  
            line_count += 1
        print(f"ColA Len {len(ColA)} ColB Len {len(ColB)}")
        print(f'Processed {line_count} lines.')
    
    keysSet_ColA = set(ColA.keys())
    keysSet_ColB = set(ColB.keys())
    
    summaryList=[]

 
    if (keysSet_ColA & keysSet_ColB):
        commonElements=keysSet_ColA & keysSet_ColB
        
        for commonElement in commonElements:
            rowNumberA=ColA[commonElement][0]
            IndexNumberA=ColA[commonElement][1]
            rowNumberB=ColB[commonElement][0]
            IndexNumberB=ColB[commonElement][1]            
            summaryList.append([commonElement,rowNumberA,IndexNumberA,rowNumberB,IndexNumberB])

        
        print(len(commonElements))
    else:
        print("No common elements")
        
    df = pd.DataFrame(summaryList,columns=['CommonElement','RowNumberInA','IndexNumberInRow','RowNumberInB','IndexNumberInRow'])
    df.to_csv('abc.csv')

    
#     # fit from 1-8 columns

#     for index, row in df.iterrows():
#         X=[1,2,3,4,5,6,7,8]
#         Y=df.iloc[index,1:9].values.flatten().tolist()
#         slope=np.polyfit(X,Y,1)[0]
#         df._set_value(index, 'Slope', slope)
#         # print(f"Row {index} Slope {slope}")
    
#     final_df = df.sort_values(by=['Slope'], ascending=False)
    
#     # set threshold
#     threshold=0.4
    
#     column_headers = list(final_df.columns.values)
    
#     # for i in range(final_df.shape[0]): #iterate over rows
#     #     for j in range(1,9): #iterate over columns
#     #         if(final_df.iloc[i, j]>threshold): #get cell value
#     #             final_df._set_value(i, column_headers[j], threshold)    
                
#     # print(final_df.to_string()) 


    

#     x_axis_labels = ""  # labels for x-axis
#     y_axis_labels = ""  # labels for y-axis

#     Matrix  =   final_df.iloc[:,1:9].to_numpy()

#     print(Matrix.shape)


#     svm = sn.heatmap(Matrix, xticklabels=x_axis_labels,
#                      yticklabels=y_axis_labels, cmap="YlGnBu", vmin=0.15, vmax=threshold)

#     for tick in svm.get_xticklabels():
#         tick.set_fontname("Arial")
#         tick.set_fontweight("bold")

#     for tick in svm.get_yticklabels():
#         tick.set_fontname("Arial")
#         tick.set_fontweight("bold")

#     svm.tick_params(length=4, width=1.5)

#     # use matplotlib.colorbar.Colorbar object
#     cbar = svm.collections[0].colorbar
#     cbar.set_label('')
   
#     # here set the labelsize by 20

#     cbar.ax.set_yticks([])
    
    
#    # for tick in cbar.ax.get_yticklabels():
#       #  tick.set_fontname("Arial")
#       #  tick.set_fontweight("bold")
#     # plt.show()
#     #
#     # cbar_axes = svm.figure.axes[-1]
#     #
#     # cbar_axes.tick_params(labellength=6, width=2)

#     plt.savefig(f'{rawFileFolderPath}\\HeatMap_WithoutAnnot.png', dpi=1200)

#     plt.clf()

    




    ##get overlap index

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
