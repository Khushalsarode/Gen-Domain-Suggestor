import requests
import streamlit as st
import textwrap
import google.generativeai as genai
import pymongo
import random
import os
from dotenv import load_dotenv
load_dotenv()


# Configurethe API key
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

# Function to connect to MongoDB and retrieve domain extensions
def get_domain_extensions():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["domainnamesset"]
    collection = db["extension"]
    extensions = collection.find({}, {"_id": 0})
    return [ext["Extension"] for ext in extensions]

# Function to generate domain name suggestions
def generate_domain_suggestions(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt, stream=True)
    full_response = ""
    for chunk in response:
        full_response += chunk.text
    return full_response

# Function to generate random domain name with provided extension
def generate_random_domain(extension):
    return f"example{extension}"  # Replace "example" with your desired prefix

# Function to convert plain text to markdown format with indentation
def to_markdown(text):
    return textwrap.indent(text.replace('•', '  *'), '> ', predicate=lambda _: True)

# Function to connect to MongoDB and retrieve industry types
def get_industry_types():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["domainnamesset"]
    collection = db["industry"]
    industries = collection.find({}, {"_id": 0})
    return [ind["Industry"] for ind in industries]

# Function to retrieve domain names from MongoDB collection
def get_domain_names():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["domainnamesset"]
    collection = db["domains"]
    domain_names = collection.find({}, {"_id": 0})
    return [doc["domain"].lower() for doc in domain_names]  # Ensure domain names are in lowercase
    
# Function to get random extensions from the MongoDB collection
def get_random_extensions(num_extensions=5):
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["domainnamesset"]
    collection = db["extension"]

    # Retrieve all extensions from the collection
    all_extensions = [doc['Extension'] for doc in collection.find()]

    # Randomly select 4-5 extensions
    random_extensions = random.sample(all_extensions, min(num_extensions, len(all_extensions)))

    return random_extensions


# Function to retrieve WHOIS information for a domain
def get_whois_info(domain_name, api_key):
    url = f"https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={api_key}&domainName={domain_name}&outputFormat=json"

    try:
        response = requests.get(url)
        data = response.json()

        if "ErrorMessage" in data:
            # If an error message is received, return None
            return None

        whois_record = data.get("WhoisRecord", {})
        registry_data = whois_record.get("registryData", {})
        registrant = registry_data.get("registrant", {})
        
        # Check if 'registrant' exists in the WHOIS record
        if registrant:
            registrant_name = registrant.get("name", "")
            registrant_org = registrant.get("organization", "")
            registrant_email = registrant.get("email", "")
        else:
            registrant_name = ""
            registrant_org = ""
            registrant_email = ""

        domain_info = {
            "Domain Name": whois_record.get("domainName", ""),
            "Registrar Name": whois_record.get("registrarName", ""),
            "Creation Date": registry_data.get("createdDate", ""),
            "Expiration Date": registry_data.get("expiresDate", ""),
            "Registrant Name": registrant_name,
            "Registrant Organization": registrant_org,
            "Registrant Email": registrant_email,
            "Name Servers": registry_data.get("nameServers", {}).get("hostNames", []),
            "Domain Status": registry_data.get("status", "")
        }
        return domain_info

    except Exception as e:
        print("An error occurred:", e)
        return None

# Function to connect to MongoDB and check if domain exists
def check_domain_exists(domain_name):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["domainnamesset"]
    collection = db["domain"]
    domain_document = collection.find_one({"domain": domain_name.lower()})
    return domain_document is not None

def chat_with_gemini():
  """
  Manages the chat interaction with the Gemini model.
  """
  try:
    # Initialize the chat
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])

    # Create empty container
    conversation_history = st.container()

    # Set title for the container
    st.write("Conversation History")  # This sets the title

    # Chat input for user messages
    user_input = st.text_input("You:", key="user_input", placeholder="Enter your message")

    # Send message and display response
    if st.button("Send"):
      if user_input:
        # Add user message to conversation history
        conversation_history.text(f"You: {user_input}")

        # Send user message to the chat
        response = chat.send_message(user_input, stream=True)

        # Display response chunks
        for chunk in response:
          conversation_history.text(f"Bot: {chunk.text}")
      else:
        st.warning("Please enter a message to send.")
  except Exception as e:
    st.error(f"An error occurred: {e}")

# Streamlit app
def main():
     # Sidebar for options
    st.sidebar.title("App Menu")
    option = st.sidebar.radio("Pages:", ["Generate Domain Name Suggestions", "Generate Random Domain Names", "Check Domain Availability", "Check Domain Availability Locally", "chat with me"])
    # Display database statistics
   
    # Display the selected option
    if option == "Generate Domain Name Suggestions":
        st.title("Domain Name Suggestion App")
        # User inputs
        project_name = st.text_input("Enter your project name or description:")
        primary_keywords = st.text_area("Enter primary keywords (separated by commas):")
        secondary_keywords = st.text_area("Enter secondary keywords (separated by commas):")
        # Load industry types from MongoDB collection
        industry_types = get_industry_types()
        
        # User selects an industry type
        industry_type = st.selectbox("Select an industry type:", industry_types)
        # Load domain extensions from MongoDB collection
        domain_extensions = get_domain_extensions()
        
        # User selects either domain extensions or enters a custom extension
        option = st.radio("Choose an option:", ["Select domain extension(s)", "Enter custom extension (e.g., '.com')"])
        
        if option == "Select domain extension(s)":
            # User selects domain extensions
            selected_extensions = st.multiselect("Select domain extensions:", domain_extensions)
            extensions = selected_extensions
        else:
            # Input box for custom extension
            custom_extension = st.text_input("Enter custom extension (e.g., '.com'):")
            extensions = [custom_extension] if custom_extension else []
        # Arrange the buttons side by side
        # Generate suggestions when 'Generate' button is clicked
        if st.button("Generate"):
                # Check if all required fields are filled
            if not project_name or not primary_keywords or not secondary_keywords or not extensions:
                st.error("Please fill in all required fields before generating suggestions.")
                return
                
            prompt = f"Provide creative and unique domain name suggestions for the {industry_type} industry. The domain should relate to {project_name} and included this keywords: {primary_keywords}, {secondary_keywords} may help you grab the best. Please include the following extensions: {', '.join(extensions)} and at end also provide the SEO Metadata & Taglines based on prompt and domains!"
            st.write("Generating domain name suggestions...")
                
                # Generate domain name suggestions
            try:
                suggestions = generate_domain_suggestions(prompt)
                formatted_suggestions = to_markdown(suggestions)
                st.write("## Domain Name Suggestions:")
                st.markdown(formatted_suggestions)
            except Exception as e:
                st.error(f"Error: {e}")

    elif option == "Generate Random Domain Names":
        st.title("Random Domain Name Generator")
        # Button to generate random domain names using selected extensions
        if st.button("Suprise Me!"):
            # Get 4-5 random extensions from the MongoDB collection
            random_extensions = get_random_extensions(num_extensions=random.randint(4, 5))

            if not random_extensions:
                st.error("No domain extensions found in the database.")
                return
            
                # Construct prompt for generating random domain names with the randomly selected extensions
            random_prompt = f"Generate creative and unique domain names using the following extensions: {', '.join(random_extensions)}."
            
            st.write("Generating random domain names...")
            try:
                    # Generate random domain names
                random_domains = generate_domain_suggestions(random_prompt)
                st.write("## Random Domain Names:")
                st.markdown(random_domains)
            except Exception as e:
                st.error(f"Error: {e}")

    elif option == "Check Domain Availability":
        st.title("Check for Domain Availability")
        # Get user input for domain name and API key
        domain_to_check = st.text_input("Enter the domain name to check availability:")
        api_key = os.getenv("WHOISXMLAPI_API_KEY")  # Fetch API key from environment variable

        # Check domain availability when the button is clicked
        if st.button("Check Domain Availability"):
            # Ensure both domain name and API key are provided
            if domain_to_check and api_key:
                # Retrieve WHOIS information for the entered domain name
                domain_info = get_whois_info(domain_to_check, api_key)
                print(domain_info)
                # Check if WHOIS information is retrieved successfully
                if domain_info:
                    # Display domain information if available
                    st.write("## Domain Information:")
                    if domain_info["Registrar Name"]:
                        st.write("Registrar Name:", domain_info["Registrar Name"])
                    if domain_info["Creation Date"]:
                        st.write("Creation Date:", domain_info["Creation Date"])
                    if domain_info["Expiration Date"]:
                        st.write("Expiration Date:", domain_info["Expiration Date"])
                    if domain_info["Registrant Name"]:
                        st.write("Registrant Name:", domain_info["Registrant Name"])
                    if domain_info["Registrant Organization"]:
                        st.write("Registrant Organization:", domain_info["Registrant Organization"])
                    if domain_info["Registrant Email"]:
                        st.write("Registrant Email:", domain_info["Registrant Email"])
                    if domain_info["Name Servers"]:
                        st.write("Name Servers:", ", ".join(domain_info["Name Servers"]))
                    if domain_info["Domain Status"]:
                        st.write("Domain Status:", domain_info["Domain Status"])
                    if domain_info["Registrar Name"]:
                        st.error(f"The domain {domain_to_check} is already taken.")

                    # Check if any domain information is empty
                    #if not domain_info["Registrar Name"] or not domain_info["Creation Date"] or not domain_info["Expiration Date"] or not domain_info["Registrant Name"] or not domain_info["Registrant Organization"] or not domain_info["Registrant Email"] or not domain_info["Name Servers"] or not domain_info["Domain Status"]:
                        # Display a popup message indicating that the domain exists
                        
                    else:
                        # Display an error message indicating that the domain is already taken
                        st.success(f"The domain {domain_to_check} is available!")
                else:
                    # Display a popup message indicating that the domain exists
                    st.success(f"The domain {domain_to_check} is available!")
            else:
                st.error("Please provide both the domain name!")
    elif option == "Check Domain Availability Locally":
         # Display the selected option
        # Get user input for domain name
        domain_to_check = st.text_input("Enter the domain name to check availability:")

        # Check domain availability when the button is clicked
        if st.button("Check Domain Availability"):
            # Ensure domain name is provided
            if domain_to_check:
                # Check if the domain exists in the local database
                domain_exists = check_domain_exists(domain_to_check)
                
                if domain_exists:
                    st.error(f"The domain {domain_to_check} already exists in the database.")
                else:
                    st.success(f"The domain {domain_to_check} is available!")
            else:
                st.error("Please provide the domain name.")
    elif option == "chat with me":
        st.title("Chat with Gemini")
        chat_with_gemini()


# Run the app
if __name__ == "__main__":
    main()
