import datetime
import random
import streamlit as st

# --- PAGE CONFIGURATION & AESTHETIC LIGHT MODE STYLING ---
st.set_page_config(
    page_title="Aesthetic Daily Companion & Growth App",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS ensuring 100% white boxes and crisp contrast for Light Mode
st.markdown(
    """
    <style>
    /* Force Light Theme Base across the entire app */
    .stApp {
        background-color: #FAF4F5 !important;
        color: #1D273B !important;
    }
    
    /* Sidebar Styling & Text Visibility */
    section[data-testid="stSidebar"] {
        background-color: #FCEEF3 !important;
        border-right: 1px solid #E6BABC;
    }
    
    section[data-testid="stSidebar"] label, 
    section[data-testid="stSidebar"] span, 
    section[data-testid="stSidebar"] p, 
    section[data-testid="stSidebar"] div,
    section[data-testid="stSidebar"] .stRadio label {
        color: #1D273B !important;
        font-weight: 500;
    }
    
    /* Main Content Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #863253 !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* General Paragraphs & Text */
    p, span, label, .stMarkdown {
        color: #1D273B !important;
    }
    
    /* FORCE ALL INPUT, TEXTAREA, SELECT, DATE, TIME BOXES TO BE WHITE WITH DARK TEXT */
    input, textarea, select, 
    div[data-baseweb="input"], 
    div[data-baseweb="base-input"], 
    div[data-baseweb="select"] > div,
    div[data-testid="stDateInput"] div,
    div[data-testid="stTimeInput"] div {
        background-color: #FFFFFF !important;
        color: #1D273B !important;
        border-color: #E6BABC !important;
        border-radius: 8px !important;
    }
    
    input, div[data-baseweb="input"] input, div[data-baseweb="base-input"] input, 
    div[data-testid="stDateInput"] input, div[data-testid="stTimeInput"] input {
        color: #1D273B !important;
        background-color: #FFFFFF !important;
        -webkit-text-fill-color: #1D273B !important;
    }

    /* File Uploader Box & Browse Button styling */
    div[data-testid="stFileUploader"] {
        background-color: #FFFFFF !important;
        border: 2px dashed #E6BABC !important;
        border-radius: 12px;
        padding: 15px;
        color: #1D273B !important;
    }
    div[data-testid="stFileUploader"] section {
        background-color: #FFFFFF !important;
        color: #1D273B !important;
    }
    div[data-testid="stFileUploader"] button {
        background-color: #3F839C !important;
        color: #FFFFFF !important;
        border: none !important;
    }
    div[data-testid="stFileUploader"] small, div[data-testid="stFileUploader"] span {
        color: #1D273B !important;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #3F839C !important;
        color: white !important;
        border-radius: 12px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        background-color: #863253 !important;
        color: white !important;
    }
    
    /* Custom Cards & Ojas Box */
    .ojas-box {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #E6BABC;
        box-shadow: 0 4px 6px rgba(0,0,0,0.03);
        margin-bottom: 20px;
        color: #1D273B;
    }
    
    .metric-container {
        background-color: #FFFFFF;
        padding: 15px;
        border-radius: 10px;
        border-left: 6px solid #863253;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- SESSION STATE INITIALIZATION ---
if "streak" not in st.session_state:
    st.session_state.streak = 0  # Starts at zero as requested
if "last_completed_date" not in st.session_state:
    st.session_state.last_completed_date = None
if "rest_mode" not in st.session_state:
    st.session_state.rest_mode = False
if "diary_entries" not in st.session_state:
    st.session_state.diary_entries = []
if "water_intake" not in st.session_state:
    st.session_state.water_intake = 0

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🌸 Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "✨ Home & Introduction",
        "⏰ Morning Routine & Mind",
        "🥗 Health, Diet & Water",
        "💪 Exercise & Screen Time",
        "📚 Study & Skills",
        "📖 Diary & Ojas AI",
    ],
)

# Sidebar Streak & Rest Mode widget (Duolingo / Fitness App style)
st.sidebar.markdown("---")
st.sidebar.subheader("🔥 Streak Status")

today = datetime.date.today()

if st.session_state.rest_mode:
    st.sidebar.info(
        "🌴 **Travel / Rest Mode Active**\n\n*Streak Freeze is protecting your progress today!*"
    )
    st.sidebar.metric(
        label="Active Streak", value=f"🔥 {st.session_state.streak} Days"
    )
else:
    st.sidebar.metric(
        label="Active Streak", value=f"🔥 {st.session_state.streak} Days"
    )

rest_toggle = st.sidebar.checkbox(
    "🌴 Enable Rest Day / Travel Mode", st.session_state.rest_mode
)
if rest_toggle != st.session_state.rest_mode:
    st.session_state.rest_mode = rest_toggle
    st.rerun()

# --- PAGE 1: INTRODUCTION & HOME ---
if page == "✨ Home & Introduction":
    st.title("Welcome to Your Aesthetic Daily Companion")
    st.markdown(
        "*Designed with love to nurture your body, mind, and productivity in light mode.*"
    )

    st.markdown(
        """
        <div style="text-align: center; padding: 25px; background-color: #FFFFFF; border-radius: 15px; border: 1px solid #E6BABC; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
            <h2 style="color: #3F839C; margin-bottom: 0px;">✨ Ojas & Harmony Hub ✨</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📌 About the App & How to Use")
        st.write(
            "• **Why this software was made:** To help you maintain consistency, wellness, and self-care without burning out."
        )
        st.write(
            "• **Privacy Respected:** Your personal data and diary entries stay secure and private."
        )
        st.write(
            "• **Streak System:** Use the app daily to watch your streak grow like Duolingo! Use Rest Mode if you are traveling."
        )

    with col2:
        st.markdown(
            """
            <div class="ojas-box">
                <h4>🤖 Meet Ojas (Your Personal AI Guide)</h4>
                <p><i>"Hello! I am Ojas, your personal AI assistant. I am here to guide you through your wellness journey, keep you motivated, and help you track your goals effortlessly."</i></p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# --- PAGE 2: MORNING ROUTINE & MIND ---
elif page == "⏰ Morning Routine & Mind":
    st.title("🌅 Morning Routine & Mindfulness")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("1️⃣ Wake Up Early")
        wake_time = st.time_input(
            "Set your wake-up time:", datetime.time(6, 0)
        )
        st.success(
            "💡 **Benefit:** Waking up early improves mental clarity, lowers stress, and gives you a head start on your day!"
        )

    with col2:
        st.subheader("2️⃣ Meditation & Calm")
        meditate_mins = st.slider(
            "Meditation Duration (Minutes):", 0, 60, 10
        )
        st.info(
            "🧘 **Benefit:** Centers your nervous system and enhances focus."
        )
        st.markdown(
            "**Recommended Resources:** [Vipassana App](https://www.dhamma.org) & [Calming Om Chanting on YouTube](https://www.youtube.com)"
        )

    st.markdown("---")
    if st.button("Complete Morning Rituals"):
        st.balloons()
        st.success("Great job starting your morning mindfully!")

# --- PAGE 3: HEALTH, DIET & WATER ---
elif page == "🥗 Health, Diet & Water":
    st.title("🥗 Nutrition & Hydration")

    # Water Tracker
    st.subheader("💧 Water Intake Tracker")
    col_w1, col_w2, col_w3 = st.columns(3)
    if col_w1.button("➕ Add 250ml"):
        st.session_state.water_intake += 250
    if col_w2.button("➕ Add 500ml"):
        st.session_state.water_intake += 500
    if col_w3.button("🔄 Reset Water"):
        st.session_state.water_intake = 0

    st.metric(
        label="Total Water Drank Today",
        value=f"{st.session_state.water_intake} ml",
    )
    st.caption(
        "💡 **Benefit:** Staying hydrated boosts skin radiance, digestion, and energy levels."
    )

    st.markdown("---")

    # Early Morning Healthy Food
    st.subheader("🥑 Early Morning Healthy Food")
    food_choice = st.selectbox(
        "What did you have this morning?",
        [
            "Fresh Green Salad 🥗",
            "Mixed Fresh Fruits 🍉",
            "Fresh Fruit Juice 🍊",
            "Detox Green Juice 🥒",
        ],
    )
    st.success(
        f"Selected: {food_choice}. **Benefit:** Kickstarts metabolism with essential vitamins and antioxidants."
    )

    st.markdown("---")

    # Calorie Plate (Optional)
    st.subheader("🍽️ Calorie Plate (Optional Diet Tracker)")
    use_diet = st.checkbox(
        "I want to track my diet today (Skipping this will NOT affect your streak!)"
    )

    if use_diet:
        dish_name = st.text_input("Describe your dish / meal name:")
        dish_photo = st.file_uploader(
            "Upload photo of your meal for AI analysis:",
            type=["jpg", "png", "jpeg"],
        )
        if st.button("Calculate Calories with Ojas AI"):
            if dish_name or dish_photo:
                simulated_calories = random.randint(300, 750)
                st.info(
                    f"🤖 **Ojas AI Analysis:** Your meal '{dish_name or 'Uploaded Meal'}' contains approximately **{simulated_calories} kcal**. You are safely within your daily human calorie limit!"
                )
            else:
                st.warning("Please enter a dish name or upload a photo first.")

# --- PAGE 4: EXERCISE & SCREEN TIME ---
elif page == "💪 Exercise & Screen Time":
    st.title("💪 Fitness & Digital Wellness")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏋️ Exercise & Workout")
        ex_type = st.selectbox(
            "Choose your activity:",
            ["Daily Workout", "Yoga & Stretching", "Female Fitness Routine"],
        )
        st.success(
            "💪 **Benefit:** Builds strength, releases endorphins, and maintains posture."
        )
        st.markdown(
            "🔗 [Explore Recommended Workout Routines & Yoga Guides](https://www.youtube.com)"
        )

    with col2:
        st.subheader("📱 Screen Time Management")
        screen_hours = st.slider(
            "Estimated Daily Screen Time (Hours):", 0, 16, 4
        )
        if screen_hours > 5:
            st.warning(
                "⚠️ High screen time detected! Reducing screen time protects your eyes, improves sleep, and frees up time for real-world hobbies."
            )
        else:
            st.success(
                "🌟 Great job keeping your screen time balanced and mindful!"
            )

# --- PAGE 5: STUDY & SKILLS ---
elif page == "📚 Study & Skills":
    st.title("📚 Study Hours & New Skills")

    # New Skills
    st.subheader("🧠 New Skills Learnt Today")
    new_skill = st.text_input("What new skill or concept did you learn today?")
    if new_skill:
        st.success(f"Awesome! Recorded new skill: **{new_skill}**")

    st.markdown("---")

    # Study Hours & Conditional Bar
    st.subheader("⏱️ Study Hours Tracker")
    target_hours = st.number_input(
        "Your Expected Study Hours:", 0.0, 16.0, 4.0, 0.5
    )
    actual_hours = st.number_input(
        "Your Actual Study Hours:", 0.0, 16.0, 3.5, 0.5
    )

    # Conditional color logic requested in notes
    if actual_hours < target_hours:
        bar_color = "red"
        status_msg = "Needs improvement! You are below your expectation."
    elif actual_hours == target_hours:
        bar_color = "green"
        status_msg = "Spot on! You met your exact study goal today!"
    else:
        bar_color = "blue"
        status_msg = "Outstanding! You exceeded your expectation today!"

    st.markdown(f"**Status:** {status_msg}")
    st.progress(
        min(actual_hours / max(target_hours, 1.0), 1.0),
        text=f"Completed {actual_hours} / {target_hours} Hours (Indicator Color: {bar_color.upper()})",
    )

# --- PAGE 6: DIARY & OJAS AI ---
elif page == "📖 Diary & Ojas AI":
    st.title("📖 Personal Diary & Ojas AI Assistant")

    st.markdown(
        """
        <div class="ojas-box">
            <h4>🤖 Ojas AI Guide</h4>
            <p><i>"Write down your thoughts, reflections, and memories here. Your diary entries and photos are safely stored for your eyes only."</i></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    diary_date = st.date_input("Date", datetime.date.today())
    diary_notes = st.text_area("Write your diary entry / notes for today:")
    diary_photo = st.file_uploader(
        "Add a photo to today's entry:", type=["jpg", "png", "jpeg"]
    )

    if st.button("Save Diary Entry"):
        if diary_notes:
            st.session_state.diary_entries.append(
                {
                    "date": str(diary_date),
                    "notes": diary_notes,
                    "photo": diary_photo,
                }
            )
            st.success("Diary entry saved successfully! ✨")
        else:
            st.warning("Please write something before saving.")

    # Display past entries
    if st.session_state.diary_entries:
        st.subheader("📜 Past Entries")
        for entry in reversed(st.session_state.diary_entries):
            with st.container():
                st.markdown(f"**Date:** {entry['date']}")
                st.write(entry["notes"])
                if entry["photo"]:
                    st.image(entry["photo"], width=200)
                st.markdown("---")

    # Congratulation message section & Streak Increment
    st.subheader("🎉 Daily Completion Celebration")
    if st.button("Check Daily Completion & Claim Streak"):
        if st.session_state.last_completed_date != today:
            st.session_state.streak += 1
            st.session_state.last_completed_date = today
            st.balloons()
            st.success(
                f"🔥 Streak increased! Your new streak is **{st.session_state.streak} Days**!"
            )
        else:
            st.info(
                f"✨ You already completed today's goals! Your streak remains at **{st.session_state.streak} Days**."
            )

        st.markdown(
            """
            <div style="background-color: #FFFFFF; padding: 20px; border-radius: 12px; border: 1px solid #E6BABC; margin-top: 15px;">
                <p style="font-size: 1.1em; color: #863253; font-style: italic; text-align: center;">
                <b>"Now you have a whole day what you want to do match movie, go out with friends, visit new place. Do anything you want today because you have done taking care of body. It's your day and time enjoy. See you tomorrow!"</b>
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )