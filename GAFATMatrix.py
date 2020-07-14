import numpy as np
import GAInit as GA
import math as Math
import random
class FAT:
    swapLength = Math.floor((4 * 4 - 1) / 3);

    def __init__(self,FAT):
        self.FAT = FAT
        self.fitnessScore = GA.evaluteFAT(FAT)

    def create_individual(self):
        return np.random.randint(2, size=(4, 4))

    def __lt__(self, other):
        return self.fitnessScore < other.fitnessScore
    def mate(self, fatherFat):
        swapPositionStart = Math.ceil((15 - self.swapLength) * random.random());
        swapPositionEnd = swapPositionStart + self.swapLength
        i1 = Math.floor(swapPositionStart / 4)
        j1 = swapPositionStart % 4
        i2 = Math.floor(swapPositionEnd / 4)
        j2 = swapPositionEnd % 4
        for j in range(j1, 4):
            [self.FAT[i1][j], fatherFat.FAT[i1][j]] = [fatherFat.FAT[i1][j], self.FAT[i1][j]]
        for i in range(i1 + 1, i2):
            [self.FAT[i], fatherFat.FAT[i]] = [fatherFat.FAT[i], self.FAT[i]]
        j = 0
        while j <= j2:
            [self.FAT[i2][j], fatherFat.FAT[i2][j]] = [fatherFat.FAT[i2][j], self.FAT[i2][j]];
            j += 1
        # print([self.FAT, fatherFat.FAT])
        return [self.FAT, fatherFat.FAT]

    def mutate_swap(self):

        swapPositionStart = Math.floor(15 * random.random());
        swapPositionDestination = Math.floor(15 * random.random());
        i1 = Math.floor(swapPositionStart / 4)
        j1 = swapPositionStart % 4;
        i2 = Math.floor(swapPositionDestination / 4)
        j2 = swapPositionDestination % 4;
        [self.FAT[i1, j1], self.FAT[i2, j2]] = [self.FAT[i2, j2], self.FAT[i1, j1]];
