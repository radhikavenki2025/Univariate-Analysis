class Univariate():

    def QuanQual(dataset):
        quan=[]
        qual=[]
        for columnname in dataset.columns:
    ###print(columnname)
            if(dataset[columnname].dtype=='O'):
    ###  print("qual")
                qual.append(columnname)
            else:
    #### print("quan")
                 quan.append(columnname)
        return quan,qual