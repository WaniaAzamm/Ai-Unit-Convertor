import streamlit as st
import time
import pint
import google.generativeai as genai
from dotenv import load_dotenv
import random
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

ureg = pint.UnitRegistry()
ureg.autoconvert_offset_to_baseunit = True  

st.set_page_config(
    page_title="🚀 Convertify AI - Smartest Unit Converter",
    layout="wide",
    initial_sidebar_state="expanded"
)

fun_facts = [
    "1 inch is exactly 2.54 centimeters!",
    "A gallon of water weighs about 8.34 pounds!",
    "A nautical mile is longer than a land mile (1.15 times).",
    "A kilogram was originally defined by a block of platinum-iridium!",
    "Light travels approximately 186,282 miles per second!",
    "The speed of sound is about 343 meters per second at sea level!",
    "One metric ton of water is exactly one cubic meter!",
    "A mile is 5,280 feet long!",
    "The metric system is used by 95% of the world's population!",
    "A liter of water weighs exactly one kilogram!",
    "The original definition of a meter was one ten-millionth of the distance from the equator to the North Pole!",
    "One horsepower is equivalent to 746 watts!",
    "A foot was originally based on the length of a human foot!",
    "An acre is approximately the size of a football field!",
    "One knot is equal to 1.852 kilometers per hour!",
    "A square mile is 640 acres!",
    "A fluid ounce in the US is different from a fluid ounce in the UK!",
    "The Fahrenheit and Celsius scales intersect at -40 degrees!",
    "A metric ton is 1,000 kilograms, but a US ton is 2,000 pounds!",
    "An inch was originally defined as three barleycorns laid end to end!"
]
ureg = pint.UnitRegistry()

ureg.define("fluid_ounce = 29.5735 * milliliter = fl_oz")
ureg.define("cubic_metre = meter ** 3")
ureg.define("square_metre = meter ** 2")
ureg.define("square_kilometre = kilometer ** 2")

random_fact = random.choice(fun_facts)

def apply_modern_ui():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

        * {
            font-family: 'Poppins', sans-serif;
        }

        .stSidebar {
            background: #0f172a;
            color: white;
        }

        .stButton>button {
            background: linear-gradient(90deg, #6366f1, #8b5cf6);
            color: white;
            font-weight: 600;
            border-radius: 12px;
            width: 100%;
            border: none;
            box-shadow: 0px 4px 15px rgba(99, 102, 241, 0.4);
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            transform: translateY(-3px);
            box-shadow: 0px 7px 20px rgba(99, 102, 241, 0.6);
        }

        /* Minimal AI Response Box */
        .result-box {
            padding: 8px 12px;
            background: transparent;
            border-radius: 5px;
            margin-top: 10px;
            text-align: left;
            font-size: 0.85rem;
            font-weight: 400;
            color: #ffffff;
            border-left: 3px solid #5b5b5b;
            line-height: 1.5;
        }

        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: #64748b;
            margin-top: 2rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

        * {
            font-family: 'Poppins', sans-serif;
        }

        .stSidebar {
            background: #0f172a;
            color: white;
        }

        .stButton>button {
            background: linear-gradient(90deg, #6366f1, #8b5cf6);
            color: white;
            font-weight: 600;
            border-radius: 12px;
            width: 100%;
            border: none;
            box-shadow: 0px 4px 15px rgba(99, 102, 241, 0.4);
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            transform: translateY(-3px);
            box-shadow: 0px 7px 20px rgba(99, 102, 241, 0.6);
        }

        /* Professional result box */
        .result-box {
            padding: 10px;
            background: transparent;
            border-radius: 5px;
            margin-top: 10px;
            text-align: left;
            font-size: 0.9rem;
            font-weight: 400;
            color: #ffffff;
            border-left: 4px solid #5b5b5b;
        }

        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: #64748b;
            margin-top: 2rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

        * {
            font-family: 'Poppins', sans-serif;
        }

        .stSidebar {
            background: linear-gradient(180deg, #1e293b, #0f172a);
            color: white;
        }

        .stButton>button {
            background: linear-gradient(90deg, #6366f1, #8b5cf6);
            color: white;
            font-weight: 600;
            border-radius: 12px;
            width: 100%;
            border: none;
            box-shadow: 0px 4px 15px rgba(99, 102, 241, 0.4);
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            transform: translateY(-3px);
            box-shadow: 0px 7px 20px rgba(99, 102, 241, 0.6);
        }

        .result-box {
            padding: 1.5rem;
            # background:rgb(0, 0, 0);
            border-radius: 12px;
            margin-top: 1rem;
            text-align: left;
            font-size: 0.9rem;
            font-weight: 600;
            color: #ffffff;
            border-left: 4px solidrgb(91, 91, 91);
        }

        .footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: #64748b;
            margin-top: 2rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

apply_modern_ui()

unit_categories = {
    "Length": ["Metre", "Kilometre", "Centimetre", "Millimetre", "Mile", "Yard", "Foot", "Inch", "Nautical Mile"],
    "Weight": ["Kilogram", "Gram", "Milligram", "Pound", "Ounce", "Stone", "Ton"],
    "Volume": ["Litre", "Millilitre", "Gallon", "Pint", "Fluid Ounce", "Cubic Metre"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Time": ["Second", "Minute", "Hour", "Day", "Week", "Month", "Year"],
    "Speed": ["Metre/second", "Kilometre/hour", "Mile/hour", "Knot", "Foot/second"],
    "Area": ["Square metre", "Square kilometre", "Square mile", "Hectare", "Acre", "Square foot"]
}

def convert_units(value, from_unit, to_unit):
    try:
        from_unit = from_unit.lower().replace(" ", "_")
        to_unit = to_unit.lower().replace(" ", "_")

        if "celsius" in from_unit or "fahrenheit" in from_unit or "kelvin" in from_unit:
            q = ureg.Quantity(value, getattr(ureg, from_unit))
            result = q.to(getattr(ureg, to_unit))
        else:
            q = ureg.Quantity(value, from_unit)
            result = q.to(to_unit)

        return f"{value} {from_unit.replace('_', ' ')} = {result.magnitude:.2f} {to_unit.replace('_', ' ')}"
    except pint.DimensionalityError:
        return "🚫 Invalid conversion: units are not compatible"
    except Exception as e:
        return f"⚠️ Error: {str(e)}"





with st.sidebar:
    st.markdown("<h2 style='color: white;'>🚀 Convertify AI</h2>", unsafe_allow_html=True)
    
    mode = st.radio("🎛️ Select Mode", ["🎮 Standard Mode", "🤖 AI Assistant", "📊 Batch Convert"])
    
    selected_category = st.radio("📌 Choose a Category", list(unit_categories.keys()))

    with st.expander("💡 Quick Fact"):
        st.markdown(f"**{random_fact}**")

    with st.expander("ℹ️ About Convertify AI"):
        st.markdown("""
        Convertify AI is the most advanced unit converter powered by artificial intelligence.  
        **Features:**  
        - 🧠 AI-Powered conversions  
        - ⚡ Lightning-fast calculations  
        - 📊 Support for 100+ units  
        - 📱 Responsive design  
        """)

st.markdown("<h1 style='text-align: center;'>🚀 Convertify AI</h1>", unsafe_allow_html=True)

if mode == "🎮 Standard Mode":
    st.markdown("<h3 style='text-align: center; color: white;'>🔄 Standard Conversion</h3>", unsafe_allow_html=True)

    cols = st.columns([2, 1, 2])

    with cols[0]:
        unit_from_display = st.selectbox("From:", unit_categories[selected_category])

   

    with cols[2]:
        unit_to_display = st.selectbox("To:", unit_categories[selected_category], index=1)

    value = st.number_input("Enter value:", min_value=0.0, format="%.4f")

    if st.button("🔄 Convert"):
        with st.spinner("🔄 Processing..."):
            time.sleep(0.5)
            result = convert_units(value, unit_from_display, unit_to_display)
            st.markdown(f"<div class='result-box'>✅ {result}</div>", unsafe_allow_html=True)


if mode == "🤖 AI Assistant":
    user_text = st.text_input("📝 Enter your query:", placeholder="Convert 5 miles to km")
    
    if st.button("🚀 Get AI Result"):
        with st.spinner("🤖 Thinking..."):
            time.sleep(0.5)
            if user_text:
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(f"Convert: {user_text}")
                ai_response = response.text if response else "❌ Error fetching response"
                st.markdown(f"<div class='result-box'>💬 {ai_response}</div>", unsafe_allow_html=True)
            else:
                st.error("❌ Please enter a query!")


if mode == "📊 Batch Convert":
    unit_from_batch = st.selectbox("From Unit:", unit_categories[selected_category])
    unit_to_batch = st.selectbox("To Unit:", unit_categories[selected_category], index=1)
    
    batch_values = st.text_area("Enter values (one per line):", height=150, placeholder="10\n20\n30\n40\n50")
    
    if st.button("📊 Convert Batch"):
        if batch_values:
            values = batch_values.strip().split('\n')
            with st.spinner("⏳ Processing batch conversion..."):
                time.sleep(0.5)
                results = [convert_units(float(val), unit_from_batch, unit_to_batch) for val in values]
                for result in results:
                    st.markdown(f"<div class='result-box'>🔹 {result}</div>", unsafe_allow_html=True)
        else:
            st.error("❌ Please enter values to convert")



st.markdown("<div class='footer'>🚀 Convertify AI | © 2025 | <a href='#' style='color: #6366f1;'>Terms & Privacy</a></div>", unsafe_allow_html=True)
