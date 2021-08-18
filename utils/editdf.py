import pandas as pd

class EditFile(object):

    def edit(self):
#         df = pd.read_csv('../assets/HalfHeusler.csv')
        df = pd.read_csv(filePath)
        print (df.head())

        id_list = df['Materials-ID'].to_list()

        n = df.columns[0]
        df.drop(n, axis=1, inplace=True)

        df[n] = ["mp-" + str(x) for x in id_list]
        print (df.head())

#         df.to_csv('Heusler compound.csv')
        df.to_csv(fileName)
