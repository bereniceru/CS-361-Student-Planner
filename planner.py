def main():
    planner_name = ""
    running = True
    
    # Display title
    print("Student Planner")
    print("~~~~~~~~~~~~~~~~~")
    print("This planner is designed to help students manage academic and personal tasks.")
    print()
    
    # Initial instruction message
    
    print("Students can interact with the planner")
    print("based on the planner app functions.")
    print()
    
    while running:
        # Show commands menu
        print("Planner Commands:")
        print("Type 'create' to create a new schedule item.")
        print("Type 'calendar' to view your schedule in calendar format.")
        print("Type 'Q' or 'quit' to leave.")
        print()
        
        # Get user input
        command = input("[Enter/create/calendar/quit/Q]: ")
        
        # Process commands
        if command == "":
            # Show schedule
            print()
            print("YOUR SCHEDULE:")
            print("Study CS")
            print("Meet study group")
            print("Complete assignment - CS 361")
            print()
            
        elif command == "create":
            # Create schedule
            print()
            print("CREATE A SCHEDULE ITEM:")
            print("This will take approximately 30 seconds to complete.")
            task = input("What is your task? ")
            
            if task:
                date = input("Enter date (MM/DD/YYYY): ")
                time = input("Enter time: ")
                notify = input("Enable notifications? (y/n): ")
                
                if notify.lower() == "y":
                    print("Got it. Notification enabled for this task.")
                else:
                    print("Got it. No notification for this task.")
            else:
                print("Task creation cancelled.")
            print()
            
        elif command == "calendar":
            # Show calendar
            print()
            print("CALENDAR VIEW:")
            print()
            print("Tasks:")
            print("05/06: Study")
            print("05/08: Meet group")
            print("05/10: Complete assignment CS 361")
            print()
            

        elif command.lower() in ["q", "quit"]:
            # Quit confirmation
            print()
            print("Are you sure? Unsaved changes will be lost (y/n)")
            confirm = input()
            if confirm.lower() == "y":
                running = False
            print()
            
        else:
            # Invalid command
            print("Invalid command. Please try again.")
            print()

if __name__ == "__main__":
    main()