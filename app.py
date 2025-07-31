
# import streamlit as st
# import matplotlib.pyplot as plt
# import cohere

# # ✅ Add your Cohere API key
# COHERE_API_KEY = "4Ypi8MREWd6gs0urmzhOiWEZts2hTGEPH3nLhO3j"  # 🔹 Replace with your API key
# co = cohere.Client(COHERE_API_KEY)

# # ---- Existing FACTORS and Functions Here ----
# FACTORS = {
#     "electricity": 0.82,
#     "car": 0.21,
#     "ac_hour": 1.5,
#     "gas": 2.0,
#     "induction": 1.2,
#     "electric": 2.5
# }

# def calculate_emissions(bill, km, ac_hours, cook_type):
#     electricity_kwh = bill / 8
#     electricity_emissions = electricity_kwh * FACTORS["electricity"]
#     travel_emissions = km * FACTORS["car"] * 30
#     ac_emissions = ac_hours * FACTORS["ac_hour"] * 30
#     cook_emissions = 30 * FACTORS.get(cook_type, 2.0)
#     total = electricity_emissions + travel_emissions + ac_emissions + cook_emissions
#     return total, {
#         "Electricity": electricity_emissions,
#         "Travel": travel_emissions,
#         "AC Usage": ac_emissions,
#         "Cooking": cook_emissions
#     }

# def get_badge(emission):
#     if emission < 150:
#         return "Gold", "gold"
#     elif emission < 300:
#         return "Silver", "silver"
#     else:
#         return "Bronze", "bronze"

# # ✅ Function to Get AI Tips from Cohere
# def get_ai_tips(bill, km, ac_hours, cook_type):
#     prompt = f"""
#     Suggest 3 personalized and practical tips to reduce carbon footprint for a user with:
#     - Monthly electricity bill ₹{bill}
#     - Travels {km} km per day
#     - Uses AC {ac_hours} hours/day
#     - Cooking type: {cook_type}
#     Tips should be short, practical, and eco-friendly.
#     """

#     response = co.chat(
#         model="command-r",
#         message=prompt  # ✅ old API uses 'message'
#     )

#     text = response.text  # ✅ old API returns full text here

#     # Split into list of tips
#     return [tip.strip(" -•") for tip in text.split("\n") if tip.strip()]


# # ---- MAIN APP ----
# st.set_page_config(page_title="⚡ AI Smart Energy Advisor", page_icon="⚡", layout="wide")
# st.title("⚡ AI Smart Energy Advisor")
# st.caption("🌍 Calculate your carbon footprint & get AI-powered tips")

# with st.form("energy_form"):
#     bill = st.slider("💡 Monthly Electricity Bill (₹)", 100, 5000, 1500)
#     km = st.slider("🚗 Daily Travel Distance (km)", 0, 100, 10)
#     ac_hours = st.slider("❄️ Daily AC Usage (hours)", 0, 24, 4)
#     cook_type = st.selectbox("🍳 Cooking Type", ["gas", "induction", "electric"])
#     submitted = st.form_submit_button("🚀 Calculate My Footprint")

# if submitted:
#     total, breakdown = calculate_emissions(bill, km, ac_hours, cook_type)

#     st.success(f"🌍 Your Monthly CO₂ Emission: **{total:.2f} kg**")
#     badge_text, badge_class = get_badge(total)
#     st.info(f"🏅 **{badge_text} Saver**")

#     # Pie Chart
#     fig, ax = plt.subplots(figsize=(5, 5))
#     ax.pie(breakdown.values(), labels=breakdown.keys(), autopct="%1.1f%%")
#     st.pyplot(fig)

#     # AI Energy Tips
#     st.subheader("🤖 AI-Powered Smart Energy Tips")
#     with st.spinner("Generating AI tips..."):
#         tips = get_ai_tips(bill, km, ac_hours, cook_type)
#         for tip in tips:
#             st.markdown(f"✅ {tip}")
#     st.success("✨ Tips generated successfully!")






import streamlit as st
import matplotlib.pyplot as plt
import cohere

# ✅ Cohere API Key
COHERE_API_KEY = "4Ypi8MREWd6gs0urmzhOiWEZts2hTGEPH3nLhO3j"  # Replace with your API key
co = cohere.Client(COHERE_API_KEY)

FACTORS = {
    "electricity": 0.82,
    "car": 0.21,
    "ac_hour": 1.5,
    "gas": 2.0,
    "induction": 1.2,
    "electric": 2.5
}

def calculate_emissions(bill, km, ac_hours, cook_type):
    electricity_kwh = bill / 8
    electricity_emissions = electricity_kwh * FACTORS["electricity"]
    travel_emissions = km * FACTORS["car"] * 30
    ac_emissions = ac_hours * FACTORS["ac_hour"] * 30
    cook_emissions = 30 * FACTORS.get(cook_type, 2.0)
    total = electricity_emissions + travel_emissions + ac_emissions + cook_emissions
    return total, {
        "Electricity": electricity_emissions,
        "Travel": travel_emissions,
        "AC Usage": ac_emissions,
        "Cooking": cook_emissions
    }

def get_badge(emission):
    if emission < 150:
        return "Gold", "#FFD700"
    elif emission < 300:
        return "Silver", "#C0C0C0"
    else:
        return "Bronze", "#CD7F32"

def get_ai_tips(bill, km, ac_hours, cook_type):
    prompt = f"""
    Suggest 3 personalized and practical tips to reduce carbon footprint for a user with:
    - Monthly electricity bill ₹{bill}
    - Travels {km} km per day
    - Uses AC {ac_hours} hours/day
    - Cooking type: {cook_type}
    Tips should be short, practical, and eco-friendly.
    """

    response = co.chat(model="command-r", message=prompt)
    text = response.text
    return [tip.strip(" -•") for tip in text.split("\n") if tip.strip()]

st.set_page_config(page_title="🌱 Smart Energy Advisor", page_icon="🌱", layout="wide")

# 🌍 HERO SECTION
st.markdown("""
    <div style="text-align:center; padding:60px; background:linear-gradient(135deg,#a8e063,#56ab2f); color:white; border-radius:20px;">
        <h1 style="font-size:50px;">🌍 Join the Fight Against Climate Change</h1>
        <p style="font-size:20px; max-width:700px; margin:auto;">
            Discover your carbon footprint and get AI-powered tips to make your lifestyle more sustainable. 
            Together, let's build a greener future! 💚
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""<br><br><h2 style='text-align:center;'>👇 Calculate Your Impact</h2>""", unsafe_allow_html=True)

# # ---- MAIN APP ----
st.set_page_config(page_title="⚡ AI Smart Energy Advisor", page_icon="⚡", layout="wide")
st.title("⚡ AI Smart Energy Advisor")
st.caption("🌍 Calculate your carbon footprint & get AI-powered tips")

with st.form("energy_form"):
    bill = st.slider("💡 Monthly Electricity Bill (₹)", 100, 5000, 1500)
    km = st.slider("🚗 Daily Travel Distance (km)", 0, 100, 10)
    ac_hours = st.slider("❄️ Daily AC Usage (hours)", 0, 24, 4)
    cook_type = st.selectbox("🍳 Cooking Type", ["gas", "induction", "electric"])
    submitted = st.form_submit_button("🚀 Calculate My Footprint")

if submitted:
    total, breakdown = calculate_emissions(bill, km, ac_hours, cook_type)

    st.success(f"🌍 Your Monthly CO₂ Emission: **{total:.2f} kg**")
    badge_text, badge_class = get_badge(total)
    st.info(f"🏅 **{badge_text} Saver**")

    # Pie Chart
    fig, ax = plt.subplots(figsize=(1.5, 1.5))
    ax.pie(breakdown.values(), labels=breakdown.keys(), autopct="%1.1f%%",textprops={'fontsize': 6})
    st.pyplot(fig)

    # AI Energy Tips
    st.subheader("🤖 AI-Powered Smart Energy Tips")
    with st.spinner("Generating AI tips..."):
        tips = get_ai_tips(bill, km, ac_hours, cook_type)
        for tip in tips:
            st.markdown(f"✅ {tip}")
    st.success("✨ Tips generated successfully!")

    # EXTRA FEATURES
    st.markdown("""<br><h3>🌟 More Ways to Make a Difference</h3>""", unsafe_allow_html=True)
    st.info("♻️ Try carpooling, switching to LEDs, and reducing single-use plastics!")
    st.info("🌿 Plant a tree for every 100 kg CO₂ you save!")
    st.info("⚡ Track your monthly footprint trends with our upcoming feature!")
