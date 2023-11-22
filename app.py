# core package
import streamlit as st
import pandas as pd

# DB fanctions packages
from db_fxns import *




def main():

    create_food_table()
    create_beverage_table()


    # set the title and header    
    st.title("Questionnaire for food and beverage professionals")
    st.subheader("We would like to express our sincere gratitude for your invaluable contribution and cooperation to the realization of this captivating and sustainable event.")
    st.subheader("The data collected here will be used for greenhouse gas emission calculations.")

    # Question about providing food
    provide_food = st.radio("Q. Do you provide food?", ('Yes', 'No'))

    # Initialize an empty DataFrame
    food_data = pd.DataFrame()

    if provide_food == 'Yes':
        # Expander for food details
        with st.expander("Please provide details about the food you offer:"):
            # Options for type of food
            food_types = ['Meal with chicken', 'Meal with beef', 'Vegitable meal', 'Hot and cold snack', 'Other types of food']

            # Collecting food data
            food_data_list = []
            for food in food_types:
                # Asking for the number of meals for each food type
                num_meals = st.number_input(f"How many meals for '{food}'?", min_value=0, step=1)
                food_data_list.append({'Type of Food': food, 'Number of Meals': num_meals})

            # Convert list of dictionaries to DataFrame
            food_data = pd.DataFrame(food_data_list)




    # Question about providing beverages
    provide_beverage = st.radio("Q. Do you provide beverages?", ('Yes', 'No'))
    # Initialize an empty DataFrame for beverage data
    beverage_data = pd.DataFrame()

    if provide_beverage == 'Yes':
        # Expander for beverage details
        with st.expander("Please provide details about the beverages you offer:"):
            # Options for type of beverage
            beverage_options = ['Alcoholic', 'Non-alcoholic']

            # Collecting beverage data
            beverage_data_list = []
            for beverage in beverage_options:
                # Asking for the quantity of each beverage type
                volume = st.number_input(f"How many litres of '{beverage}' beverages?", min_value=0, step=1)

                # Method of measurement
                measurement_method = st.radio(f"Measurement method for '{beverage}':", ('Volume (specification) x Number of bottles', 'Weight difference before and after the event'))
                
                beverage_data_list.append({'Type of Beverage': beverage, 'Volume (litres)': volume, 'Measurement Method': measurement_method})

            # Convert list of dictionaries to DataFrame
            beverage_data = pd.DataFrame(beverage_data_list)

    # Button to confirm beverage data
    if st.button('Confirm the input data details'):
        # Display the data frame to user for confirmation
        st.write("Your iput data provision details:")
        st.dataframe(food_data)
        st.dataframe(beverage_data)
        st.warning("If the information you entered is correct, please push the submit button")


    # Ask for the company name
    company = st.text_input("Please enter your company name:")


    # Submit button
    if st.button('Submit'):
        
        # # set the data to add them to the database        
        # food_type = food_data["Type of Food"]
        # food_amount = food_data["Number of Meals"]
        # # company has been set above
        # beverage_type = beverage_data["Type of Beverage"]
        # beverage_amount = beverage_data["Volume (litres)"]
        # method = beverage_data["Measurement Method"]
    
    
        # Loop through each row in the food data DataFrame
        for idx, row in food_data.iterrows():
            add_food_data(row['Type of Food'], row['Number of Meals'], company)

        # Loop through each row in the beverage data DataFrame
        for idx, row in beverage_data.iterrows():
            add_beverage_data(row['Type of Beverage'], row['Volume (litres)'], row['Measurement Method'], company)

        
        
        
        
        # Thank you message after submission
        st.success("Your response has been submitted. Thank you for your cooperation.")

if __name__ == '__main__':
    main() 



