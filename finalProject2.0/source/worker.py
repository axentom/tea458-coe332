from jobs import rd, q, update_job_status
from api import get_data
from matplotlib import pyplot as plt

@q.worker
def execute_job(jid):
    update_job_status(jid, 'in progress')

    # Create figure
    count = int(rd.get('count'))
    adoptions_dict = get_data()
    age_x = []
    adoptions_y = []
    for i in range(0, count):
        if (adoptions_dict[i]["Outcome Type"] == "Adoption"):
            adoption_age = adoptions_dict[i]["Age upon Outcome"]
                if adoption_age not in age_x:
                    age_x.append(adoption_age)
                    adoptions_y.append(1)
                else:
                    for index, item in enumerate(age_x):
                        if item == adoption_age:
                            adoptions_y[index] = adoption_y[index] + 1
    plt.bar(age_x, adoptions_y)
    plt.xlabel('Adoption Age')
    plt.ylabel('# of Adoptions')
    plt.savefig('adoption_ages.png')

    update_job_status(jid, 'complete')
    
if __name__ == '__main__':
    execute_job()
