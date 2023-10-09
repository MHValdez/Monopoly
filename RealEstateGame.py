# Author:           Marcos Valdez
# GitHub username:  MHValdez
# Date:             05/27/2022
# Description:      A collection of classes representing objects needed to
#                   play a simplified version of Monopoly. The board has
#                   25 spaces (including GO) and there is a 2 player minimum.
#                   Property rent values, number of players, player names,
#                   player starting balances, and GO space payout are set by
#                   the user. Property purchase values are 5x rent.


class Space:
    """
    Represents a space on a game board with a unique name
    and value.
    """
    def __init__(self, name, value):
        """
        Creates a new space of specified name and value.
        :param name: string representing the space's name
        :param value: int or float representing a monetary value
        """
        self._name = name
        self._value = value

    def get_name(self):
        """
        Getter for name
        :return: string representing space's name
        """
        return self._name


class GO(Space):
    """
    Represents a GO type of Space class object called "GO" with
    a user defined payout value. Cannot be owned and does not
    have ownership functionality.
    """
    def __init__(self, payout):
        """
        Creates a new GO space with the name "GO" and specified
        payout value.
        :param payout: int or float representing a monetary value
        """
        super().__init__("GO", payout)

    def get_payout(self):
        """
        Getter for value, the GO space's payout
        :return: int or float representing space's payout value
        """
        return self._value


class Property(Space):
    """
    Represents a property type of Space class object with a unique name,
    a user defined rent value, and a purchase price of 5x rent. Has an
    owner that is initialized to None, can be set to a Player class object,
    and can be reverted to None.
    """
    def __init__(self, name, rent):
        """
        Creates a new Property space of specified name and rent,
        a price of 5x rent, and no owner.
        :param name: string representing the space's name
        :param rent: int or float representing a monetary value
        """
        super().__init__(name, rent)
        self._price = self._value * 5
        self._owner = None

    def get_rent(self):
        """
        Getter for value, the property space's rent
        :return: int or float representing space's rent value
        """
        return self._value

    def get_price(self):
        """
        Getter for price, which is a function of the property
        space's value
        :return: int or float representing space's purchase price
        """
        return self._price

    def get_owner(self):
        """
        Getter for owner
        :return: Player object representing space's owner (None if no owner)
        """
        return self._owner

    def set_owner(self, buyer):
        """
        Setter for owner
        :param buyer: Player class object or None
        :return: None
        """
        self._owner = buyer


class Player:
    """
    Represents a player with a name, a balance, and a position on the
    game board
    """
    def __init__(self, name, balance):
        """
        Creates a new player positioned at GO (index 0) with the specified
        name and balance.
        :param name: string representing the player's name
        :param balance: int or float representing the player's balance
        """
        self._name = name
        self._balance = balance
        self._pos = 0

    def get_name(self):
        """
        Getter for name
        :return: string representing player's name
        """
        return self._name

    def get_balance(self):
        """
        Getter for balance
        :return: int or float representing player's balance
        """
        return self._balance

    def get_pos(self):
        """
        Getter for pos
        :return: int representing the index of the player's position
        """
        return self._pos

    def set_pos(self, pos):
        """
        Setter for pos
        :param pos: int representing the new index of player's position
        :return: None
        """
        self._pos = pos

    def update_balance(self, amount):
        """
        Alters player's balance by amount. Amount can be either positive
        or negative to reflect a payment or charge.
        :param amount: int or float representing a monetary value
        :return: None
        """
        if amount < -self._balance:     # Disallow balance below 0
            self._balance = 0
        else:
            self._balance += amount


class RealEstateGame:
    """
    Represents a simplified version of Monopoly including the board layout,
    states of players, and current game state. Initializes to an empty board
    with no players.
    Has a method to create a list of 1 GO class object and 24 Property class
    objects (subclasses of Space) representing the game board.
    Has a method to create a new Player class object.
    Has methods to query Player objects for balance and position to track
    state of play.
    Has a method that allows a player to buy a property space, updating the
    Property object's ownership.
    Has a method that moves the player, modifying the Player object's position.
    If necessary, modifies the balance of relevant Player objects and ownership
    of relevant Space objects.
    Has a method to check for a win condition and return the winning Player
    object's name.
    """
    def __init__(self):
        """
        Creates a new game with no board and no players.
        """
        self._board = []
        self._players = []

    def create_spaces(self, payout, rents):
        """
        Creates 1 GO class object and 24 uniquely named Property class
        objects based on the parameters and stores them in a list
        representing the game board. Will replace existing board if
        called again.
        :param payout: int or float representing payout amount for GO space
        :param rents: list of 24 ints or floats representing space rent values
        :return: None
        """
        self._board = []                # Reinitialize board

        self._board.append(GO(payout))  # Create GO space

        prop_num = 1
        for rent in rents:              # Create property spaces
            if prop_num < 10:
                self._board.append(Property(f"Prop_0{prop_num}", rent))
            else:
                self._board.append(Property(f"Prop_{prop_num}", rent))
            prop_num += 1

    def create_player(self, name, balance):
        """
        Creates a Player object based on the parameters. Does not allow
        players with duplicate names.
        :param name: string representing player name
        :param balance: int or float representing player starting balance
        :return: None
        """
        found = False

        for player in self._players:        # Check if player with name
            if player.get_name() == name:   # already exists
                found = True

        if not found:
            self._players.append(Player(name, balance))

    def get_space(self, index):
        """
        Getter for Space class objects on board
        :param index: integer representing index of space [0..24]
        :return: Space class object with the passed index
        """
        return self._board[index]

    def get_player(self, name):
        """
        Getter for Player class objects in player list
        :param name: string representing player name
        :return: Player class object with the passed name
        """
        for player in self._players:
            if player.get_name() == name:
                return player

    def get_player_account_balance(self, name):
        """
        Retrieves the current balance of the Player object with the passed name
        :param name: string representing player name
        :return: int or float representing player's current balance
                 None if player doesn't exist
        """
        player = self.get_player(name)

        if player is not None:
            return player.get_balance()

    def get_player_current_position(self, name):
        """
        Retrieves the current position of the Player object with the passed name
        :param name: string representing player name
        :return: int representing the index of the player's position
                 where GO is at index 0
                 None if player doesn't exist
        """
        player = self.get_player(name)

        if player is not None:
            return player.get_pos()

    def buy_space(self, name):
        """
        Allows player to purchase a Property space. Updates Property object's
        owner data member to the Player object with the passed name if space
        is not already owned and player's balance is greater than or equal to
        space's purchase price. Reduces player's balance by amount equal to
        space's purchase price under same conditions. Does not allow purchase
        of GO space.
        :param name: string representing player name
        :return: True if purchase is successful, False otherwise
        """
        player = self.get_player(name)

        if player is not None:              # Ignore nonexistent players
            pos = self.get_player_current_position(name)

            if pos == 0:                    # Ignore players that have lost
                return False

            space = self.get_space(pos)
            owner = space.get_owner()

            if owner is not None:           # Ignore requests to purchase
                return False                # owned space

            balance = self.get_player_account_balance(name)
            price = space.get_price()

            if price > balance:             # Ignore request to purchase
                return False                # space out of budget

            player.update_balance(-price)   # Purchase space
            space.set_owner(player)

            return True

    def move_player(self, name, spaces):
        """
        Updates the position of Player object with the passed name. Moves the player
        to the position "spaces" indices above the previous position. Treats the board
        list as a loop in cases where this value is beyond the range of spaces. Pays
        player GO payout if player lands on or passes GO. Charges player rent if player
        lands on a space owned by a different player (paid to said player). Reduces
        player balance by rent amount or player balance (whichever is smaller) and
        increases owner player's balance by same amount. If player's account balance
        becomes 0 after rent charge, the owner of any spaces the player owns is updated
        to None. Does not move players with an existing balance of 0.
        :param name: string representing player name
        :param spaces: int in range [1..6] representing spaces to move
        :return: None
        """
        player = self.get_player(name)
        balance = 0
        pos = 0
        board_size = len(self._board)

        if player is not None:                  # Ignore nonexistent players
            balance = self.get_player_account_balance(name)
            pos = self.get_player_current_position(name)

        if balance != 0:                        # Ignore players that have lost
            pos += spaces                       # Perform initial move

            if pos > board_size - 1:            # If end of board passed, loop to
                pos -= board_size               # start of board and payout from GO

                payout = self._board[0].get_payout()
                player.update_balance(payout)

            player.set_pos(pos)                 # Update position

            if pos != 0:                        # Skip rent check on GO
                prop = self.get_space(pos)
                owner = prop.get_owner()

                if owner is not None:           # Skip rent check on space without owner
                    rent = prop.get_rent()
                    player.update_balance(-rent)    # Charge player
                    balance = player.get_balance()
                    owner.update_balance(rent)      # Pay owner

                if balance == 0:                    # Check for player loss
                    for prop in self._board[1:]:
                        owner = prop.get_owner()

                        if owner == player:         # Relinquish losing player's properties
                            prop.set_owner(None)

    def check_game_over(self):
        """
        Checks all player balances. If only 1 player has a balance greater than 0, that
        player is the winner.
        :return: string representing winning player's name (empty string if game is not over)
        """
        winner = ""
        player_count = 0

        for player in self._players:
            name = player.get_name()
            balance = self.get_player_account_balance(name)

            if balance > 0:
                winner = name
                player_count += 1

                if player_count > 1:        # Return "" if more than one active
                    return ""               # player found

        return winner                       # Return name of only active player

    def print_players(self, index):
        """
        Helper for display method. Creates and returns a string representing
        the players on the space associated with index.
        :param index: int [0..24] representing the index of a space in self._board
        :return: a string representing the names of players
        """
        players = []

        for player in self._players:
            name = player.get_name()
            pos = self.get_player_current_position(name)

            if pos == index:                        # Add any player on space
                players.append(name)

        if len(players) == 0:                       # If no players
            return str(None)

        print_players = ""

        for name in players[:len(players) - 1]:     # Add all but last player to string
            print_players += name + ", "            # with formatting

        print_players += players[len(players) - 1]  # Add last player to string

        return print_players

    def spacer(self, string_list):
        """
        Helper for display. Calculates number of spaces for column alignment.
        :param string_list: a list of strings the size of self._board + 1
        :return: a list of strings containing spaces for formatting
        """
        largest = 0
        str_spaces = []

        for str in string_list:                 # Get length of largest string in column
            if len(str) > largest:
                largest = len(str)

        for str in string_list:                 # Calculate spaces needed for alignment
            spaces = ""
            num_spaces = largest - len(str)

            for count in range(num_spaces):     # Create space string
                spaces += " "

            str_spaces.append(spaces)

        return str_spaces

    def display(self):
        """
        Prints a simple depiction of the current state of the game to the console. Represents
        the board as a vertical line with GO at the top. Data on spaces are separated into
        multiple columns for readability. Does not align columns.
        Column 1: Space names
        Column 2: GO payout and property rents/prices
        Column 3: Owner
        Column 4: Player positions
        After the board display, each player's balance is printed.
        :return: None
        """
        board = self._board
        size = len(board)

        # Do nothing if board has not been created
        if size > 0:
            names = ["Space"]
            values = ["Value"]
            owners = ["Owner"]
            players_present = ["Players"]

            # Create strings from Space data
            for space in board:
                name = space.get_name()
                names.append(name)

                pos = board.index(space)

                if pos == 0:
                    value = f"${space.get_payout()}"
                    owner = "NA"
                else:
                    rent = space.get_rent()
                    price = space.get_price()
                    value = f"${rent}/${price}"
                    owner = space.get_owner()

                    if owner is None:
                        owner = str(owner)
                    else:
                        owner = owner.get_name()

                values.append(value)
                owners.append(owner)

                players = self.print_players(pos)
                players_present.append(players)

            # Create lists of spaces for alignment
            n_spaces = self.spacer(names)
            v_spaces = self.spacer(values)
            o_spaces = self.spacer(owners)
            p_spaces = self.spacer(players_present)

            # Write header and strings for each space
            for index in range(size + 1):
                name = names[index] + n_spaces[index]
                value = values[index] + v_spaces[index]
                owner = owners[index] + o_spaces[index]
                players = players_present[index] + p_spaces[index]

                print(f"[{name}]  [{value}]  [{owner}]  [{players}]")

            # Write Player balances
            print()
            players = self._players

            for player in players:
                name = player.get_name()
                balance = self.get_player_account_balance(name)

                print(f"{name}: ${balance}")
