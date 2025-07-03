import streamlit as st
import sqlite3
from datetime import datetime
import plotly.express as px

class FinanceDashboard():
    def __init__(self):
        pass

    def add(self, get_date, get_amount):
        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO finance (date, amount) VALUES (?, ?)", (get_date, get_amount))
            conn.commit()

    def graph(self):
        
        date_list = []
        amount_list = []

        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT date, amount FROM finance")
            result = cursor.fetchall()

            for row in result:
                date_list.append(row[0])
                amount_list.append(row[1])

            figure = px.line(x=date_list, y=amount_list, labels={"x" : "Dates", "y" : "Scores"})
            st.plotly_chart(figure)

            return figure
    

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

    def show_graph(self):
        st.session_state.dashboard = FinanceDashboard()
        graph_clicked = st.button("Show Budget Graph")

        if graph_clicked:
            st.session_state.dashboard.graph()

if __name__ == "__main__":
    frontend = Frontend()
    
    frontend.run_web()
    frontend.show_graph()

