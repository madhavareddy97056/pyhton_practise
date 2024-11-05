print("Welcome to BMR sports academy. please select required sports")
game = input("Enter outdoor_sports (or) indoor_sports (or) atheletes:")

outdoor_sports = ["cricket", "volleyball", "football", "hockey", "badminton", "golf", "baseball", "tennis", "koko", "kabaddi"]
indoor_sports = ("carrom", "chess", "tt", "badminton")
atheletics = {"water":"swimming", "rope":"skipping","grond":"running", "weights":"gym"}

if game in outdoor_sports:
    print(f"The sport {game} has available seats. please book your membership")
elif game in indoor_sports:
    print(f"The sport {game} has no seats left. Try another sport.")
elif game in atheletics.values():
    print(f"The selected sport {game} is not available in the academy. We are sorry for inconvinience.")
else:
    print(f"The selected sport {game} is not available in this academy")
