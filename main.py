import sqlite3

# This will organize the Tickets into a simple table #
conn = sqlite3.connect("tickets.db") 
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    status TEXT
)
""")

conn.commit()

# Program to Create Tickets that will later be saved and be viewed. #
def create_ticket():
    title = input("Enter ticket title: ")
    ticket_id = title
    description = input("Enter description of what the problem is in 100 words or less: ")

    cursor.execute(
        "INSERT INTO tickets (title, description, status) VALUES (?, ?, ?)",
        (title, description, "Open")

    )

    conn.commit()
    print ("Ticket created.")

def view_tickets():
    cursor.execute("SELECT * FROM tickets")
    tickets = cursor.fetchall()

    for ticket in tickets:
        print(ticket)

def resolve_ticket():
    ticket_id = input("Enter ticket ID to resolve: ")

    cursor.execute(
        "UPDATE tickets SET status = ? WHERE id = ?",
        ("Resolved", ticket_id)
    )

    conn.commit()
    print("Ticket resolved.")


# This is what the user will see in the console #
# they will choose between options 1 - 4 and will get different prompts based on what they pick #
while True:
    print ("\n1. Create Ticket")
    print ("2. View Tickets")
    print ("3. Resolve Ticket")
    print ("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        create_ticket()
        print ("Your Ticket has been created and will be taken care of as soon as possible!")
        print ("Is there anything else we can help you with?")
    elif choice == "2":
        view_tickets()
        print ("Is there anything else we can help you with?")
    elif choice == "3":
        resolve_ticket()
        print ("Wonderful Job!")
        print ("Is there anything else we can help you with?")
    elif choice == "4":
        print ("Thank you for using our Online Ticketing System - Have a wonderful Day!")
        break            