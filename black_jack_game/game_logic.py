from deck import Deck
from hand import Hand
from chips import Chips


def place_bet(chips):
    while True:
        try:
            print("Please place your bet to start the game. ")
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry, a bet must be an integer!")
            continue
        else:
            if chips.bet > chips.total:
                print(f"Sorry, your bet cant exceed: {chips.total}")
            else:
                break


def display_some_cards(player_hand, dealer_hand):
    print(f"\nDealer's Card: [X, {dealer_hand.current_cards[1]}]")
    print(f"\nPlayer's Card: ", *player_hand.current_cards, sep=', ')
    print()


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, player_hand, dealer_hand):
    global game_playing
    while True:
        try:
            hit_stand = input("Do you want to hit or stand? Please enter h for hit or s for stand. ")
        except:
            print("Please enter valid input")
            continue
        else:
            if hit_stand.lower() == 'h':
                hit(deck, player_hand)
                display_some_cards(player_hand, dealer_hand)
                continue
            elif hit_stand.lower() == 's':
                print("Dealer's Turn to Play!")
                game_playing = False
                break
            else:
                print("Sorry, please try again!")
                continue


def display_all_cards(player_hand, dealer_hand):
    print(f"\nDealer's Card: ", *dealer_hand.current_cards, sep=', ')
    print(f"\nPlayer's Card: ", *player_hand.current_cards, sep=', ')
    print()


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


game_playing = True

while True:
    deck = Deck()
    deck.shuffle_cards()

    player_hand = Hand("Player One")
    dealer_hand = Hand("Dealer")

    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    chips = Chips()  # default chips available is set to 100

    place_bet(chips)

    display_some_cards(player_hand, dealer_hand)

    while game_playing:
        hit_or_stand(deck, player_hand, dealer_hand)

        display_some_cards(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

            # Show all cards
        display_all_cards(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, chips)

        else:
            push(player_hand, dealer_hand)

    print("\nPlayer's winnings stand at", chips.total)

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        game_playing = True
        continue
    else:
        print("Thanks for playing!")
        break
