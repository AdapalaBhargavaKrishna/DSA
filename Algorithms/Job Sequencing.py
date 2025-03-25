class Job:
    def __init__(self, id, dl, profit):
        self.id = id
        self.dl = dl
        self.profit = profit

def job_sequencing(jobs):
    jobs.sort(key=lambda job: job.profit, reverse = True)
    max_dl = max(job.dl for job in jobs)
    slots = [-1]*(max_dl + 1)
    total_profit = 0

    for job in jobs:
        for j in range(job.dl, 0, -1):
            if slots[j] == -1:
               slots[j] = job.id 
               total_profit += job.profit
               break
            
    js = [job for job in slots if job != -1]

    return js, total_profit

jobs = []

n = int(input("Enter number of jobs:"))

for i in range(n):
    print(f"\nEnter details for job{i + 1}:")
    id = str(input(f"Enter id of the job{i + 1}:"))
    dl = int(input(f"Enter deadline of the job{i + 1}:"))
    profit = int(input(f"Enter profit of the job{i + 1}:"))

    jobs.append(Job(id,dl,profit))
    
scheduled_jobs, total_profit = job_sequencing(jobs)
print("Scheduled Jobs:", scheduled_jobs)
print("Total Profit:", total_profit)