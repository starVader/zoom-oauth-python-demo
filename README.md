# Setup locally
git clone https://github.com/starVader/zoom-oauth-python-demo.git  
virtualenv -p python3 venv  
source venv/bin/activate  
pip install -r requirements.txt

setup .env file, add zoom secrets and redirect URL 

#Run
python main.py 
this will start a server listening on port 4000

# Install ngrok
During the OAuth flow, Zoom will need to know where to redirect a user after they have successfully authenticated and installed the app on their account.

For this we'll use ngrok, which creates a public link to a localhost development server.

Download and install ngrok, then follow the steps to connect your account.

Run ngrok on the same localhost port (4000):

~/./ngrok http 4000
This will generate a forwarding link. Copy this and add it into your .env file as the redirectURL. Keep ngrok running! If the linkage disconnects, we'll need to readd a new redirectURL.

Example:

redirectURL=https://example.ngrok.io
# Create an OAuth App on the Zoom App Marketplace

Sign in to the Zoom App Marketplace and Create an OAuth App.

Creating this app will generate your OAuth Client ID and Secret needed to install on your account and get an access token.

Copy these credentials and add them to your .env file.

Example:

clientID=86fnfgbn44  
clientSecret=cb784bf84fgb4f4f4f43f  
redirectURL=https://example.ngrok.io  
Add your Redirect URL from ngrok to your app  
Copy and paste your ngrok link into the Redirect URL for OAuth field, then click Continue.

# install app
Run install option available under local test tab on zoom website

