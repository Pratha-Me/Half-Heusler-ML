import pandas as pd

class EditFile:

    def __init__(self):
        pass
    
#     def __init__(self, fp, fn):
#         self.filePath = fp
#         self.fileName = fn
    
    def generateFile(filePath, fileName):
#         df = pd.read_csv(self.filePath)
        df = pd.read_csv(filePath)
        print (df.head())

        id_list = df['Materials-ID'].to_list()

        n = df.columns[0]
        df.drop(n, axis=1, inplace=True)

        df[n] = ["mp-" + str(x) for x in id_list]
        print (df.head())

        df.to_csv(fileName, index = False)
