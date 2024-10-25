import streamlit as st

st.title("About us")

overview = '''<p>The web application functions as a comprehensive platform for guiding users through HDB resale flat purchasing procedures and price analysis. 
It subtly integrates automation, web scraping, and data filtering to offer seamless, user-friendly tools, delivering relevant, up-to-date insights to assist prospective home buyers in their decisions.</p>

        <p><h5>Use Case 1: Chatbot for Resale Flat Buying Procedures</h5></p>

<p>The Resale Flat Buying Procedure Chatbot is built to assist users in navigating the intricate steps of purchasing an HDB resale flat. 
From eligibility requirements and essential documents to important milestones in the buying journey, the chatbot delivers clear, accurate, and timely information. 
By incorporating web scraping from the HDB website, it ensures users always have the latest procedural details and guidelines readily available.</p>

    <p>Key Features:<br>
        1) Live, step-by-step assistance throughout the resale flat buying process<br>
        2) Immediate answers to frequently asked questions on eligibility, required documents, and key timelines<br>
        3) Accurate information sourced directly from the official HDB website via web scraping
    </p>

        <p><h5>Use Case 2: Resale Flat Price Lookup for HDB</h5></p>

<p>For individuals looking to buy or sell resale flats, our HDB Resale Flat Price Search tool provides a quick and convenient way to explore the market. 
By entering search criteria such as flat type or price range, users can access filtered transaction data from the past 12 months, resulting in a tailored list of resale prices. 
Powered by a data-driven system, this feature delivers real-time pricing information, helping users make well-informed decisions regarding their flat purchase or sale.</p>

    <p>Key Features:<br>
        1) User-friendly interface for seamless navigation and data exploration<br>
        2) Dynamic search feature to filter HDB resale flat prices by flat type or price range
    </p>
'''

st.html(overview)