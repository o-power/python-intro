# 1. Create three lists of car models, each list should only have the models for a particular manufacturer. 
#    For example, you could have one list of Fords, one of Toyotas, and one of Reanults. Give the lists 
#    appropriate names
nissan_models = ['Micra','Leaf','Qashqai','Juke']
toyota_models = ['Yaris','Corolla','RAV4','C-HR','Prius']
volkswagen_models = ['Polo','Golf','Passat','Jetta']

# 2. Create a list called car_models with the three lists of car models as items in the new list
car_models = [nissan_models, toyota_models, volkswagen_models]
#print(car_models)

# 3. Iterate over the list to print each nested list of car models, the output would look similar to this:
for car_model in car_models:
    print(car_model)