# Function to perform Job Sequencing using Greedy strategy
def job_sequencing(jobs):
    # Sort jobs based on profit in descending order
    jobs.sort(key=lambda x: x[1], reverse=True)

    n = len(jobs)
   
    # Find maximum deadline to determine the number of slots
    max_deadline = max(job[2] for job in jobs)
    slots = [False] * max_deadline  # Time slots
    job_result = [''] * max_deadline  # Store job sequence
    total_profit = 0

    for job in jobs:
        job_id, profit, deadline = job
       
        # Find a free slot (latest possible before deadline)
        for i in range(min(deadline, max_deadline) - 1, -1, -1):
            if not slots[i]:
                slots[i] = True
                job_result[i] = job_id
                total_profit += profit
                break

    # Output
    print("\nScheduled Jobs:", end=" ")
    for j in job_result:
        if j != '':
            print(j, end=" ")
    print(f"\nTotal Profit: {total_profit}")

# Take input from user
def main():
    num_jobs = int(input("Enter number of jobs: "))
    jobs = []

    print("Enter job details (JobID Profit Deadline):")
    for _ in range(num_jobs):
        details = input().split()
        job_id = details[0]
        profit = int(details[1])
        deadline = int(details[2])
        jobs.append((job_id, profit, deadline))

    job_sequencing(jobs)

if __name__ == "__main__":
    main()
