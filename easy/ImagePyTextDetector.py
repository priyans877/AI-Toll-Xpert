from easyocr import Reader
import os

b=[]
def funti():
 
    dir_path = r'C:/Users/pk877/OneDrive/Desktop/prdce/imge'
    s=len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))])

    for i in range(1,s+1):
        reader=Reader(['en'],gpu=False)
        resul=reader.readtext('C:/Users/pk877/OneDrive/Desktop/prdce/imge/image{}.jpg'.format(i))
        b.append(resul)
        if len(resul)!=0:
                for item in resul:
                    if item[2]>=.5:
                        for i in range(1,len(item)-1):
                            print(item[i])
                            print("*---------------------------------*--------------------------------*")

    
    return 0

if __name__ == "__main__" :
    print(funti())