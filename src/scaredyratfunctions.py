import os
import math
import time
import numpy as np
import pandas as pd

def find_epoch(df, epochLabel, isFlagged, numEpochs, epochStartTime, epochEndTime, window):
    '''
    Creates dictionary of each epoch. Values are
    dataframes...
    '''
    tones = {}
    i = 0
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
            itime = df.index.get_loc(epochStartTime,method='bfill') #Index for pretone start
            etime = df.index.get_loc(epochEndTime,method='bfill') #Index for pretone end
            epochs[i] = df.iloc[itime:etime]
        
        i += 1
        
    return(epochs)