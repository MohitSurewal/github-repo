from collections import deque

class Process:
    def __init__(self, pid, burst_time):
          self.pid = pid   
          self.burst_time = burst_time
          self.remaining_time = burst_time

def round_robin(processes, quantum):
    queue = deque (processes)
    time = 0
    while queue:
         current_process = queue.popleft()
         print(f"Time {time}: proces {current_process.pid}start execution")

         if current_process.remaining_time > quantum:
              current_process.remaining_time -= quantum
              time += qauntum
              queue.append(current_process)
              print(f"time {time}: process {current_process.pid} executed for {quantum}Units.Remaining time: {current_process.remaining_time}")

                   
         else:
              time += current_process.remaining_time
              print(f"time {time}: process {current_process.pid} Finished Execution in      {current_process.remaining_time}units")
              current_process.remaining_time = 0

         print(f"time {time}: process {current_process.pid} completed\n")

         if __name__ == "__main__":
             processes = [
                 Process(1, 10),
                 Process(2, 5),
                 Process(3, 8),
                 Process(4, 6)
                  
        
             ]

             quantum = 4 
             print(f"Round Robin CPU Schedulling simulation (Quantumn: {quantum}units)\n")
             round_robbin(processes, quantum)

  