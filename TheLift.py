class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.queues = [list(x) for x in queues]
        self.capacity = capacity
        self.lift = []
        self.stopFloors = [0]
        self.PeopleWaitForLift = True
        
    def appendToStopFloors(self, floor):
        if self.stopFloors[-1] != floor:
            self.stopFloors.append(floor)
    
    def removePeopleFromLift(self, floor):
        for person in self.lift[:]:
            if person == floor:
                self.lift.remove(person)
                self.appendToStopFloors(floor)
                
    def appendPeopleToLift (self, floor, person):
        if len(self.lift) < self.capacity:
            self.lift.append(person)
            self.queues[floor].remove(person)
        else:
            self.PeopleWaitForLift = True
    
    def theLift(self):
        lift = []
        floors = [0]
        
        while self.PeopleWaitForLift:
            self.PeopleWaitForLift = False
        
            # going up
            for floor in range(0, len(self.queues)):
                self.removePeopleFromLift(floor)
                
                for person in self.queues[floor][:]:
                    if person > floor:
                        self.appendToStopFloors(floor)
                        self.appendPeopleToLift(floor, person)
                            
            #going down
            for floor in range(len(self.queues) -1 , 0, -1):
                self.removePeopleFromLift(floor)
                        
                for person in self.queues[floor][:]:
                    if person < floor:
                        self.appendToStopFloors(floor)
                        self.appendPeopleToLift(floor, person)
                            
        if self.stopFloors[-1] != 0:
            self.stopFloors.append(0)
                
        return self.stopFloors
