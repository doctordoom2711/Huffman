from functools import cmp_to_key

class Job:
    def __init__(self, id, time, loss):
        self.id = id
        self.time = time
        self.loss = loss

def compare_jobs(job1, job2):
    ratio1 = job1.loss * job2.time
    ratio2 = job2.loss * job1.time
    if ratio1 != ratio2:
        return 1 if ratio2 > ratio1 else -1
    return -1 if job1.id < job2.id else 1

def minimize_loss_sequence(times, losses):
    n = len(times)
    jobs = []
    for i in range(n):
        jobs.append(Job(id=i + 1, time=times[i], loss=losses[i]))
    jobs.sort(key=cmp_to_key(compare_jobs))
    return [job.id for job in jobs]

if __name__ == "__main__":
    job_durations = [4, 1, 3, 2, 5]
    job_losses = [2, 10, 1, 4, 5]
    sequence = minimize_loss_sequence(job_durations, job_losses)
    print(f"Optimal Job Sequence to Minimize Loss: {sequence}")
