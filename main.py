import streamlit as st
import sqlite3
from datetime import datetime

class FinanceDashboard():
    def __init__(self):
        pass

    def add(self, get_date, get_amount):
        with sqlite3.connect("database.db") as connection:
            conn = connection.cursor()
            conn.execute("INSERT INTO finance (date, amount) VALUES (?, ?)", (get_date, get_amount))
            connection.commit()

    def graph(self):
        with sqlite3.connect("database.db") as connection:
            conn = connection.cursor()
            conn.execute("SELECT amount FROM finance")
        date = 1
        amount = 1
    

class Frontend():

    def __init__(self):
        self.current_time = datetime.now().strftime("%m-%d %H:%M")
        
    def run_web(self):

        st.session_state.dashboard = FinanceDashboard()

        st.markdown("<div style='text-align: center;'>"
                    "<h1>Finance Dashboard</h1>"
                    "</div>", unsafe_allow_html=True)
        
        money = st.number_input("Enter the amount:")

        add_money = st.button("Add")
        if add_money:
            st.session_state.dashboard.add(self.current_time, money)
            st.success("Successfully Added")

if __name__ == "__main__":
    frontend = Frontend()
    frontend.run_web()

