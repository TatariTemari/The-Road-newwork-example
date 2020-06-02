# -*- coding: utf-8 -*-
"""
Created on Sat May 30 22:25:46 2020

@author: IT
"""
import matplotlib.pyplot as plt
from numpy.random import rand,random
import numpy as np

def example_1():
    #Positions = {'a':{'x':0.1,'y':0.5},'b':{'x':0.5,'y':0.9},'c':{'x':0.7,'y':0.3},'d':{'x':0.16,'y':0.1},'e':{'x':0.25,'y':0.25},'f':{'x':0.27,'y':0.45},'g':{'x':0.51,'y':0.59},'h':{'x':0.5,'y':0.3}};
    Positions = {'a':{'x':0.1,'y':0.5},'b':{'x':0.16,'y':0.1},'c':{'x':0.7,'y':0.3},'d':{'x':0.5,'y':0.9},'e':{'x':0.25,'y':0.25},'f':{'x':0.27,'y':0.45},'g':{'x':0.51,'y':0.59},'h':{'x':0.5,'y':0.3}};
    Roads = {0:{'from':'a','to':'e','link':1}, 1:{'from':'b','to':'h','link':1},2:{'from':'c','to':'g','link':1}, 3:{'from':'d','to':'f','link':1},
             4:{'from':'e','to':'f','link':1}, 5:{'from':'f','to':'g','link':1},6:{'from':'g','to':'h','link':1},7:{'from':'h','to':'e','link':1}};
     
    
    plt.figure()
    ax = plt.gca()
    for p in Positions.keys():
        ax.scatter(Positions[p]['x'],Positions[p]['y'],color = 'black',marker = 'x')
        ax.text(Positions[p]['x'],Positions[p]['y'],p,size = 20)   
        
 
    for r in Roads.keys():
        distance = 'not applicable'
        if Roads[r]['link'] == 1:
            ax.plot([Positions[Roads[r]['from']]['x'],Positions[Roads[r]['to']]['x']],[Positions[Roads[r]['from']]['y'],Positions[Roads[r]['to']]['y']],color = 'b',linewidth = 5);
            distance = ((Positions[Roads[r]['from']]['x']-Positions[Roads[r]['to']]['x'])**2 + (Positions[Roads[r]['from']]['y']-Positions[Roads[r]['to']]['y'])**2)**0.5;
            ax.text((Positions[Roads[r]['from']]['x']+Positions[Roads[r]['to']]['x'])/2,(Positions[Roads[r]['from']]['y']+Positions[Roads[r]['to']]['y'])/2,round(distance,3),size = 10,color = 'r')

def example_2():
    total_distant = 0;
    for r in Roads.keys():
        if Roads[r]['link'] == 1:
            distance = ((Positions[Roads[r]['from']]['x']-Positions[Roads[r]['to']]['x'])**2 + (Positions[Roads[r]['from']]['y']-Positions[Roads[r]['to']]['y'])**2)**0.5;
            total_distant = total_distant + distance;
     
    
    plt.figure()
    ax = plt.gca()
    for p in Positions.keys():
        ax.scatter(Positions[p]['x'],Positions[p]['y'],color = 'black',marker = 'x')
        ax.text(Positions[p]['x'],Positions[p]['y'],p,size = 20)   
    
 
    for r in Roads.keys():
        if Roads[r]['link'] == 1:
            ax.plot([Positions[Roads[r]['from']]['x'],Positions[Roads[r]['to']]['x']],[Positions[Roads[r]['from']]['y'],Positions[Roads[r]['to']]['y']],color = 'b',linewidth = 5);


'''
##################################################################
'''

def example_3():
    LengthOfRoadNetowrk = []
    # the solution information is the position of the junctions and the information on the links
    SolutionInformation_positions = []
    SolutionInformation_links = []
    plt.figure()
    ax = plt.gca()
    for z in range(10):
        newPositions = [];
        Edges = [];
        total_distant = 0;
        distance = 0;
        thisColor = [rand(),rand(),rand()]
        for i in range(4):
            newPositions.append([round(rand(),3),round(rand(),3)]);
            Edges.append(round(rand()));
        for t,p in enumerate(Positions.keys()):           
            if t>3:
                print('t',t)
                Positions[p]['x']= newPositions[t-4][0];
                Positions[p]['y']= newPositions[t-4][1];   
            
        for r in range(4,8):    
            print('r',r)
            Roads[r]['link'] = Edges[(r-4)];
            
        print('Edges')
        print(Edges)
            

        for p in Positions.keys():
            ax.scatter(Positions[p]['x'],Positions[p]['y'],color = 'black',marker = 'x')
            ax.text(Positions[p]['x'],Positions[p]['y'],p,size = 20)   
        
        numberofLinks = 0;
        for r in Roads.keys():
            if Roads[r]['link'] == 1:
                ax.plot([Positions[Roads[r]['from']]['x'],Positions[Roads[r]['to']]['x']],[Positions[Roads[r]['from']]['y'],Positions[Roads[r]['to']]['y']],color = thisColor,linewidth = 2);
                distance = ((Positions[Roads[r]['from']]['x']-Positions[Roads[r]['to']]['x'])**2 + (Positions[Roads[r]['from']]['y']-Positions[Roads[r]['to']]['y'])**2)**0.5;
                total_distant = total_distant + distance;
                numberofLinks = numberofLinks + 1;
        # lets say we are interested in solution with at list interlinkages
        if numberofLinks == 8:
            SolutionInformation_positions.append([newPositions[0],newPositions[1],newPositions[2],newPositions[3]])
            SolutionInformation_links.append([Edges[0],Edges[1],Edges[2],Edges[3]])
            LengthOfRoadNetowrk.append(total_distant)
    min_LengthOfRoadNetowrk = min(LengthOfRoadNetowrk)
    indexOftheShortestRoadNetwork = LengthOfRoadNetowrk.index(min_LengthOfRoadNetowrk)
    RoadNetworkWithLeastLength = LengthOfRoadNetowrk[indexOftheShortestRoadNetwork]
    Solution_positions = SolutionInformation_positions[indexOftheShortestRoadNetwork]
    Solution_links = SolutionInformation_links[indexOftheShortestRoadNetwork]
 
'''
##################################################################
'''
# we will use the following function in this function (example_4)
def CalcDist(in_,out_):
    #if Roads[i]['link'] == 1 and Roads[i]['from'] == NodeNames[path[j-1]] and  Roads[i]['to']== NodeNames[path[j]]
    distance = ((Positions[in_]['x']-Positions[out_]['x'])**2 + (Positions[in_]['y']-Positions[out_]['y'])**2)**0.5;
    return distance

def example_4():
    
    
    for o in range(10):
        performanceData = [];
        LengthOfRoadNetowrk = []
        MaximumPathInthNetwork = []
        # the solution information is the position of the junctions and the information on the links
        SolutionInformation_positions = []
        SolutionInformation_links = []
        for z in range(2000000):
            distances = []
            newPositions = [];
            Edges = [];
            total_distant = 0;
            distance = 0;
            thisColor = [rand(),rand(),rand()]
            for i in range(4):
                newPositions.append([round(rand(),3),round(rand(),3)]);
                Edges.append(round(rand()));
            for t,p in enumerate(Positions.keys()):           
                if t>3:
                    Positions[p]['x']= newPositions[t-4][0];
                    Positions[p]['y']= newPositions[t-4][1];   
                
            for r in range(4,8):    
                Roads[r]['link'] = Edges[(r-4)];
                
            '''
            # Assuming the relative direction of the junction nodes d,e,f and ge will not change (only thier positions change)
            # we can assume the possible path from each of the four villages a,b,c, and d
            a b   
            a c
            a d
            b c
            b d
            c d
            
            will be 
            
            a e h b   
            a e h g c
            a e f d
            b h g c
            b h g t d
            c g t d        
            '''        
    
            distances.append(CalcDist('a', 'e') + CalcDist('e', 'h') + CalcDist('h', 'b' ))
            distances.append(CalcDist('a', 'e') + CalcDist('e', 'h') + CalcDist('h', 'g' ) + CalcDist('g', 'c' ))
            distances.append(CalcDist('a', 'e') + CalcDist('e', 'f') + CalcDist('f', 'd' ))
            
            distances.append(CalcDist('b', 'h') + CalcDist('h', 'g') + CalcDist('g', 'c' ))
            distances.append(CalcDist('b','h') + CalcDist('h','g') + CalcDist('g', 'f' )  + CalcDist('f', 'd' )) 
            
            distances.append(CalcDist('c', 'g') + CalcDist('g', 'f') + CalcDist('f', 'd' ))        
    
            Max_of_distances = max(distances)
     
    
    
            SolutionInformation_positions.append([newPositions[0],newPositions[1],newPositions[2],newPositions[3]])
            SolutionInformation_links.append([Edges[0],Edges[1],Edges[2],Edges[3]])
            MaximumPathInthNetwork.append(Max_of_distances)
            LengthOfRoadNetowrk.append(sum(distances))
            performanceData.append([Max_of_distances,sum(distances)])
        performanceData_ = np.array(performanceData)
        performanceData_1 = performanceData_[np.lexsort((performanceData_[:, 0], performanceData_[:, 1]))]


        '''
        min_LengthOfRoadNetowrk = min(LengthOfRoadNetowrk)
        min_MaximumPathInthNetwork = min(MaximumPathInthNetwork)        
        indexofmin_MaximumPathInthNetwork = MaximumPathInthNetwork.index(min_MaximumPathInthNetwork)
        indexOftheShortestRoadNetwork = LengthOfRoadNetowrk.index(min_LengthOfRoadNetowrk)
        RoadNetworkWithLeastLength = LengthOfRoadNetowrk[indexOftheShortestRoadNetwork]
        Solution_positions = SolutionInformation_positions[indexOftheShortestRoadNetwork]
        Solution_links = SolutionInformation_links[indexOftheShortestRoadNetwork]
        #print('o',o)
        print('The total length of the road network with the shortest path found is:')
        print(round(RoadNetworkWithLeastLength,3))          
        '''
        indexofmin_MaximumPathInthNetwork = MaximumPathInthNetwork.index(performanceData_1[0,0])
        indexOftheShortestRoadNetwork = LengthOfRoadNetowrk.index(performanceData_1[0,1])
        RoadNetworkWithLeastLength = LengthOfRoadNetowrk[indexofmin_MaximumPathInthNetwork]
        Solution_positions = SolutionInformation_positions[indexofmin_MaximumPathInthNetwork]
        Solution_links = SolutionInformation_links[indexofmin_MaximumPathInthNetwork]
   
        print(performanceData_1[0,0],performanceData_1[0,1])
        '''

        print('The length of the longest path in the network (with the shortest path found) is:')
        print(round(min_MaximumPathInthNetwork,3))   

        print('Position of the junction nodes e,f,g and h are:')
        print(Solution_positions)
        print(' the junction and the nodes are interlinked according to the matrix :')
        print(Solution_links)
        '''
       
        '''
        # here we are populating the solution information into the original proble (using dictionary format)
        '''
        for i in range(4,8):
            Positions[list(Positions.keys())[i]]['x'] = Solution_positions[i-4][0]
            Positions[list(Positions.keys())[i]]['xy'] = Solution_positions[i-4][1]
            Roads[i]['link'] = Solution_links[i-4]
            
        '''
        # lets plot the solution information
        '''
        plt.figure()
        ax = plt.gca()
        for p in Positions.keys():
            ax.scatter(Positions[p]['x'],Positions[p]['y'],color = 'black',marker = 'x')
            ax.text(Positions[p]['x'],Positions[p]['y'],p,size = 20)   
            
        for r in Roads.keys():
            #if Roads[r]['link'] == 1:
            ax.plot([Positions[Roads[r]['from']]['x'],Positions[Roads[r]['to']]['x']],[Positions[Roads[r]['from']]['y'],Positions[Roads[r]['to']]['y']],color = 'b',linewidth = 5);
            distance = ((Positions[Roads[r]['from']]['x']-Positions[Roads[r]['to']]['x'])**2 + (Positions[Roads[r]['from']]['y']-Positions[Roads[r]['to']]['y'])**2)**0.5;
            ax.text((Positions[Roads[r]['from']]['x']+Positions[Roads[r]['to']]['x'])/2,(Positions[Roads[r]['from']]['y']+Positions[Roads[r]['to']]['y'])/2,round(distance,3),size = 10,color = 'r')
      
'''
##################################################################
'''
def example_5():
    LengthOfRoadNetowrk = []
    # the solution information is the position of the junctions and the information on the links
    SolutionInformation_positions = []
    SolutionInformation_links = []
    NodeNames = list(Positions.keys())
    for z in range(5):
        newPositions = [];
        Edges = [];
        total_distant = 0;
        distance = 0;
        Max_distance = 0;
        thisColor = [rand(),rand(),rand()]
        for i in range(4):
            newPositions.append([round(rand(),3),round(rand(),3)]);
            Edges.append(round(rand()));
        for t,p in enumerate(Positions.keys()):           
            if t>3:
                Positions[p]['x']= newPositions[t-4][0];
                Positions[p]['y']= newPositions[t-4][1];   
            
        for r in range(4,8):    
            Roads[r]['link'] = Edges[(r-4)];
        
        MaximumDistance = []
        for fr in list(Positions.keys())[:4]:
            for to in list(Positions.keys())[:4]:
                if fr != to:
                    print(fr,to)
                    # lets assume a maximum of four roads should lead from any point to the other
                    # we generate many cobmination of links to make different paths and accept those
                    # that lead from the fr to the to everytime
                    # Note that the number of positions we have is 8 [0 to 7]
                    # note also that the first and the last elements of the path are made from 0 to 3 because the locations are from a to d
                    
                    
                    for gg in range(20):
                        path = [round(rand()*3),(4+round(rand()*3)),(4+round(rand()*3)),(4+round(rand()*3)),round(rand()*3)];
       
                        pathName = [NodeNames[t] for t in path]
                        print(pathName)
                        
                        
                        total_distant = 0;
                        for j in range(1,4):
                            LinkExist = False;
                            PathExist = False;
                            for i in Roads.keys():
                                if Roads[i]['link'] == 1 and Roads[i]['from'] == NodeNames[path[j-1]] and  Roads[i]['to']== NodeNames[path[j]]:
                                    LinkExist == True;
                            if LinkExist == False:
                                PathExist = False;
                                break
                            else:
                                PathExist = True;
                        
 
        for r in Roads.keys():
            if Roads[r]['link'] == 1:
                distance = ((Positions[Roads[r]['from']]['x']-Positions[Roads[r]['to']]['x'])**2 + (Positions[Roads[r]['from']]['y']-Positions[Roads[r]['to']]['y'])**2)**0.5;
                total_distant = total_distant + distance;
                numberofLinks = numberofLinks + 1;
        # lets say we are interested in solution with at list interlinkages
        if numberofLinks == 8:
            SolutionInformation_positions.append([newPositions[0],newPositions[1],newPositions[2],newPositions[3]])
            SolutionInformation_links.append([Edges[0],Edges[1],Edges[2],Edges[3]])
            LengthOfRoadNetowrk.append(total_distant)
    min_LengthOfRoadNetowrk = min(LengthOfRoadNetowrk)
    indexOftheShortestRoadNetwork = LengthOfRoadNetowrk.index(min_LengthOfRoadNetowrk)
    RoadNetworkWithLeastLength = LengthOfRoadNetowrk[indexOftheShortestRoadNetwork]
    Solution_positions = SolutionInformation_positions[indexOftheShortestRoadNetwork]
    Solution_links = SolutionInformation_links[indexOftheShortestRoadNetwork]
    print('The road network with the shortest distance found is:')
    print(round(RoadNetworkWithLeastLength,3))
    print('Position of the junction nodes e,f,g and h are:')
    print(Solution_positions)
    print(' the junction and the nodes are interlinked according to the matrix :')
    print(Solution_links)
   
    '''
    # here we are populating the solution information into the original proble (using dictionary format)
    '''
    for i in range(4,8):
        Positions[list(Positions.keys())[i]]['x'] = Solution_positions[i-4][0]
        Positions[list(Positions.keys())[i]]['xy'] = Solution_positions[i-4][1]
        Roads[i]['link'] = Solution_links[i-4]
        
    '''
    # lets plot the solution information
    '''
    plt.figure()
    ax = plt.gca()
    for p in Positions.keys():
        ax.scatter(Positions[p]['x'],Positions[p]['y'],color = 'black',marker = 'x')
        ax.text(Positions[p]['x'],Positions[p]['y'],p,size = 20)   
        
    for r in Roads.keys():
        if Roads[r]['link'] == 1:
            ax.plot([Positions[Roads[r]['from']]['x'],Positions[Roads[r]['to']]['x']],[Positions[Roads[r]['from']]['y'],Positions[Roads[r]['to']]['y']],color = 'b',linewidth = 5);
      
if __name__ == "__main__": 
    Positions = {'a':{'x':0.1,'y':0.5},'b':{'x':0.16,'y':0.1},'c':{'x':0.7,'y':0.3},'d':{'x':0.5,'y':0.9},'e':{'x':0.25,'y':0.25},'f':{'x':0.27,'y':0.45},'g':{'x':0.51,'y':0.59},'h':{'x':0.5,'y':0.3}};
    Roads = {0:{'from':'a','to':'e','link':1}, 1:{'from':'b','to':'h','link':1},2:{'from':'c','to':'g','link':1}, 3:{'from':'d','to':'f','link':1},
             4:{'from':'e','to':'f','link':1}, 5:{'from':'f','to':'g','link':1},6:{'from':'g','to':'h','link':1},7:{'from':'h','to':'e','link':1}};
     
    example_4()
    '''
    example_2()
    example_3()
    example_4()
    '''