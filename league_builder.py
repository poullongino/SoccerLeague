import csv

# global variables declaration tests
yes_list = []
no_list = []


# Creating Teams with Equal Number of Players and Experience
def Teams(yes, no):
    x = ', '.join(yes[:4])
    with open("teams.txt", 'w') as teamfile:
        # Writing the -*- SHARKS -*- team to teams.txt file
        teamfile.write("SHARKS" + "\n")
        teamfile.write("="*len(x) + "\n")
        teamfile.write(', '.join(yes[:4]))
        teamfile.write("\n")
        teamfile.writelines(', '.join(no[:4]))
        teamfile.write("\n")
        teamfile.writelines(', '.join(yes[4:8]))
        teamfile.write("\n")
        teamfile.writelines(', '.join(no[4:8]))
        teamfile.write("\n")
        teamfile.writelines(', '.join(yes[8:12]))
        teamfile.write("\n")
        teamfile.writelines(', '.join(no[8:12]))
        teamfile.write("\n\n")

        # Writing the -*- DRAGON -*- team to teams.txt file
        teamfile.write("DRAGONS" + "\n")
        teamfile.write("=" * len(x) + "\n")
        teamfile.write(', '.join(yes[12:16]))
        teamfile.write("\n")
        teamfile.writelines(', '.join(no[12:16]))
        teamfile.write("\n")
        teamfile.writelines(', '.join(yes[16:20]))
        teamfile.write("\n")
        teamfile.writelines(', '.join(no[16:20]))
        teamfile.write("\n")
        teamfile.writelines(', '.join(yes[20:24]))
        teamfile.write("\n")
        teamfile.writelines(', '.join(no[20:24]))
        teamfile.write("\n\n")

        # Writing the -*- RAPTORS -*- team to teams.txt file
        teamfile.write("RAPTORS" + "\n")
        teamfile.write("=" * len(x) + "\n")
        teamfile.write(', '.join(yes[24:28]))
        teamfile.write("\n")
        teamfile.writelines(', '.join(no[24:28]))
        teamfile.write("\n")
        teamfile.writelines(', '.join(yes[28:32]))
        teamfile.write("\n")
        teamfile.writelines(', '.join(no[28:32]))
        teamfile.write("\n")
        teamfile.writelines(', '.join(yes[32:36]))
        teamfile.write("\n")
        teamfile.writelines(', '.join(no[32:36]))

# Sorting Players with Experience and Without Experience
def sort_players():
    with open("soccer_players.csv", newline='') as csvplayers:
        players_dict = csv.DictReader(csvplayers)
        for row in players_dict:
            # Creating a list of Experienced Players
            if row['Soccer Experience'] == 'YES':
                yes_list.extend([row['Name'], row['Height (inches)'], row['Soccer Experience'], row['Guardian Name(s)']])
            # Creating a list of None Experience Players
            if row['Soccer Experience'] == 'NO':
                no_list.extend([row['Name'], row['Height (inches)'], row['Soccer Experience'], row['Guardian Name(s)']])

def invitation(player_inv, player, guardian, team):
    with open(player_inv, 'w') as inv_letter:
        inv_letter.write("""Hello Mr/Mrs.{}, 
           we are happy to inform you that your Son {} is now a {} player. We expect the first training
           to be on 6/2/2018. hope to see you there!""". format(guardian, player, team))

# Running the main script
if __name__ == '__main__':
    sort_players()
    Teams(yes_list, no_list)

    # Composing invitation letters
    invitation("joe_smith.txt","Joe Smith", "Jim and Jan Smith", "Sharks")
    invitation("eva_gordon.txt","Eva Gordon", "Wendy and Mike Gordon", "Sharks")
    invitation("jill_tanner.txt","Jill Tanner", "Clara Tanner", "Sharks")
    invitation("matt_gill.txt","Matt Gill", "Charles and Sylvia Gill", "Sharks")
    invitation("bill_bon.txt","Bill Bon", "Sara and Jenny Bon", "Sharks")
    invitation("kimmy_stein.txt","Kimmy stein", "Bill and Hillary Stein", "Sharks")

    invitation("karl_saygan.txt","Karl Saygan", "Heather Bledsoe", "Dragons")
    invitation("sammy_adams.txt","Sammy Adams", "Jeff Adams", "Dragons")
    invitation("suzane_greenberg.txt","Suzane Greenberg", "Henrietta Dumas", "Dragons")
    invitation("sal_dali.txt","Sal Dali", "Gala Dali", "Dragons")
    invitation("diego_soto.txt","Diego Soto", "Robin and Sarika Soto", "Dragons")
    invitation("joe_kavalier.txt","Joe Kavalier", "Sam and Elaine Kavalier", "Dragons")

    invitation("phillip_helm.txt","Phillip Helm", "Thomas Helm and Eva Jones", "Raptors")
    invitation("ben_finkelstein.txt","Ben Finkelstein", "Aaron and Jill Finkelstein", "Raptors")
    invitation("les_clay.txt","Les Clay", "Wynonna Brown", "Raptors")
    invitation("chloe_alaska.txt","Chloe Alaska", "David and Jamie Alaska", "Raptors")
    invitation("herschel_krustofski.txt","Herschel Krustofski", "Hyman and Rachel Krustofski", "Raptors")
    invitation("arnold_willis.txt","Anord Willis", "Claire Willis", "Raptors")
