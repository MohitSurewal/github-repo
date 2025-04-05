from collections import deque

class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid         # Process ID
        self.burst_time = burst_time  # Burst Time (execution time)
        self.remaining_time = burst_time  # Remaining time (for RR scheduling)

def round_robin(processes, quantum):
    queue = deque(processes)  # Process queue (FIFO)
    time = 0  # Tracks the current time

    while queue:
        current_process = queue.popleft()  # Get the first process in the queue
        print(f"Time {time}: Process {current_process.pid} starts execution")

        if current_process.remaining_time > quantum:
            current_process.remaining_time -= quantum
            time += quantum
            queue.append(current_process)  # Re-queue the process with remaining time
            print(f"Time {time}: Process {current_process.pid} executed for {quantum} units. Remaining time: {current_process.remaining_time}")
        else:
            time += current_process.remaining_time
            print(f"Time {time}: Process {current_process.pid} finished execution in {current_process.remaining_time} units.")
            current_process.remaining_time = 0  # Process is finished

        print(f"Time {time}: Process {current_process.pid} completed\n")

# Example usage
if __name__ == "__main__":
    processes = [
        Process(1, 10),  # Process 1 with burst time of 10 units
        Process(2, 5),   # Process 2 with burst time of 5 units
        Process(3, 8),   # Process 3 with burst time of 8 units
        Process(4, 6)    # Process 4 with burst time of 6 units
    ]

    quantum = 4  # Time quantum (time slice)
    
    print(f"Round Robin CPU Scheduling Simulation (Quantum: {quantum} units)\n")
    round_robin(processes, quantum)
