class InstagramAccount:
    def __init__(self, account_name, password):
        # Public variable
        self.account_name = account_name

        # Protected variable
        self._private_reels = []

        # Private variables
        self.__archived_reels = []
        self.__password = password

    # Add private reel
    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)

    # Display private reels
    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:", self._private_reels)
        else:
            print("Access Denied! Only followers can view private reels")

    # Add archived reel
    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)

    # Display archived reels
    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:", self.__archived_reels)
        else:
            print("Access Denied! Only account holder can view archived reels")

    # Getter method for archived reels
    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied!"

    # Setter method to update password
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully!")
        else:
            print("Wrong password! Cannot update.")


# --------- Object Creation and Method Calls ---------

account = InstagramAccount("chandana_insta", "1234")

# Add private reels
account.add_private_reel("Private Reel 1")
account.add_private_reel("Private Reel 2")

# Add archived reels
account.add_archived_reel("Archived Reel 1")
account.add_archived_reel("Archived Reel 2")

# Display private reels
print("\nFollower View:")
account.display_private_reels(True)

print("\nNon-Follower View:")
account.display_private_reels(False)

# Display archived reels
print("\nCorrect Password:")
account.display_archived_reels("1234")

print("\nWrong Password:")
account.display_archived_reels("0000")

# Update password
print("\nUpdating Password:")
account.set_password("1234", "5678")

# Check again with new password
print("\nAfter Password Update:")
account.display_archived_reels("5678")