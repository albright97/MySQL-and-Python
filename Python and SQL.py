#!/usr/bin/env python
# coding: utf-8

# In[1]:


conda install -c anaconda mysql-connector-python


# In[3]:


get_ipython().run_line_magic('pip', 'install mysql-connector-python')


# In[9]:


import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0728520105@Winnie."
)
print(mydb)


# In[11]:


import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0728520105@Winnie.",
    database="sq"
)


# In[31]:


# Create a cursor object
mycursor = mydb.cursor()

# Define the SQL statement
create_table_query = """
CREATE TABLE custom (
    name VARCHAR(255),
    address VARCHAR(255)
);
"""


# In[33]:


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0728520105@Winnie.",
    database="sq"
)
mycursor = mydb.cursor()
mycursor.execute("show tables")
for x in mycursor:
    print(x)


# In[35]:


# Fetch all table names
tables = mycursor.fetchall()

# Check if 'custom' table exists
if any(table[0] == 'custom' for table in tables):
    print("Table 'custom' exists in the 'sq' database.")
else:
    print("Table 'custom' does not exist in the 'sq' database.")


# In[37]:


import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0728520105@Winnie.",
    database="sq"
)

# Create a cursor object
mycursor = mydb.cursor()

# Confirm the current database
print("Current database:", mydb.database)

# Execute SQL query to show all tables
mycursor.execute("SHOW FULL TABLES")

# Fetch and print each table name
tables = mycursor.fetchall()
print("Tables in the 'sq' database:")
for table in tables:
    print(table[0])  # Print the table name

# Check specifically for 'custom'
if any(table[0] == 'custom' for table in tables):
    print("Table 'custom' exists in the 'sq' database.")
else:
    print("Table 'custom' does not exist in the 'sq' database.")


# In[39]:


import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0728520105@Winnie.",
    database="sq"
)

# Create a cursor object
mycursor = mydb.cursor()

# Create the 'custom' table
mycursor.execute("""
CREATE TABLE IF NOT EXISTS custom (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255)
)
""")

print("Table 'custom' created successfully in the 'sq' database.")


# In[41]:


# Execute SQL query to show all tables
mycursor.execute("SHOW TABLES")

# Fetch and print each table name
tables = mycursor.fetchall()
print("Tables in the 'sq' database:")
for table in tables:
    print(table[0])  # Print the table name


# In[47]:


# SQL statement with corrected placeholder syntax
sql = "INSERT INTO custom (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")

# Execute the SQL statement
mycursor.execute(sql, val)

# Commit the transaction
mydb.commit()

# Print the number of rows inserted
print(mycursor.rowcount, "record inserted")

# Close the cursor and connection
mycursor.close()
mydb.close()


# In[53]:


import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0728520105@Winnie.",
    database="sq"
)

# Create a cursor object
mycursor = mydb.cursor()

# SQL statement with placeholders
sql = "INSERT INTO custom (name, address) VALUES (%s, %s)"

# List of dummy data
data = [
    ("John Doe", "123 Elm Street"),
    ("Jane Smith", "456 Oak Avenue"),
    ("Alice Johnson", "789 Pine Road"),
    ("Bob Brown", "101 Maple Lane"),
    ("Charlie Davis", "202 Birch Blvd"),
    ("Diana Evans", "303 Cedar St"),
    ("Evan Wilson", "404 Spruce Dr"),
    ("Fiona Miller", "505 Fir Court"),
    ("George Anderson", "606 Redwood Crescent"),
    ("Hannah Lee", "707 Sequoia Way")
]

# Execute the SQL statement for each data entry
mycursor.executemany(sql, data)

# Commit the transaction
mydb.commit()

# Print the number of rows inserted
print(mycursor.rowcount, "records inserted")

# Close the cursor and connection
mycursor.close()
mydb.close()


# In[59]:


import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0728520105@Winnie.",
    database="sq"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute the SELECT query
mycursor.execute("SELECT * FROM custom")

# Fetch all the results
myresult = mycursor.fetchall()

# Print each result
for x in myresult:
    print(x)

# Close the cursor and connection
mycursor.close()
mydb.close()


# In[ ]:




