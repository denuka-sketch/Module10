def main():
    # The Todo class
    from todo import Todo
    todo = Todo()
    todo.addTask("Make the bed")
    todo.addTask("Do homework")
    todo.addTask("Check email")
    print(repr(todo))

    # The SchoolTask class
    from schooltasks import SchoolTasks
    st = SchoolTasks()
    st.addTask("11/4/2025", "Write Essay")
    st.addTask("11/04/2025", "Read Chapter 5")
    st.addTask("11/07/2025", "Complete Online Exam")
    print(repr(st))
    print(st)

    #The TaskTracker Class
    from tasktracker import TaskTracker
    track = TaskTracker("Workout for the day")
    track.addTask("11/01/2025", "Deadlift")
    track.addTask("11/01/2025", "Run 3 miles", "11/01/2025")
    track.addTask("11/05/2025", "Swim 50 Laps")
    track.addTask("11/02/2025", "HIIT Training", "11/02/2025")
    print(repr(track))
    track.removeTask("Deadlift")
    print(repr(track))
    print(str(track))

    # call generate list
    generate_list(todo)
    generate_list(st)
    generate_list(track)




def generate_list(t):
    from todo import Todo
    if not isinstance(t, Todo):
        print("Not Todo List")
        return NotImplemented
    print("Generate List Function")
    print(t)

main()