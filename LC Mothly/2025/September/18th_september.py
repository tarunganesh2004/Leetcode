# Design Task Manager LC 3408

import heapq


class TaskManager:
    def __init__(self,tasks):
        self.taskToUser={}
        self.taskToPriority={}

        self.topTask=[]

        for userId,taskId,priority in tasks:
            self.add(userId,taskId,priority)
    
    def add(self,userId,taskId,priority):
        self.taskToUser[taskId]=userId
        self.taskToPriority[taskId]=priority
        heapq.heappush(self.topTask,(-priority,-taskId))

    def edit(self,taskId,newPriority):
        self.taskToPriority[taskId]=newPriority
        heapq.heappush(self.topTask,(-newPriority,-taskId))

    def rmv(self,taskId):
        if taskId in self.taskToUser:
            del self.taskToUser[taskId]
            del self.taskToPriority[taskId]

    def execTop(self):
        if not self.taskToUser:
            return -1
        while self.topTask:
            priority,negTaskId=heapq.heappop(self.topTask)
            taskId=-negTaskId
            if taskId in self.taskToUser and self.taskToPriority[taskId]==-priority:
                user=self.taskToUser.pop(taskId)
                self.taskToPriority.pop(taskId)
                return user 
        return -1
        