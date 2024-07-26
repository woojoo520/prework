import sqlite3;

def connect_db():
    return sqlite3.connect('assignment.db')

def search_students(name):
    conn = connect_db()
    cursor = conn.cursor() 
    
    # perform searching
    # query_str = 'SELECT * FROM students' 
    # cursor.execute(query_str, ())
    query_str = 'SELECT name, marks FROM students WHERE name LIKE ?' 
    cursor.execute(query_str, (f"%{name}%",))
    res = cursor.fetchall()
    
    conn.close() 
    return res

def print_students(res):
    if not res or len(res) == 0:
        print("No matching records found")
        return
    
    total_marks = 0
    print("Matching records:")
    for name, marks in res: 
        print(f"Name: {name}, Marks: {marks}")
        total_marks += marks
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {total_marks / len(res)}")
    
def main():
    while True: 
        query_name_prefix = input("Please enter a search string: ")
        query_name_prefix = query_name_prefix.strip()
        if not query_name_prefix: 
            continue
        else: 
            res = search_students(query_name_prefix)
            print_students(res)
            break 

if __name__ == '__main__':
    main()