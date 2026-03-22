import streamlit as st

st.title("📦 Inventory Management System")

# Initialize session state for inventory
if 'inventory' not in st.session_state:
    st.session_state.inventory = []

# Sidebar for adding items
st.sidebar.header("Add New Item")
item_name = st.sidebar.text_input("Item Name")
item_qty = st.sidebar.number_input("Quantity", min_value=1)
item_price = st.sidebar.number_input("Price per Unit", min_value=0.0)

if st.sidebar.button("Add to Inventory"):
    st.session_state.inventory.append({"Name": item_name, "Qty": item_qty, "Price": item_price})
    st.sidebar.success(f"Added {item_name}!")

# Main Area: Display Inventory
st.subheader("Current Stock")
if st.session_state.inventory:
    st.table(st.session_state.inventory)
    
    # Billing Calculation
    total = sum(item['Qty'] * item['Price'] for item in st.session_state.inventory)
    st.write(f"### Total Inventory Value: ${total:,.2f}")
else:
    st.info("Your inventory is currently empty.")
