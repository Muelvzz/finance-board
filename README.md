This is a simple web-based finance tracker built with **Streamlit**, **SQLite**, and **Plotly**. This is my second project made
using streamlit for handlign frontend interfaces while sqlite for the database management.
---

## Features
  **Add Entry**: Input a specific amount and log it with a timestamp.
  **View Graph**: Plot a line graph showing your budget or expenses over time using Plotly.
  **View Records**: Display all saved financial entries with corresponding dates and amounts.
  **Delete Entry**: Remove a specific entry by clicking the delete button next to each record.
  **Local Storage**: Stores all data locally in a lightweight SQLite database (`database.db`).

Make sure you have the required libraries installed:
  streamlit
  plotly

Then simply run the app using:
  streamlit run your_file_name.py

## Example Input/Output (Console Summary)
* **Input**:
  * Amount: `1000`
  * Action: Click “Add” → Entry is saved with timestamp.

* **Output**:
  * Success message: `✅ Successfully Added`
  * Graph showing the increase of total budget over time.
  * Listed entries with a “Delete” button beside each.
  * Total budget displayed below the graph.
 
    ![image](https://github.com/user-attachments/assets/554b2f4b-97b2-4cab-ac54-b257f32a534c)
    ![image](https://github.com/user-attachments/assets/c5992d67-2265-415d-8659-0098050a69d9)
    ![image](https://github.com/user-attachments/assets/d591cf44-59bb-420d-b078-3e587b8bd393)

## Future Improvements
  **Export to CSV**: Allow users to export their financial records.
  **Dashboard UI Enhancements**: Add tabs, filters, and styled layout.
  **Date Picker**: Allow manual date entry for more flexible backdated logging.
  **Category Tagging**: Tag expenses as "Food", "Transport", etc. for detailed analytics.
