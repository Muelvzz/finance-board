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

            amount_list = sum(amount_list)
            st.subheader(f"Total: {amount_list}")

            return figure
        
    def delete_amount(self, get_id):
        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM finance WHERE id = ?", (get_id,))
            conn.commit()

    def view(self):

        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM finance")
            result = cursor.fetchall()
            return result

class Frontend():

    def __init__(self):
        self.current_time = datetime.now().strftime("%m-%d %H:%M")
        
    def run_web(self):
        if "dashboard" not in st.session_state:
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
        if "dashboard" not in st.session_state:
            st.session_state.dashboard = FinanceDashboard()
        graph_clicked = st.button("Show Budget Graph")

        if graph_clicked:
            st.session_state.dashboard.graph()

    def view_amount(self):
        if "dashboard" not in st.session_state:
            st.session_state.dashboard = FinanceDashboard()

        if "view_mode" not in st.session_state:
            st.session_state.view_mode = False

        view_clicked = st.button("View Budget", key="view")

        if view_clicked:
            st.session_state.view_mode = True

        if st.session_state.view_mode:
            amount_entries = st.session_state.dashboard.view()
            if amount_entries:
                for row in amount_entries:
                    id1 = row[0]
                    st.write(row[1])
                    st.write(row[2])
                    delete_clicked = st.button("Delete", key=f"delete_{row[0]}")
                    if delete_clicked:
                        st.session_state.dashboard.delete_amount(id1)


if __name__ == "__main__":
    frontend = Frontend()

    frontend.run_web()
    frontend.show_graph()
    frontend.view_amount()

