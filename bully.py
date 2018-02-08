#CSC 315 DISTRIBUTED SYSTEMS
#P15/1691/2016
#BULLY ALGORITHM

# the shared knowledge repository where a node knows the ids of other nodes and hence priority
def process_Pool(id,message_case=0):
    nodes_list = [1, 2, 3, 4,5] # id of the nodes in the networks
    if message_case==1: # sending the election request, message=election
        new_list=[]
        for x in nodes_list:
            if id<x:
                new_list.append(x) # create a list of nodes with an id higher
                #than the current node denoted by the parameter id
        if id==len(nodes_list): # last node in the list
             return None # theres no higher priority node

        return new_list # return list of higher priority nodes
    if message_case==2 and id is not 1:#sending an ok mesage within the time limit
        return [nodes_list[int(id)-2] ]# return id of predecessor node in priority hierachy
    if message_case==3: #sending an Ive won message to other nodes
        del nodes_list[len(nodes_list)-1] # pop the highest id and form a list of recepients which is
        #everyone else
        return nodes_list # updated list with recepients being everyone minus the winner


#simulate communication of nodes
def sending_data(recepients,message): # recepients list and message to be sent

    if recepients is not None:# no empty list
        for node in recepients:
            print(message+" sent to Node"+str(node)) # emulate send message via print

# Construct a node
def node(myId):
    sending_list=process_Pool(myId,1)
    if  sending_list is None: # meaning no node is higher and thus, this node has won
        sending_data(process_Pool(myId,3),"I've won") # when the highest node wins
    else :
        sending_data(sending_list,"Election") # forward an election message to your successor in the priority list
    sending_data(process_Pool(myId,2),"OK") #send data to your predecessor in the priority list

#Initialize program by simulating the starting of nodes
# by calling the node function
node(1)
node(2)
node(3)
node(4)
node(5)
