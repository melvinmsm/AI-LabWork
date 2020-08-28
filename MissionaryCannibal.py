#using bfs - Finds path to successfully transport 3 cannibals and 3 missionaries from one side of river to another, and the cost of the operation
def Missionary_cannibals(initial_state, goal_state):
    directions = {1:0,0:1}
    queue = [initial_state]
    history = set()
    cost = 0
    history.add(initial_state)
    while(len(queue)>0):
        print(queue)
        cost += 1
        length = len(queue)
        for i in range(0,length):
            curr_state = queue.pop(0)
            print("curr_state: {}".format(curr_state))
            if(curr_state==goal_state):
                print("End reached")
                break
            else:
                curr_state_M, curr_state_P,curr_state_direction = curr_state
                opposite_state_M, opposite_state_P,opposite_state_direction = 3 - curr_state_M, 3 - curr_state_P, directions[curr_state_direction]
                #If the boat is on left side of bank
                if((curr_state_M>=curr_state_P or curr_state_M==0) and (opposite_state_M>=opposite_state_P or opposite_state_M==0) and curr_state_direction==1):
                    if(curr_state_M>0 and (curr_state_M-1,curr_state_P,opposite_state_direction) not in history):
                        queue.append((curr_state_M-1,curr_state_P,opposite_state_direction))
                        history.add((curr_state_M-1,curr_state_P,opposite_state_direction))
                    if(curr_state_P>0 and (curr_state_M,curr_state_P-1,opposite_state_direction) not in history):
                        queue.append((curr_state_M,curr_state_P-1,opposite_state_direction))
                        history.add((curr_state_M,curr_state_P-1,opposite_state_direction))
                    if(curr_state_M>1 and (curr_state_M-2,curr_state_P,opposite_state_direction) not in history):
                        queue.append((curr_state_M-2,curr_state_P,opposite_state_direction))
                        history.add((curr_state_M-2,curr_state_P,opposite_state_direction))
                    if(curr_state_P>1 and (curr_state_M,curr_state_P-2,opposite_state_direction) not in history):
                        queue.append((curr_state_M,curr_state_P-2,opposite_state_direction))
                        history.add((curr_state_M,curr_state_P-2,opposite_state_direction))
                    if(curr_state_P>0 and curr_state_M>0 and (curr_state_M-1,curr_state_P-1,opposite_state_direction) not in history):
                        queue.append((curr_state_M-1,curr_state_P-1,opposite_state_direction))
                        history.add((curr_state_M-1,curr_state_P-1,opposite_state_direction))
                #If the boat is on right side of bank
                if((curr_state_M>=curr_state_P or curr_state_M==0) and (opposite_state_M>=opposite_state_P or opposite_state_M==0) and curr_state_direction==0):
                    if(opposite_state_M>0 and (curr_state_M+1,curr_state_P,opposite_state_direction) not in history):
                        queue.append((curr_state_M+1,curr_state_P,opposite_state_direction))
                        history.add((curr_state_M+1,curr_state_P,opposite_state_direction))
                    if(opposite_state_P>0 and (curr_state_M,curr_state_P+1,opposite_state_direction) not in history):
                        queue.append((curr_state_M,curr_state_P+1,opposite_state_direction))
                        history.add((curr_state_M,curr_state_P+1,opposite_state_direction))
                    if(opposite_state_M>1 and (curr_state_M+2,curr_state_P,opposite_state_direction) not in history):
                        queue.append((curr_state_M+2,curr_state_P,opposite_state_direction))
                        history.add((curr_state_M+2,curr_state_P,opposite_state_direction))
                    if(opposite_state_P>1 and (curr_state_M,curr_state_P+2,opposite_state_direction) not in history):
                        queue.append((curr_state_M,curr_state_P+2,opposite_state_direction))
                        history.add((curr_state_M,curr_state_P+2,opposite_state_direction))
                    if(opposite_state_M>0 and opposite_state_P>0 and (curr_state_M+1,curr_state_P+1,opposite_state_direction) not in history):
                        queue.append((curr_state_M+1,curr_state_P+1,opposite_state_direction))
                        history.add((curr_state_M+1,curr_state_P+1,opposite_state_direction))
    return cost


initial_state = (3,3,1)
final_state = (0,0,0)

print(Missionary_cannibals(initial_state,final_state))
