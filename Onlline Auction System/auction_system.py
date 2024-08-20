class User:
    def __init__(self, username):
        self.username = username

class Auction:
    def __init__(self, item_name):
        self.item_name = item_name
        self.bids = []

    def place_bid(self, bid):
        self.bids.append(bid)

    def get_highest_bid(self):
        if self.bids:
            return max(self.bids)
        return 0

def main():
    users = {}
    auctions = {}

    while True:
        print("\nWelcome to the Online Auction System!")
        print("1. Register User")
        print("2. Create Auction")
        print("3. Place Bid")
        print("4. View Auctions")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter your username: ")
            users[username] = User(username)
            print(f"User '{username}' registered successfully.")

        elif choice == '2':
            item_name = input("Enter the item name for auction: ")
            auction = Auction(item_name)
            auctions[item_name] = auction
            print(f"Auction for '{item_name}' created successfully.")

        elif choice == '3':
            item_name = input("Enter the item name to bid on: ")
            if item_name in auctions:
                bid = float(input("Enter your bid amount: "))
                auctions[item_name].place_bid(bid)
                print(f"Bid of {bid} placed on '{item_name}' successfully.")
            else:
                print("Auction not found.")

        elif choice == '4':
            print("\nCurrent Auctions:")
            for item_name, auction in auctions.items():
                highest_bid = auction.get_highest_bid()
                print(f"Item: {item_name}, Highest Bid: {highest_bid}, Bids: {auction.bids}")

        elif choice == '5':
            print("Exiting the auction system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()