import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF


st.markdown("""
<style>
    .stMetric {
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Basic App Setup
st.set_page_config(page_title="Ethiopia Climate Finace Dashboard", layout="wide")

st.title("Ethiopia Climate Finance & Carbon Market Readiness Dashboard")
st.markdown("Policy Intelligence Tool for COP32")


# Load Data
@st.cache_data
def load_data():
    df = pd.read_parquet("data/processed/oecd_final.parquet")
    return df

df = load_data()

ethiopia_df = df[
    df["RecipientName"].str.contains("Ethiopia", case=False, na=False)
].copy()

@st.cache_data
def load_data():
    return pd.read_parquet("data/processed/oecd_final.parquet")

df = load_data()

ethiopia_df = df[
    df["RecipientName"].str.contains("Ethiopia", case=False, na=False)
].copy()

# ---- FILTERS ----
st.sidebar.header("Filters")

years = sorted(ethiopia_df["Year"].unique())
selected_years = st.sidebar.multiselect("Select Year", years, default=years)

donors = sorted(ethiopia_df["DonorName"].dropna().unique())
selected_donors = st.sidebar.multiselect("Select Donor", donors)

sectors = sorted(ethiopia_df["SectorName"].dropna().unique())
selected_sectors = st.sidebar.multiselect("Select Sector", sectors)

# Apply filters
filtered_df = ethiopia_df[
    ethiopia_df["Year"].isin(selected_years)
]

if selected_donors:
    filtered_df = filtered_df[filtered_df["DonorName"].isin(selected_donors)]

if selected_sectors:
    filtered_df = filtered_df[filtered_df["SectorName"].isin(selected_sectors)]

# Slider Navigation
st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Go To: ",
    [
        "Overview",
        "Climate Finance Trend",
        "Donors",
        "Sector Analysis",
        "Forecast",
        "Risk Analysis",
        "Policy Insights"
    ]
)



# Build Sections
# Overview
if section == "Overview":
    st.header("Overview")

    total_funding = ethiopia_df["USD_Commitment"].sum()
    st.metric("Total Climate Finance (USD)", f"{total_funding:,.0f}")

    st.markdown("""
    This dashboard analyzes Ethiopia’s climate finance flows,
    carbon market readiness, and policy risks ahead of COP32.
    """)
    
# Climate Finance Trend
elif section == "Climate Finance Trend":
    st.header("Climate Finance Trend")

    trend = ethiopia_df.groupby("Year")["USD_Commitment"].sum()

    fig, ax = plt.subplots()
    trend.plot(ax=ax)
    ax.set_title("Climate Finance Trend")
    ax.set_ylabel("USD Commitment")

    st.pyplot(fig)
    
# Donors
elif section == "Donors":
    st.header("Top Donors")

    donors = (
        ethiopia_df.groupby("DonorName")["USD_Commitment"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(donors)
    
# Sector Analysis
elif section == "Donors":
    st.header("Top Donors")

    donors = (
        ethiopia_df.groupby("DonorName")["USD_Commitment"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(donors)

# Forecast
elif section == "Forecast":
    st.header("Forecast")

    trend = ethiopia_df.groupby("Year")["USD_Commitment"].sum().reset_index()

    st.line_chart(trend.set_index("Year"))
    
    st.markdown("""
    Forecast suggests steady growth but highlights dependence on external funding.
    """)

# Risk Analysis
elif section == "Risk Analysis":
    st.header("Risk Analysis")

    risk_data = {
        "Donor Dependency": 71,
        "Climate Alignment": 87,
        "Volatility": 21,
        "Sector Concentration": 10
    }

    st.bar_chart(pd.Series(risk_data))
    
# Policy Insights
elif section == "Policy Insights":
    st.header("Policy Recommendations")

    st.markdown("""
    1. Strengthen Climate Finance Tagging
         - Increase Climate-Tagged Finance
         - Strengthen classification and reporting standards
         - Align projects with mitigation/adaptation
         - Ensure alignment with mitigation and adaptation objectives

    2. Develop Carbon Market Project Pipeline
         - Priorities/Invest in:
             - forestry
             - land restoration
             - agriculture carbon projects

         * Align with Article 6 mechanisms

    3. Improve MRV Systems
             - Strengthen Monitoring, Reporting, and Verification
             - Enable credible carbon credits generation
             - builds investor confidence

    4. Diversify Funding Sources
          - Expand engagemet with:
             - private sector
             - multilateral funds
             - carbon markets

    5. Shift from Reactive → Strategic Investment
         - reduce over-reliance on emergency funding
         - prioritize long-term resilience sectors

    6. Implications for COP32: 
    Ethiopia has a strong opportunity to position itself as a climate finance and carbon market leader; however, doing so will require addressing structural inefficiencies in climate finance allocation and strengthening mitigation-focused investment pipelines ahead of COP32.  
    """)
    
st.header("🔮 Scenario Comparison")

years = list(range(2024, 2030))

bau = [19000, 19500, 20000, 20500, 21000, 21500]
policy = [19000, 20500, 22000, 24000, 26000, 28000]
carbon = [19000, 21000, 24000, 27000, 30000, 34000]

fig, ax = plt.subplots()

ax.plot(years, bau, label="Business as Usual")
ax.plot(years, policy, label="Policy Improvement")
ax.plot(years, carbon, label="Carbon Market Expansion")

ax.legend()
ax.set_title("Climate Finance Scenarios")

st.pyplot(fig)

col1, col2, col3 = st.columns(3)

col1.metric("Total Finance", f"{filtered_df['USD_Commitment'].sum():,.0f}")
col2.metric("Top Donor Share", "71%")
col3.metric("Climate Targeted Share", "13%")

# Use ASCII Cleaning for PDF
def clean_text(text):
    return text.encode("latin-1", "ignore").decode("latin-1")

# Export to PDF
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Climate Finance Policy Brief", ln=True)

    pdf.multi_cell(0, 10, txt=clean_text("""
    
 POLICY BRIEFING (NOTEBOOK 05 or final section)

 1. Executive Summary 

Ethiopia’s climate finance landscape demonstrates steady growth (approximately 8.7% annually) with moderate stability. However, funding remains highly concentrated among a small number of donors and only a limited share (approximately 13%) is explicitly climate-targeted. Scenario analysis indicates that, without targeted policy intervention, Ethiopia’s ability to leverage carbon markets under Article 6 of the Paris Agreement will remain constrained. Strengthening mitigation-focused investment, improving climate finance tagging, and diversifying funding sources will be critical priorities ahead of COP32.

 2. Key Findings (Data → Insight)

   - Climate Finance Trends
       - Climate finance is growing (approx. 8.7% annually)
       - Moderate volatility → relatively stable inflows
       - Insight:
          - Growth is consistent but not yet strategically aligned with long-term climate objectives

    - Donor Structure
       - Top two donors account for approximately 71% of total funding
       - Insight:
          - High dependency risk → vulnerability to funding shocks
          - High concentration creates vulnerability to external funding shifts

    - Sector Allocation
       - Strong/Significant funding in agriculture and water
       - Large share in emergency response
       - Insight:
           - Financing remains partially reactive rather than fully resilience-oriented

    - Climate Alignment
       - Only approximately 13% of funding is climate-targeted
       - Insight:
           - Limited alignment with mitigation and adaptation objectives constrains effective climate outcomes


 3. Strategic Risks (VERY IMPORTANT)


   1. Donor Dependency Risk
        - Over-reliance on a small number of donors limits financial resilience.
        - Exposure to funding volatility due to concentration

   2. Misaligned Financing
        - Low climate tagging reduces effectiveness, accountability, and transparency.

   3. Limited Carbon Market Readiness
        - Insufficient mitigation-focused investment constrains participation in carbon markets.

   4. Reactive Investment Pattern
        - High emergency funding indicates short-term response over long-term resilience (i.e., Emergency funding dominates over long-term resilience planning). 

 4. Scenario Insights (FROM YOUR MODEL)

   - Business as Usual:
       - Growth continues
       - Structural issues remain
       - Outcome:
           - Limited improvement in readiness

   - Policy Improvement Scenario
       - Climate share increases
       - Outcome:
           - Better access to climate finance + stronger alignment

   - Carbon Market Expansion Scenario:
       - Higher mitigation funding
       - Increased growth
       - Outcome:
           - Ethiopia becomes competitive in carbon markets


 5. Policy Recommendations 

    1. Strengthen Climate Finance Tagging
         - Increase Climate-Tagged Finance
         - Strengthen classification and reporting standards
         - Align projects with mitigation/adaptation
         - Ensure alignment with mitigation and adaptation objectives

    2. Develop Carbon Market Project Pipeline
         - Priorities/Invest in:
             - forestry
             - land restoration
             - agriculture carbon projects

         * Align with Article 6 mechanisms

    3. Improve MRV Systems
             - Strengthen Monitoring, Reporting, and Verification
             - Enable credible carbon credits generation
             - builds investor confidence

    4. Diversify Funding Sources
          - Expand engagemet with:
             - private sector
             - multilateral funds
             - carbon markets

    5. Shift from Reactive → Strategic Investment
         - reduce over-reliance on emergency funding
         - prioritize long-term resilience sectors

    6. Implications for COP32: 
    Ethiopia has a strong opportunity to position itself as a climate finance and carbon market leader; however, doing so will require addressing structural inefficiencies in climate finance allocation and strengthening mitigation-focused investment pipelines ahead of COP32.


 I developed a climate finance intelligence system to assess Ethiopia’s readiness for carbon market participation. The analysis showed that while climate finance is growing steadily, only a small proportion is climate-targeted and funding is highly concentrated among a few donors. I then modeled future scenarios and found that improving climate alignment and increasing mitigation-focused investment could significantly enhance readiness ahead of COP32.

    """)
)

    file_path = "report.pdf"
    pdf.output(file_path)
    return file_path

if st.button("Download Policy Brief (PDF)"):
    file = generate_pdf()
    with open(file, "rb") as f:
        st.download_button("Download", f, file_name="policy_brief.pdf")