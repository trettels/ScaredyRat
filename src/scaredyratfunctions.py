import os
import math
import time
import numpy as np
import pandas as pd

def find_epoch(df, epochLabel, isFlagged, numEpochs, epochStartTime, epochEndTime):
    '''
    Creates dictionary of each epoch. Values are
    dataframes...
    '''
    epochs = {}
    i = 1
    while i <= numEpochs: # number of epochs
        if(isFlagged): # Ethovision has a bucket for this epoch type
            num = str(i)
            label = epochLabel + ' ' + num
            if(epochStartTime!=0): # if we're looking for a timeframe outside the bucket
                epochstart = epochs.iloc[0] #Time for epoch start, as a dataframe
    
                starttime = math.floor(epochstart['Recording time']-epochStartTime) # Epoch start
                endtime = math.floor(tonestart['Recording time']+epochEndTime) #T Epoch end
                itime = df.index.get_loc(starttime,method='bfill') #Index for epoch start
                etime = df.index.get_loc(endtime,method='bfill') #Index for epoch end
                epoch = df.iloc[itime:etime] #dataframe for epoch
            else: # Epoch spans, and is fully contained within, the bucket
                epoch = pd.DataFrame(df[df[label] == 1]) # dataframe for epoch
            
            epochs[i] = epoch #Store the epoch in the output structure
        else:
            itime = df.index.get_loc(epochStartTime[i-1],method='bfill') #Index for pretone start
            etime = df.index.get_loc(epochEndTime[i-1],method='bfill') #Index for pretone end
            epochs[i] = df.iloc[itime:etime]
        
        i += 1
        
    return(epochs)
    
def find_epoch_vels(df, numEpochs):
    '''
    '''
    epochVels = {}
    i=1
    while i <= numEpochs:
        num = str(i)
        epochDF = []
        epochstart = df[i].iloc[0] # Time for epoch start
        epochend = df[i].iloc[-1] #Time for epoch end
        #print(epochstart)
        starttime = math.floor(epochstart['Recording time']) #Time for epoch start
        endtime = math.floor(epochend['Recording time']) #Time for epoch end
        itime = df[i].index.get_loc(starttime,method='bfill') #Index for epoch start
        etime = df[i].index.get_loc(endtime,method='bfill') #Index for epoch end
    
        epochDF = df[i].iloc[itime:etime] #df for epoch i
        epochVels[i] = epochDF['Velocity']
        i+=1
    return(epochVels)

#def find_epoch_freezing(df, numEpochs, thresh):
    
#def find_epoch_darting(df, numEpochs, thresh):