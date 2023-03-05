"""

CHARACTER PALETTE
You can copy the necessary characters for drawing cards from here.

Horizontal lines:  │

Vertical lines:  ─

Corners of a card:  ┐  ┌  ┘  └

Intersections of two cards:

    if card1_height == card2_height:  ┬  ┴

    if card1_height < card2_height:  ┤

    if card1_height > card2_height:  ├

"""

print("This program will draw two cards next to each other.")
print("─" * 20)

print("Texts must not be empty.")
card1_text = input("Text of first card: ")
card2_text = input("Text of second card: ")
print("─" * 20)

##############################
# INSERT YOUR CODE HERE
# Assign proper values to card1_min_width and card2_min_width here.
# They are length of the corresponding text + 2.
# For example, if card1_text contains 5 characters, then card1_min_width must be 7.
card1_min_width = len(card1_text) + 2
card2_min_width = len(card2_text) + 2
# DO NOT EDIT THE CODE UNDER THIS LINE.
##############################

print("Width of first card must be at least " + str(card1_min_width) + ".")
card1_width = int(input("Width of first card: "))
print("Width of second card must be at least " + str(card2_min_width) + ".")
card2_width = int(input("Width of second card: "))
print("─" * 20)

print("Heights must be odd and at least 3.")
card1_height = int(input("Height of first card: "))
card2_height = int(input("Height of second card: "))
print("─" * 20)


##############################
# INSERT YOUR CODE HERE
# Assign the proper value to is_invalid.
# Check if there is at least one problem in the inputs.
# I added two conditions, add more to the line below.

# -----------------------------------------------------------
# if card1_text is empty or
# card2_text is empty or
# card1_width is less than card1_min_width or
# card2_width is less than card2_min_width or
# card1_height is less than 3 or
# card2_height is less than 3 or
# card1_height is even or
# card2_height is even
#
# -> inputs are invalid --------------------------------------
is_invalid = len(card1_text) == 0 or len(
    card2_text) == 0 or card1_width < card1_min_width or card2_width < card2_min_width or card1_height < 3 or card2_height < 3 or card1_height % 2 == 0 or card2_height % 2 == 0
# DO NOT EDIT THE CODE UNDER THIS LINE.
##############################

if is_invalid:
    print("ERROR: Invalid inputs.")

else:

    if card1_height == card2_height:

        ##############################
        # INSERT YOUR CODE HERE
        # Case 1
        # You can add as many new lines as you need.

        # Top of the cards
        print("┌" + (card1_width - 2) * "─" +
              "┬" + (card2_width - 2) * "─" + "┐")

        # Middle of the cards before the texts
        if card1_height == 3:
            pass
        else:
            print(int(((card1_height + 1) / 2) - 3) * ("│" + (card1_width - 2) * " " +
                  "│" + (card2_width - 2) * " " + "│\n") + ("│" + (card1_width - 2) * " " +
                  "│" + (card2_width - 2) * " " + "│"))

        # Text
        print("│" + int((card1_width - 2 - len(card1_text)) / 2) * " " +
              card1_text + (card1_width - 2 - len(card1_text) - int((card1_width - 2 - len(card1_text)) / 2)) * " " + "│" +
              int((card2_width - 2 - len(card2_text)) / 2) * " " +
              card2_text + (card2_width - 2 - len(card2_text) - int((card2_width - 2 - len(card2_text)) / 2)) * " " + "│")

        # Middle of the cards after the texts
        if card1_height == 3:
            pass
        else:
            print(int(((card1_height + 1) / 2) - 3) * ("│" + (card1_width - 2) * " " +
                  "│" + (card2_width - 2) * " " + "│\n") + ("│" + (card1_width - 2) * " " +
                  "│" + (card2_width - 2) * " " + "│")
                  )

        # Bottom of the cards
        print("└" + (card1_width - 2) * "─" +
              "┴" + (card2_width - 2) * "─" + "┘")

        pass

        # DO NOT EDIT THE CODE UNDER THIS LINE.
        ##############################

    elif card1_height > card2_height:

        ##############################
        # INSERT YOUR CODE HERE
        # Case 2
        # You can add as many new lines as you need.

        # Top of the cards:
        print("┌" + (card1_width - 2) * "─" + "┐")

        # Middle of the card1 before card2 start:
        if card1_height - card2_height == 2:
            pass
        else:
            print((int((card1_height - card2_height) / 2) - 2) * ("│" +
                  (card1_width - 2) * " " + "│\n") + ("│" + (card1_width - 2) * " " + "│"))

        # Card2 start:
        print("│" + (card1_width - 2) * " " +
              "├" + (card2_width - 2) * "─" + "┐")

        # Middle of the cards before the texts:
        if card2_height == 3:
            pass
        else:
            print((int((card2_height - 3) / 2) - 1) * ("│" + (card1_width - 2) * " " +
                  "│" + (card2_width - 2) * " " + "│\n") + ("│" + (card1_width - 2) * " " +
                  "│" + (card2_width - 2) * " " + "│"))

        # Texts
        print("│" + int((card1_width - 2 - len(card1_text)) / 2) * " " +
              card1_text + (card1_width - 2 - len(card1_text) - int((card1_width - 2 - len(card1_text)) / 2)) * " " +
              "│" + int((card2_width - 2 - len(card2_text)) / 2) * " " + card2_text +
              (card2_width - 2 - len(card2_text) - int((card2_width - 2 - len(card2_text)) / 2)) * " " + "│")

        # Middle of the cards after the texts:
        if card2_height == 3:
            pass
        else:
            print((int((card2_height - 3) / 2) - 1) * ("│" + (card1_width - 2) * " " +
                  "│" + (card2_width - 2) * " " + "│\n") + ("│" + (card1_width - 2) * " " +
                  "│" + (card2_width - 2) * " " + "│"))

        # End of Card2:
        print("│" + (card1_width - 2) * " " +
              "├" + (card2_width - 2) * "─" + "┘")

        # Middle of the card1 after the end of card2:
        if card1_height - card2_height == 2:
            pass
        else:
            print((int((card1_height - card2_height) / 2) - 2) * ("│" +
                  (card1_width - 2) * " " + "│\n") + ("│" + (card1_width - 2) * " " + "│"))

        # End of card1:
        print("└" + (card1_width - 2) * "─" + "┘")

        pass

        # DO NOT EDIT THE CODE UNDER THIS LINE.
        ##############################

    else:

        ##############################
        # INSERT YOUR CODE HERE
        # Case 3
        # You can add as many new lines as you need.

        # Top of the cards:
        print((card1_width - 1) * " " + "┌" + (card2_width - 2) * "─" + "┐")

        # Middle of the card2 before card1 start:
        if card2_height - card1_height == 2:
            pass
        else:
            print((int((card2_height - card1_height) / 2) - 2) * ((card1_width - 1) * " " + "│" +
                  (card2_width - 2) * " " + "│\n") + ((card1_width - 1) * " " + "│" + (card2_width - 2) * " " + "│"))

        # Card2 start:
        print("┌" + (card1_width - 2) * "─" + "┤" + (card2_width - 2) * " " +
              "│")

        # Middle of the cards before the texts:
        if card1_height == 3:
            pass
        else:
            print((int((card1_height - 3) / 2) - 1) * ("│" + (card1_width - 2) * " " +
                  "│" + (card2_width - 2) * " " + "│\n") + ("│" + (card1_width - 2) * " " +
                  "│" + (card2_width - 2) * " " + "│"))

        # Texts
        print("│" + int((card1_width - 2 - len(card1_text)) / 2) * " " +
              card1_text + (card1_width - 2 - len(card1_text) - int((card1_width - 2 - len(card1_text)) / 2)) * " " +
              "│" + int((card2_width - 2 - len(card2_text)) / 2) * " " + card2_text +
              (card2_width - 2 - len(card2_text) - int((card2_width - 2 - len(card2_text)) / 2)) * " " + "│")

        # Middle of the cards after the texts:
        if card1_height == 3:
            pass
        else:
            print((int((card1_height - 3) / 2) - 1) * ("│" + (card1_width - 2) * " " +
                  "│" + (card2_width - 2) * " " + "│\n") + ("│" + (card1_width - 2) * " " +
                  "│" + (card2_width - 2) * " " + "│"))

        # Card1 end:
        print("└" + (card1_width - 2) * "─" +
              "┤" + (card2_width - 2) * " " + "│")

        # Middle of the card1 after the End of Card2:
        if card2_height - card1_height == 2:
            pass
        else:
            print((int((card2_height - card1_height) / 2) - 2) * (((card1_width - 1) * " ") + "│" +
                  (card2_width - 2) * " " + "│\n") + (((card1_width - 1) * " ") + "│" + (card2_width - 2) * " " + "│"))

        # End of the card1:
        print(((card1_width - 1) * " ") + "└" + (card2_width - 2) * "─" + "┘")

        pass

        # DO NOT EDIT THE CODE UNDER THIS LINE.
        ##############################
