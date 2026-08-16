import pandas as pd
import numpy as np
import re
# Currency Normalization
def normalize_currency(value):

    

    if pd.isna(value):
        return np.nan

    value = str(value).strip()

    # If startup was integrated/acquired, valuation is unknown
    if "Integrated" in value:
        return np.nan

    # Critically downgraded
    if "Critically" in value:
        return 100

    # Remove unwanted symbols
    value = value.replace("~", "")
    value = value.replace("$", "")
    value = value.replace("+", "")

    # Remove everything inside brackets
    value = re.sub(r"\(.*?\)", "", value)

    value = value.strip()

    if "Bn" in value:

        number = re.findall(r"[\d.]+", value)

        if number:
            return float(number[0]) * 1000

    elif "Mn" in value:

        number = re.findall(r"[\d.]+", value)

        if number:
            return float(number[0])

    else:

        number = re.findall(r"[\d.]+", value)

        if number:
            return float(number[0])

    return np.nan
        
# Percentage Normalization
def normalize_percentage(value):

    if pd.isna(value):
        return np.nan

    value = str(value)

    value = value.replace("%", "")
    value = value.replace("~", "")
    value = value.strip()

    try:
        return float(value)
    except:
        return np.nan

# Traffic Normalization
def normalize_traffic(value):

    

    if pd.isna(value):
        return np.nan

    value = str(value).lower()

    # Remove unnecessary symbols
    value = value.replace("~", "")
    value = value.replace(",", "")
    value = value.replace("+", "")

    # Remove words
    value = value.replace("monthly", "")
    value = value.replace("visits", "")

    # Remove anything inside brackets
    value = re.sub(r"\(.*?\)", "", value)

    value = value.strip()

    # Extract numeric value
    number = re.findall(r"[\d.]+", value)

    if not number:
        return np.nan

    number = float(number[0])

    if "m" in value:
        return number * 1_000_000

    elif "k" in value:
        return number * 1_000

    else:
        return number

# App Download Normalization
def normalize_downloads(value):

    

    if pd.isna(value):
        return np.nan

    value = str(value).lower()

    # Cases where downloads don't exist
    if "n/a" in value:
        return 0

    if "integrated" in value:
        return 0

    # Remove unwanted symbols
    value = value.replace("~", "")
    value = value.replace("+", "")
    value = value.replace(",", "")

    # Remove everything inside brackets
    value = re.sub(r"\(.*?\)", "", value)

    value = value.strip()

    # Extract numeric part
    number = re.findall(r"[\d.]+", value)

    if not number:
        return np.nan

    number = float(number[0])

    if "m" in value:
        return number * 1_000_000

    elif "k" in value:
        return number * 1_000

    else:
        return number
    
# GOOGLE TREND NORMALIZATION
def normalize_google_trend(value):

    if pd.isna(value):
        return np.nan

    try:
        return float(value)
    except:
        return np.nan

# APP RATING NORMALIZATION
def normalize_rating(value):

    if pd.isna(value):
        return np.nan

    value = str(value).replace("/5", "").strip()

    try:
        return float(value)
    except:
        return np.nan
    
# Review Count Normalization
def normalize_reviews(value):

    if pd.isna(value):
        return np.nan

    value = str(value).lower()

    # Remove unwanted symbols
    value = value.replace("~", "")
    value = value.replace("+", "")
    value = value.replace(",", "")

    # Remove text inside brackets
    value = re.sub(r"\(.*?\)", "", value)

    value = value.strip()

    # Extract number
    number = re.findall(r"[\d.]+", value)

    if not number:
        return np.nan

    number = float(number[0])

    if "m" in value:
        return number * 1_000_000

    elif "k" in value:
        return number * 1_000

    else:
        return number
    
# Revenue Normalization (₹ Crore)

def normalize_revenue(value):

    if pd.isna(value):
        return np.nan

    value = str(value)

    # Cases where revenue isn't directly available
    if "Included" in value:
        return np.nan

    if "Group-level" in value:
        return np.nan

    value = value.replace("₹", "")
    value = value.replace(",", "")
    value = value.replace("+", "")
    value = value.replace("Cr", "")

    # Remove anything inside brackets
    value = re.sub(r"\(.*?\)", "", value)

    value = value.strip()

    number = re.findall(r"[\d.]+", value)

    if not number:
        return np.nan

    return float(number[0])

# Funding Normalization (USD Million)

def normalize_funding(value):

    if pd.isna(value):
        return np.nan

    value = str(value)

    # Cases where funding amount is unavailable
    invalid = [
        "Part of",
        "Acquired",
        "Funded internally",
        "Raised via Public Markets"
    ]

    for text in invalid:
        if text.lower() in value.lower():
            return np.nan

    # Clean symbols
    value = value.replace("~", "")
    value = value.replace("$", "")
    value = value.replace("₹", "")
    value = value.replace(",", "")
    value = value.replace("+", "")

    # Remove everything inside brackets
    value = re.sub(r"\(.*?\)", "", value)

    value = value.strip()

    # Extract numeric value
    number = re.findall(r"[\d.]+", value)

    if not number:
        return np.nan

    number = float(number[0])

    # Convert to Million USD scale
    if "Bn" in value:
        return number * 1000

    elif "Mn" in value:
        return number

    # INR values (Crore) - keep numeric value
    elif "Cr" in value:
        return number

    else:
        return number
    
# Profit / Loss Normalization (₹ Crore)

def normalize_profit_loss(value):

    if pd.isna(value):
        return np.nan

    value = str(value)

    value = value.replace("₹", "")
    value = value.replace(",", "")
    value = value.replace("Cr", "")

    # Remove everything inside brackets
    value = re.sub(r"\(.*?\)", "", value)

    value = value.strip()

    number = re.findall(r"-?[\d.]+", value)

    if not number:
        return np.nan

    number = float(number[0])

    if "Profit" in value:
        return abs(number)

    elif "Loss" in value:
        return -abs(number)

    else:
        return number

# TAM Normalization (USD Million)

def normalize_tam(value):

    if pd.isna(value):
        return np.nan

    value = str(value)

    value = value.replace("$", "")
    value = value.replace(",", "")

    # Remove everything inside brackets
    value = re.sub(r"\(.*?\)", "", value)

    value = value.strip()

    number = re.findall(r"[\d.]+", value)

    if not number:
        return np.nan

    number = float(number[0])

    if "Bn" in value:
        return number * 1000

    elif "Mn" in value:
        return number

    return number

# Employee Count Normalization

def normalize_employee_count(value):

    if pd.isna(value):
        return np.nan

    value = str(value)

    value = value.replace("~", "")
    value = value.replace(",", "")
    value = value.replace("+", "")

    # Remove anything inside brackets
    value = re.sub(r"\(.*?\)", "", value)

    value = value.strip()

    number = re.findall(r"[\d.]+", value)

    if not number:
        return np.nan

    return float(number[0])