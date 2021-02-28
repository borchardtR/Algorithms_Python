"""
Title: cpm.py
Author: Ryan Borchardt

This module allows for parallel precedence-constrained job scheduling by implementing the critical path method.

It determines the optimal time to start each job based on determining when all of the jobs a job depends on are completed. 

Starting each job at the time determined by this module will allow for:
    1. Being confident that the entire pipeline of jobs will run (b/c we know that for any given job, all of its dependencies will finish running before that job starts running).
        Another way of stating this is knowing that for a given job, by the time it begins executing, we know that all of its constraints have completed.
    2. That the entire pipeline of jobs will complete in the minimum amount of time possible. 

By scheduling each job to start executing at the time it takes for the longest path:
1. We know that all of its dependencies have finished executing: the dependencies in the longest path have JUST finished executing and all other dependencies in shorter paths have finished executing before that.
2. We are starting each job at the earliest time possible (once the latest dependency has finished executing). 

Example: look at job #2:
    We are limited by the longest path to 2 (this corresponds to when the latest dependency has finished executing).
 


This critical path method takes linear time. 
    For N jobs, there are 2*N+2 vertices and a max of ~ (2*N+2)^2 edges 
    # of vertices is proportional to N and # of edges is propotional to N^2
    1. Build an empty ewdag to represent the job pipeline: time proportional to N
    2. Add all edges to the ewdag: time proportional to N^2
    3. Determine the longest path for each vertex: time proportional to V + E which is time proportional to N + N^2
    Overall, the critical path method takes time proportional to N^2 + N (worst-case) which is equivalent to saying E + V (which is considered linear time)
    


# Example:
# python cpm.py jobsPC.txt ' '
#
"""

import sys
from chapter_4.edge_weighted_digraphs.directed_edge import Directed_Edge
from chapter_4.edge_weighted_digraphs.edge_weighted_digraph import Edge_Weighted_Digraph
from chapter_4.edge_weighted_digraphs.lp_acyclic import Longest_Paths


def build_ewdag(filename, delimter):
    file_object = open(filename, 'r')
    
    num_jobs = int(file_object.readline())
    
    ewdag = Edge_Weighted_Digraph(num_jobs*2+2)
    
    source_vertex = num_jobs*2
    target_vertex = num_jobs*2 + 1
    
    for i in range(num_jobs):
        list_string = file_object.readline().split(delimter)
        duration = float(list_string[0])
        
        
        job_i_beginning_to_end_edge = Directed_Edge(v=i, w=i+num_jobs, weight=duration)
        ewdag.addEdge(job_i_beginning_to_end_edge)
        
        source_to_job_i_beginning_edge = Directed_Edge(v=source_vertex, w=i, weight=0)
        ewdag.addEdge(source_to_job_i_beginning_edge)
        
        job_i_end_to_target_edge = Directed_Edge(v=i+num_jobs, w=target_vertex, weight=0)
        ewdag.addEdge(job_i_end_to_target_edge)
        
        for x in range(1, len(list_string)):
            j = int(list_string[x])
            job_i_end_to_job_j_beginning_edge = Directed_Edge(v=i+num_jobs, w=j, weight=0)
            ewdag.addEdge(job_i_end_to_job_j_beginning_edge)
        
    
    return ewdag
    
def scheduler(ewdag):
    lp_acyclic = Longest_Paths(ewdag, s=ewdag.V()-2)
    
    scheduler_string = "Start times: \n"
    for i in range(int(ewdag.V()/2 - 1)):
        scheduler_string = scheduler_string + str(i) +":" + str(lp_acyclic.distTo(i)) +"\n"
    total_time_string = "Finish time: " + str(lp_acyclic.distTo(ewdag.V()-1))
    scheduler_string = scheduler_string + total_time_string
    return scheduler_string 
        
def main():
    ewdag = build_ewdag(sys.argv[1], sys.argv[2])
    schedule_string = scheduler(ewdag)
    print(schedule_string)
    
    

if __name__=="__main__": main()