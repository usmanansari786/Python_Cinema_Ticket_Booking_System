
def display_seats(seats):
  """Display the seating arrangement with clear labels."""
  print("\nSeating Arrangement:")
  print("    " + "   ".join(str(i + 1) for i in range(len(seats[0]))))  # Column headers (1, 2, 3...)
  for index, row in enumerate(seats):
      row_label = chr(ord('A') + index)  # Convert index to A, B, C, etc.
      print(f"{row_label} | " + " | ".join(row))  # Row label and seats
      print("   " + "---" + "---".join(["" for _ in row]))  # Separator line
  print()


def select_seats(seats, number_of_tickets):
  """Allow user to select seats."""
  while True:
      selected_seats = input("Select your seats (e.g., A1 B2) separated by spaces: ").strip().upper().split()

      if len(selected_seats) != number_of_tickets:
          print(f"You must select exactly {number_of_tickets} seats.")
          continue

      # Validate seat selection
      valid_selection = True
      for seat in selected_seats:
          row, col = seat[0], int(seat[1]) - 1  # Assuming seats like A1, B2, etc.
          row_index = ord(row) - ord('A')  # Convert letter to corresponding index

          if (row_index < 0 or row_index >= len(seats) or 
                  col < 0 or col >= len(seats[0]) or 
                  seats[row_index][col] == 'X'):
              print(f"Seat {seat} is invalid or already booked!")
              valid_selection = False
              break

      if valid_selection:
          # Mark selected seats as booked
          for seat in selected_seats:
              row, col = seat[0], int(seat[1]) - 1
              row_index = ord(row) - ord('A')
              seats[row_index][col] = 'X'
          return selected_seats
      else:
          print("Please try again.")


def main():
  # Movie data
  movies = ["Avengers", "Spiderman", "The Batman"]
  times = ["10:00am", "1:30pm", "4:00pm", "7:00pm"] 

# Added another showtime
  screens = ["screen 1", "screen 2", "screen 3", "screen 4"]  # Added another screen

  # Seating arrangement for each screen
  seats_per_screen = {f"screen {i + 1}": [['O' for _ in range(5)] for _ in range(5)] for i in range(len(screens))}

  # Ask if the user wants to book a ticket
  book = input("Would you like to book a ticket? (yes or no) \n").strip().lower()

  if book in ["yes", "y"]:
      # Choose movie
      print("\nAvailable movies:")
      for index, movie in enumerate(movies, start=1):
          print(f"{index}. {movie}")

      try:
          movie_choice = int(input("Choose your movie (enter the number): "))
          if 1 <= movie_choice <= len(movies):
              pick_movie = movies[movie_choice - 1]
          else:
              print("Invalid choice, exiting.")
              return
      except ValueError:
          print("Please enter a valid number, exiting.")
          return

      # Choose screening
      print("\nAvailable screens:")
      for index, screen in enumerate(screens, start=1):
          print(f"{index}. {screen}")

      try:
          screen_choice = int(input("Choose your screen (enter the number): "))
          if 1 <= screen_choice <= len(screens):
              pick_screen = screens[screen_choice - 1]
          else:
              print("Invalid choice, exiting.")
              return
      except ValueError:
          print("Please enter a valid number, exiting.")
          return

      # Choose time
      print("\nAvailable showtimes:")
      for index, time in enumerate(times, start=1):
          print(f"{index}. {time}")

      try:
          time_choice = int(input("Choose your time (enter the number): "))
          if 1 <= time_choice <= len(times):
              pick_time = times[time_choice - 1]
          else:
              print("Invalid choice, exiting.")
              return
      except ValueError:
          print("Please enter a valid number, exiting.")
          return

      # Choose number of tickets
      try:
          tickets = int(input("How many tickets would you like to book? "))
          if tickets <= 0:
              print("Invalid number of tickets, exiting.")
              return
      except ValueError:
          print("Please enter a valid number, exiting.")
          return

      # Display available seats
      display_seats(seats_per_screen[pick_screen])

      # Allow user to select seats
      booked_seats = select_seats(seats_per_screen[pick_screen], tickets)

      # Calculate total price
      ticket_price = 10  # Price per ticket
      total_price = tickets * ticket_price

      # Choose payment method
      print("\nPayment methods:")
      payment_methods = ["cash", "card"]
      for index, payment in enumerate(payment_methods, start=1):
          print(f"{index}. {payment.capitalize()}")

      try:
          payment_choice = int(input("Choose payment method (enter the number): "))
          if 1 <= payment_choice <= len(payment_methods):
              pick_payment = payment_methods[payment_choice - 1]
          else:
              print("Invalid payment method, exiting.")
              return
      except ValueError:
          print("Please enter a valid number, exiting.")
          return

      # Summary
      print("\n--- Booking Summary ---")
      print(f"Movie: {pick_movie}")
      print(f"Screen: {pick_screen}")
      print(f"Time: {pick_time}")
      print(f"Number of tickets: {tickets}")
      print(f"Selected seats: {', '.join(booked_seats)}")  # Show selected seats
      print(f"Total price: £{total_price}")  # Display total price
      print(f"Payment method: {pick_payment.capitalize()}")

      # Ask for a review
      review = input("\nWould you like to leave a review? (yes or no) ").strip().lower()
      if review in ['yes', 'y']:
          user_review = input("Please write your review below:\n")
          print("\nThank you for your feedback!")
      else:
          print("\nNo problem! Thank you for your booking!")

      print("Enjoy your movie!")


  else:
      print("Goodbye!")


# Entry point of the script
if __name__ == "__main__":
  main()
