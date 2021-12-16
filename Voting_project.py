candidateOne = input("Enter first candidate name:")
candidateTwo = input("Enter second candidate name:")
if candidateOne == candidateTwo:
    print("You already entered this candidate name; Please entered other candidate's name.")
    candidateTwo = input("Enter second candidate name:")
    print("Congrates!! Now Candidate Registration Completed.")
else:
    print("Congrates!! Candidate Registration Completed.")

#  Counter:which is initially 0
candidateOne_Vote_Count = 0
candidateTwo_Vote_Count = 0

# list of voter id's
voters_ID = [1001, 1002, 1003, 1004, 1005,1006,1007,1008,1009,1010]
total_voters = len(voters_ID)
print(f"\nThere are {total_voters} voters present at this booth for voting.")
voted = []

while True:
    if voters_ID == []:
        print("\nVoting Completed Successfully!")
        if candidateOne_Vote_Count > candidateTwo_Vote_Count:
            print(f"{candidateOne} won the election by {candidateOne_Vote_Count} numbers of vote.")
        elif candidateOne_Vote_Count < candidateTwo_Vote_Count:
            print(f"{candidateTwo} won the election by {candidateTwo_Vote_Count} numbers of vote.")
        elif candidateOne_Vote_Count == candidateTwo_Vote_Count:
            print(f"It's tie! Both candidate {candidateOne} and {candidateTwo} got same number of votes that is {candidateTwo_Vote_Count} ")
        break
    else:
        voter = int(input("\nEnter Your id: "))
        if voter in voted:
            print("Your vote already given.")
        else:
            if voter in voters_ID:
                print(f" 1.{candidateOne} \n 2.{candidateTwo}")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    candidateOne_Vote_Count += 1
                elif choice == 2:
                    candidateTwo_Vote_Count += 1
                voters_ID.remove(voter)     # Removing ID's from list
                voted.append(voter)         # adding ID's to voted list
            else:
                print("\nYou are not allowed to vote again.")

