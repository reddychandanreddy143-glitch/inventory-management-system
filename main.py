import streamlit as st

st.set_page_config(page_title="Inventory Manager", page_icon="📦")

st.title("📦 Inventory Management System")

# Initialize session state for inventory if it doesn't exist
if 'inventory' not in st.session_state:
    st.session_state.inventory = []

# --- SIDEBAR: ADD ITEMS ---
st.sidebar.header("➕ Add New Item")
with st.sidebar.form("add_form", clear_on_submit=True):
    name = st.text_input("Item Name")
    qty = st.number_input("Quantity", min_value=1, step=1)
    price = st.number_input("Price per Unit", min_value=0.0, step=0.5)
    submit = st.form_submit_button("Add to Inventory")

if submit and name:
    st.session_state.inventory.append({"Name": name, "Qty": qty, "Price": price})
    st.sidebar.success(f"Added {name}!")

# --- MAIN AREA: DISPLAY & MANAGE ---
st.subheader("📋 Current Stock")

if st.session_state.inventory:
    # Display the inventory table
    st.table(st.session_state.inventory)
    
    # Calculation
    total_val = sum(item['Qty'] * item['Price'] for item in st.session_state.inventory)
    st.metric("Total Inventory Value", f"${total_val:,.2f}")

    # --- DELETE SECTION ---
    st.markdown("---")
    st.subheader("🗑️ Remove Items")
    
    # Create a list of names for the dropdown
    item_names = [f"{i}: {item['Name']}" for i, item in enumerate(st.session_state.inventory)]
    selected_item = st.selectbox("Select item to delete:", item_names)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Delete Selected Item", type="primary"):
            index = int(selected_item.split(":")[0])
            removed = st.session_state.inventory.pop(index)
            st.toast(f"Removed {removed['Name']}")
            st.rerun()

    with col2:
        if st.button("Clear All Inventory"):
            st.session_state.inventory = []
            st.rerun()
else:
    st.info("Your inventory is currently empty. Use the sidebar to add items!")
