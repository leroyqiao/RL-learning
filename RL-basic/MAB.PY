import numpy as np
import matplotlib.pyplot as plt

class BernoulliBandit:
    def __init__(self,K):
        self.probs =np.random.uniform(size=K) #随机生成K个0~1之间的数，作为每个臂的成功概率
        self.best_idx = np.argmax(self.probs) #找到成功概率最大的臂的索引
        self.best_prob= self.probs[self.best_idx] #找到成功概率最大的臂的成功概率
        self.K = K
    def step(self,k):
        if np.random.rand() < self.probs[k]: #以成功概率为阈值，随机生成一个0~1之间的数，如果小于成功概率，则认为该臂成功
            return 1
        else:
            return 0

np.random.seed(1) #设置随机种子
K = 10 #臂的数量
bandit_10_arm = BernoulliBandit(K) #创建一个10臂的BernoulliBandit对象
print("随机生成了一个%d臂的伯努利老虎机" % K)
print("获奖概率最大的拉杆为%d，获奖概率为%.2f" % (bandit_10_arm.best_idx, bandit_10_arm.best_prob))

