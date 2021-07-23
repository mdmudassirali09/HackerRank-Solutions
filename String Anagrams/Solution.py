def getMinCost(crew_id, job_id):
    c=sorted(crew_id)
    j=sorted(job_id)
    sum=0
    for i in range(len(c)):
        sum+=(abs(c[i]-j[i]))
    return sum

if __name__ == "__main__":
    crew_id_count = int(input())
    crew_id=[]
    for _ in range(crew_id_count):
        crew_id.append(int(input()))
    job_id_count = int(input())
    job_id=[]
    for _ in range(job_id_count):
        job_id.append(int(input()))
    print(getMinCost(crew_id, job_id))