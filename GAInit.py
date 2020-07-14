import numpy as np
def evaluteFAT(FAT):
    SFragment =np.array([40, 80, 50, 60]) #size of fragment
    FAT = np.array(FAT)
    # print(FAT)
    RM = np.array ([
        [2, 0, 3, 2],
        [0, 2, 2, 3],
        [3, 0, 1, 2],
        [4, 2, 4, 2],
    ])
    # print(RM)
    UM = np.array( [
        [2, 2, 3, 2],
        [0, 0, 2, 2],
        [3, 0, 2, 2],
        [2, 1, 2, 1],
    ])

    FREQ = np.array([
        [2, 2, 1, 1],
        [2, 1, 2, 1],
        [4, 2, 1, 2],
        [5, 1, 2, 1],
    ])

    SEL = np.array( [
        [0.1, 0.3, 0.1, 0.4],
        [0.1, 0.3, 0.2, 0.4],
        [0.2, 0.5, 2, 0.4],
        [0.4, 0.2, 0.2, 3],
    ])

    CTR = np.array ([
        [0, 0.2, 0.2, 0.2],
        [0.2, 0, 0.5, 0.1],
        [0.2, 0.5, 0, 0.2],
        [0.2, 0.1, 0.2, 0],
    ])

    Cini = 5;
    P_SIZE = 0.1;
    VCini = 5;
    SI = 1;

    def calculateCommunicationCost(sideId1, sideId2, m_size): # calcualte communication cost
        return Cini * (m_size / P_SIZE) + CTR[sideId1][sideId2] * m_size;


    def  CCload ():
        CCload = 0
        row = FAT.shape[0]
        col = FAT.shape[1]
        for i in range(0 ,row):
            for j in range(0 ,col):
                CCload += (FAT[i][j] * calculateCommunicationCost(SI, j, SFragment[i]));
        return CCload

    def calculatorMinimumTransmissionCost (fragmentId,sizeId = 0, transactionId = 0):
        minTC = np.inf;
        for s in range(0,len(FAT[0])):
            if (FAT[fragmentId][s] == 1):
                m_size = (SEL[transactionId][fragmentId] / 100) * SFragment[fragmentId];
                result = calculateCommunicationCost(sizeId, s, m_size);
                if (minTC > result):
                    minTC = result;
        return minTC;


    def calculatorTRi (sizeId, transactionId) :

        total = 0;
        for  j in range (0,len(SFragment)):
            minTC = calculatorMinimumTransmissionCost(j,sizeId, transactionId)
            result = RM[transactionId][j] * minTC
            total += result
        return total

    def calculatorTotalTransmissionCosts(sizeId, transactionId, fragmentId):
        total = 0;
        m_size = (SEL[transactionId][fragmentId] / 100) * SFragment[fragmentId];
        length = len(FAT[0]);
        for l in  range(0, length):
            result = FAT[fragmentId][l] * calculateCommunicationCost(sizeId, l, m_size);
            total += result;
        return total;
    def calculatorTUi(sizeId, transactionId):
      total = 0;
      for j in range (0, len(SFragment)):
        totalTC = calculatorTotalTransmissionCosts(sizeId, transactionId, j);
        total += UM[transactionId][j]*totalTC;
      return total;


    def CCproc ():

        CCproc = 0
        for  k in range (0, 4):
            for i in range (0,4):
                TRi = calculatorTRi(k, i)
                TUi = calculatorTUi(k, i)
                CCproc += FREQ[i][k] * (TRi + TUi + VCini)
                return CCproc

    score = CCload() + CCproc()
    return score
