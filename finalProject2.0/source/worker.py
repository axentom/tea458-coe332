from jobs import q, update_job_status
import time

@q.worker
def execute_job(jid):
    update_job_status(jid, 'in progress')
    time.sleep(15)
    # Create figure
    update_job_status(jid, 'complete')
    
if __name__ == '__main__':
    execute_job()
