import requests
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
COMPANY_ID = os.getenv("COMPANY_ID")
COMPANY_NAME = os.getenv("COMPANY_NAME")

# Function to post content on LinkedIn
def post_to_linkedin(access_token, author, content):
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"
    }
    post_data = {
        "author": f"urn:li:organization:{author}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": content},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }
    response = requests.post(url, headers=headers, json=post_data)
    return response.json()  # You should handle errors and responses properly in real usage

def generate_linkedin_content(company_name):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a helpful assistant to post on LinkedIn for {company_name} company."},
            {"role": "user", "content": "Generate a professional LinkedIn post for a tech company focusing on innovation and community engagement."},
        ]
    )
    
    print(response.choices[0].message.content)
    return response.choices[0].message.content

# Main function to orchestrate the posting process
def main():
    # Placeholder for content - replace this with your content generation logic
    # For example, using GPT-3 to generate content based on certain prompts or data
    # generated_content = "This is a test post generated by AutoGPT for our company. #Tech #Innovation"
    generated_content = generate_linkedin_content(COMPANY_NAME)
    
    # Post the generated content to LinkedIn
    response = post_to_linkedin(LINKEDIN_ACCESS_TOKEN, COMPANY_ID, generated_content)
    print(response)  # You should add proper error handling and logging

if __name__ == "__main__":
    main()
