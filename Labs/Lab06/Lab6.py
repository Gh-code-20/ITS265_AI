# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 07:54:11 2021

@author: ghadir
"""
from typing import List


facts: List[str] = [""]
conclusion: List[str] = [""]
AskQ = True
RuleTriggered = True

def rules(triggerStatus):
    
    if triggerStatus == True:
        #if "Animal has hair" in facts or "Animal gives milk" in facts or "Animal has feathers" in facts or "Animal the animal flies" in facts or "Animal lays eggs" in facts or "Animal is a mammal" in facts or "Animal eats meat" in facts or "Animal has pointed teeth" or "Animal has claws" in facts or "Animal's eyes point forward" in facts or "Animal has hoofs" in facts or "Animal chews cud" in facts or "Animal is a carnivore" in facts or "Animal has a tawny color" in facts or "Animal has dark spots" in facts or "Animal has black strips" in facts or "Animal is an ungulate" in facts or "Animal has long legs" in facts  or "Animal has a long neck" in facts or "Animal has dark spots" in facts or " Animal has a white color" in facts or "Animal is a bird" in facts or " Animal does not fly" in facts or " Animal is black and white" in facts or "Animal is a good flyer" in facts:
            
            if "Animal has hair" in facts:
                if "Animal is a mammal" not in facts:
                    print("Animal is a mammal")
                    facts.append("Animal is a mammal")
                    conclusion.append("Animal is a mammal")
                    triggerStatus = True
                    print("Facts=", facts)
                    print("Conclusions=", conclusion)
                    return triggerStatus
            
            if "Animal gives milk" in facts:
                if "Animal is a mammal" not in facts:
                    print("Animal is a mammal")
                    facts.append("Animal is a mammal")
                    conclusion.append("Animal is a mammal")
                    triggerStatus = True
                    print("Facts=", facts)
                    print("Conclusions=", conclusion)
                    return triggerStatus
               
            
            if  "Animal has feathers" in facts:
                if "Animal is a bird" not in facts:
                    print("Animal is a bird")
                    facts.append("Animal is a bird")
                    conclusion.append("Animal is a bird")
                    triggerStatus = True
                    print("Facts=", facts)
                    print("Conclusions=", conclusion)                
                    return triggerStatus
                
            if  "Animal the animal flies" in facts and "Animal lays eggs" in facts:
                if "Animal is a bird" not in facts:
                    print("Animal is a bird")
                    facts.append("Animal is a bird")
                    conclusion.append("Animal is a bird")
                    triggerStatus = True
                    print("Facts=", facts)
                    print("Conclusions=", conclusion)                
                    return triggerStatus
            
            if  "Animal is a mammal" in facts and "Animal eats meat" in facts:
                if "Animal is a carnivore" not in facts:
                    print("Animal is a carnivore")
                    facts.append("Animal is a carnivore")
                    conclusion.append("Animal is a carnivore")
                    triggerStatus = True
                    print("Facts=", facts)
                    print("Conclusions=", conclusion)                
                    return triggerStatus
                
            if  "Animal is a mammal" in facts and "Animal has pointed teeth" in facts and "Animal has claws" in facts and "Animal's eyes point forward" in facts:
                if "Animal is a carnivore" not in facts:
                    print("Animal is a carnivore")
                    facts.append("Animal is a carnivore")
                    conclusion.append("Animal is a carnivore")
                    triggerStatus = True
                    print("Facts=", facts)
                    print("Conclusions=", conclusion)                
                    return triggerStatus
            
            if  "Animal is a mammal" in facts and "Animal has hoofs" in facts:
                if "Animal is an ungulate" not in facts:
                    print("Animal is an ungulate")
                    facts.append("Animal is an ungulate")
                    conclusion.append("Animal is an ungulate")
                    triggerStatus = True
                    print("Facts=", facts)
                    print("Conclusions=", conclusion)                
                    return triggerStatus
                
                            
            if "the animal is a mammal" and "it chews cud" in facts:
                if "it is an ungulate" and "it is even-toed" not in facts:
                    print("it is an ungulate" and "it is even-toed")
                    facts.append("it is an ungulate" and "it is even-toed")
                    conclusion.append("it is an ungulate" and "it is even-toed")
                    triggerStatus = True
                    print("Facts=", facts)
                    print("Conclusions=", conclusion)
                    return triggerStatus
                
            if  "Animal is a mammal" in facts and "Animal chews cud" in facts:
                if "Animal is an ungulate" not in facts:
                    print("Animal is an ungulate")
                    facts.append("Animal is an ungulate")
                    conclusion.append("Animal is an ungulate")
                    triggerStatus = True
                    print("Facts=", facts)
                    print("Conclusions=", conclusion)
                    
                    if "Animal is even-toed" not in facts:
                        print("Animal is even-toed")
                        facts.append("Animal is even-toed")
                        conclusion.append("Animal is even-toed")
                        triggerStatus = True
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                    else: 
                        return triggerStatus
                    
            
            if  "Animal is a carnivore" in facts and "Animal has a tawny color" in facts and "Animal has dark spots" in facts:
                if "Animal is a cheetah" not in facts:
                    print("Animal is a cheetah")
                    facts.append("Animal is a cheetah")
                    conclusion.append("Animal is a cheetah")
                    triggerStatus = True
                    print("Facts=", facts)
                    print("Conclusions=", conclusion)                
                    return triggerStatus
                
            if  "Animal is a carnivore" in facts and "Animal has a tawny color" in facts and "Animal has black strips" in facts:
                if "Animal is a tiger" not in facts:
                    print("Animal is a tiger")
                    facts.append("Animal is a tiger")
                    conclusion.append("Animal is a tiger")
                    triggerStatus = True
                    print("Facts=", facts)
                    print("Conclusions=", conclusion)                
                    return triggerStatus
                
            if  "Animal is an ungulate" in facts and "Animal has long legs" in facts and "Animal has a long neck" in facts and "Animal has a tawny color" in facts and "Animal has dark spots" in facts:
                if "Animal is a giraffe" not in facts:
                    print("Animal is a giraffe")
                    facts.append("Animal is a giraffe")
                    conclusion.append("Animal is a giraffe")
                    triggerStatus = True
                    print("Facts=", facts)
                    print("Conclusions=", conclusion)                
                    return triggerStatus
                
            if  "Animal is an ungulate" in facts and "Animal has a white color" in facts and "Animal  has black stripes" in facts:
                if "Animal is a zebra" not in facts:
                    print("Animal is a zebra")
                    facts.append("Animal is a zebra")
                    conclusion.append("Animal is a zebra")
                    triggerStatus = True
                    print("Facts=", facts)
                    print("Conclusions=", conclusion)                
                    return triggerStatus
                
            if  "Animal is a bird" in facts and "Animal does not fly" in facts and "Animal  has long legs" in facts and "Animal has a long neck" in facts and "Animal is black and white" in facts:
                if "Animal is a penguin" not in facts:
                    print("Animal is a penguin")
                    facts.append("Animal is a penguin")
                    conclusion.append("Animal is a penguin")
                    triggerStatus = True
                    print("Facts=", facts)
                    print("Conclusions=", conclusion)                
                    return triggerStatus

            if  "Animal is a bird" in facts and "Animal is a good flyer" in facts:
                if "Animal is an albatross" not in facts:
                    print("Animal is an albatross")
                    facts.append("Animal is an albatross")
                    conclusion.append("Animal is an albatross")
                    triggerStatus = True
                    print("Facts=", facts)
                    print("Conclusions=", conclusion)                
                    return triggerStatus
    
            else:
                return triggerStatus
    else:
        triggerStatus = False
        print("Conclusion reached", conclusion)
        return triggerStatus
                 
        
def check(triggerStatus):
    if triggerStatus == True:
        #this database still needs more info. 
        #Animal is a bird and Animal is an ungulate can't be input to facts at sametime
        if "Animal is a bird" in facts and "Animal is an ungulate" in facts:
            print("this fact can not be inport")
            print(facts[len(facts)-1] ," is been removed from fact")
            facts.pop(len(facts)-1)
            print("New Facts=", facts)
            return triggerStatus

        else:
            return triggerStatus

    else:
        triggerStatus = False
        return triggerStatus
    
        
        
def GetData(triggerStatus):
    if triggerStatus == True:
        Ans = input("\n Do you want to enter a fact (Y/N)?  ")
        if Ans == 'Y':
            print("\nCurrent Facts:  ", facts)
            factInput = input("\nEnter a fact:  ")
            #Check whether it is in the list
            if factInput not in facts:
                facts.append(factInput)
                #facts.append("Animal has hair")
            print("\nNew facts", facts)
            return True
        else:
            return False
    else:
        print("Conclusion reached: ", conclusion)
        return
    
    
# def GetData(triggerStatus):
#     if triggerStatus == True:
#         Ans = input("\n Do you want to enter a fact (Y/N)?  ")
#         if Ans == 'Y':
#             print("\nCurrent Facts:  ", facts)
#             print("\nNew facts", facts)
#             factInput = input("\nEnter a fact:  ")
#             #Check whether it is in the list
#             if factInput not in facts:
#                 if "Animal has hair" in facts and factInput == "Animal has feathers":
#                     print("Contradictary fact Enter a new fact")
#                     factInput = input("\nEnter a new fact: ")
#                     GetData(triggerStatus)
#                 if "Animal has feathers" in facts and factInput == "Animal is an ungulate":
#                     print("Contradictary fact Enter a new fact")
#                     factInput = input("\nEnter a new fact: ")
#                     GetData(triggerStatus)  
#                 if "Animal has feathers" in facts and factInput == "Animal has hair":
#                     print("Contradictary fact Enter a new fact")
#                     factInput = input("\nEnter a new fact: ")
#                     GetData(triggerStatus)                     
#                 if "Animal is a mammal" in facts and factInput == "Animal has feathers":
#                     print("Contradictary fact Enter a new fact")
#                     factInput = input("\nEnter a new fact: ")
#                     GetData(triggerStatus)                    
#                 if "Animal gives milk" in facts and factInput == "Animal is a bird":
#                     print("Contradictary fact Enter a new fact")
#                     factInput = input("\nEnter a new fact: ")
#                     GetData(triggerStatus)   
#                 if "Animal gives milk" in facts and factInput == "Animal has feathers":
#                    print("Contradictary fact Enter a new fact")
#                    factInput = input("\nEnter a new fact: ")
#                    GetData(triggerStatus)        
#                 if "Animal gives milk" in facts and factInput == "Animal has pointed teeth":
#                    print("Contradictary fact Enter a new fact")
#                    factInput = input("\nEnter a new fact: ")
#                    GetData(triggerStatus)   
#                 if "Animal is an ungulate" in facts and factInput == "Animal has pointed teeth":
#                    print("Contradictary fact Enter a new fact")
#                    factInput = input("\nEnter a new fact: ")
#                    GetData(triggerStatus)           
#                 if "Animal is an ungulate" in facts and factInput == "Animal has dark spots":
#                     print("Contradictary fact Enter a new fact")
#                     factInput = input("\nEnter a new fact: ")
#                     GetData(triggerStatus)
#                 if "Animal is a carnivor" in facts and factInput == "Animal is a mammal" :
#                     print("Contradictary fact Enter a new fact")
#                     factInput = input("\nEnter a new fact: ")
#                     GetData(triggerStatus)
#                 facts.append(factInput)
                     
#             return True
#         else:
#             return False
#     else:
#         print("Conclusion reached: ", conclusion)
#         return
    

# Main
while (AskQ):
    AskQ = GetData(RuleTriggered)
    if RuleTriggered == True:
        RuleTriggered = rules(RuleTriggered)
        RuleTriggered = check(RuleTriggered)
        
print("Finished Rule Processing")   
	
       

