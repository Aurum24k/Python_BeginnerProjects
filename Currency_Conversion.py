#This programm is used for currency conversion of USD/CAD/EUR/INR only. Created by Aniket Ullewar

def conversion(amount,From,To):
    rates={"USD":{"CAD":1.38,"EUR":0.87,"INR":85.43},
           "CAD":{'USD':0.72,"EUR":0.63,"INR":61.78},
           "EUR":{"USD":1.14,"CAD":1.58,"INR":97.44},
           "INR":{"USD":0.012,"CAD":0.016,"EUR":0.010},
           }
    return amount*rates[From][To]

history=[]
while True:
    try:
        amount=float(input("Enter the amount:"))
        From=(input("Source currency (USD/CAD/EUR/INR):")).upper().strip()
        To=(input("Target currency (USD/CAD/EUR/INR):")).upper().strip()

        if From==To:
            amount=f"{amount} {From} is equal to {amount} {To}"
            print(amount)
            history.append(amount)
        else:
            data=conversion(amount,From,To)
            print(f"{amount} {From} is equal to {data} {To}")
            history.append(data)
    except ValueError:
        print("Invalid input")
        continue        
    except KeyError:
        print("Invalid input or the currency doesnt exist in this code")
        continue

    again=(input("wanna try again (y/n):")).lower()
    if(again=="n"):
        break

print("History:",history)