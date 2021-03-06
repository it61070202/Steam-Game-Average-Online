import csv
import time
# ... is location file from your computer or notebook.
def read():
    with open('C:/Users/Meow Bank/Desktop/project_psit/Data/Data_Player_Averager.csv') as csvfile:
        print("Start Program.")
        print("Loading.")
        time.sleep(1)
        print("Reading data.")
        reader = csv.reader(csvfile)
        pubg = []
        dota2 = []
        csgo = []
        poe = []
        rainbow6 = []
        for row in reader:
            pubg.append([row[0],row[1],row[2]])
            dota2.append([row[0],row[1],row[3]])
            csgo.append([row[0],row[1],row[4]])
            poe.append([row[0],row[1],row[5]])
            rainbow6.append([row[0],row[1],row[6]])
            time.sleep(0.05)

        print("Reading completed.")
        time.sleep(1)
        print("Start writing data.")
        print("loading.")

        write('pubg', pubg)
        write('dota2', dota2)
        write('csgo', csgo)
        write('poe', poe)
        write('rainbow6', rainbow6)

        print("Writing completed.")
        print("Finish Program.")

def write(name, game):
    if name == 'pubg':
        writer = csv.writer(open("C:/Users/Meow Bank/Desktop/project_psit/Data/PUBG.csv", 'w',  newline=''))
        for data in game:
            writer.writerow((data))
            time.sleep(0.05)
        print('"PUBG.csv" finished writing')

    if name == 'dota2':
        writer = csv.writer(open("C:/Users/Meow Bank/Desktop/project_psit/Data/DOTA2.csv", 'w',  newline=''))
        for data in game:
            writer.writerow((data))
            time.sleep(0.05)
        print('"DOTA2.csv" finished writing')

    if name == 'csgo':
        writer = csv.writer(open("C:/Users/Meow Bank/Desktop/project_psit/Data/CS_GO.csv", 'w',  newline=''))
        for data in game:
            writer.writerow((data))
            time.sleep(0.05)
        print('"CS_GO.csv" finished writing')

    if name == 'poe':
        writer = csv.writer(open("C:/Users/Meow Bank/Desktop/project_psit/Data/POE.csv", 'w',  newline=''))
        for data in game:
            writer.writerow((data))
            time.sleep(0.05)
        print('"POE.csv" finished writing')

    if name == 'rainbow6':
        writer = csv.writer(open("C:/Users/Meow Bank/Desktop/project_psit/Data/R6.csv", 'w',  newline=''))
        for data in game:
            writer.writerow((data))
            time.sleep(0.05)
        print('"R6.csv" finished writing')
read()
