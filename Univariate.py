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

def Univariate(dataset,Quan):
    descriptive=pd.DataFrame(index==["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5rule","Lesser","Greater","Min","Max"],columns=quan)
    for columnname in quan:
        descriptive.loc["Mean",columnname]=dataset[columnname].mean()
        descriptive.loc["Median",columnname]=dataset[columnname].median()
        descriptive.loc["Mode",columnname]=dataset[columnname].mode()[0]
        descriptive.loc["Q1:25%",columnname]=dataset[columnname].quantile(0.25)
        descriptive.loc["Q2:50%",columnname]=dataset[columnname].quantile(0.50)
        descriptive.loc["Q3:75%",columnname]=dataset[columnname].quantile(0.75)
        descriptive.loc["99%",columnname]=np.percentile(dataset[columnname],99)
        descriptive.loc["Q4:100%",columnname]=dataset[columnname].quantile(1.00)
        descriptive.loc["IQR",columnname]=descriptive[columnname]["Q3:75%"]-descriptive[columnname]["Q1:25%"]
        descriptive.loc["1.5rule",columnname]=1.5*descriptive[columnname]["IQR"]
        descriptive.loc["Lesser",columnname]=descriptive[columnname]["Q1:25%"]-descriptive[columnname]["1.5rule"]
        descriptive.loc["Greater",columnname]=descriptive[columnname]["Q3:75%"]+descriptive[columnname]["1.5rule"]
        descriptive.loc["Min",columnname]=dataset[columnname].min()
        descriptive.loc["Max",columnname]=dataset[columnname].max()
    return descriptive

def freqTable(columnName,dataset):
    freqTable=pd.DataFrame(columns=["Unique_Values","Frequency","Relative_Frequency","CumSum"])
    freqTable["Unique_Values"]=dataset[columnName].value_counts().index
    freqTable["Frequency"]=dataset[columnName].value_counts().values
    freqTable["Relative_Frequency"]=(freqTable["Frequency"]/103)
    freqTable["CumSum"]=freqTable["Relative_Frequency"].cumsum()
    return freqTable

def find_Outliers(descriptive,Quan):
    lesser=[]
    greater=[]

    for columnName in Quan:
        if(descriptive[columnName]["Min"]<descriptive[columnName]["Lesser"]):
            lesser.append(columnName)
        if(descriptive[columnName]["Max"]>descriptive[columnName]["Greater"]):
            greater.append(columnName)
    return lesser,greater


def replace_Outliers(descriptive,Quan):
    for columnName in lesser :
        dataset[columnName][dataset[columnName]<descriptive[columnName]["Lesser"]]=descriptive[columnName]["Lesser"]
    for columnName in greater:
        dataset[columnName][dataset[columnName]>descriptive[columnName]["Greater"]]=descriptive[columnName]["Greater"]
    return 
