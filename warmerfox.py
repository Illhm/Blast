import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options





# --- CONFIGURATION ---
FF_PROFILE_PATH = r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\16qkizuj.default-release"

# 2. List of numbers to "warm" with (Include country code, no + sign)
CONTACTS = ["081563922708", "085717828273"]

# 3. Varied human-like messages
MESSAGES = [
    "Hey! Hope you're having a productive week.",
    "Yo, just saw something that reminded me of you!",
    "Hi there! How has your day been so far?",
    "Hello! Just reaching out to say hi.",
    "It's been a while, we should catch up soon.",
    "Hope everything is going well on your end.",
    "Just checking in to see how things are moving along.",
    "Are you busy? Just wanted to say hello.",
    "Hey hey!",
    "Have a good one!",
    "Talk soon.",
    "👍",
    "How's the weather over there today?",
    "You around? I had a quick question about something.",
    "Any big plans for the weekend?",
]


def warm_up():
    print("🚀 Starting WhatsApp Warmer for Firefox...")

    options = Options()


    if os.path.exists(FF_PROFILE_PATH):
        options.profile = FF_PROFILE_PATH
    else:
        print("Profile not found, starting without custom profile.")

    # Initialize the driver
    try:
        driver = webdriver.Firefox(options=options)
    except Exception as e:
        print(f"❌ Error: Could not start Firefox. Is it still open? \nDetails: {e}")
        return

    driver.get("https://web.whatsapp.com")

    # Initial wait for the interface to load your chats
    print("⏳ Waiting for WhatsApp Web to load your profile...")
    time.sleep(50)

    for phone in CONTACTS:
        # Pick a random message
        msg = random.choice(MESSAGES)

        # 10% chance to make it lowercase for extra 'human' feel
        if random.random() < 0.10:
            msg = msg.lower()

        print(f"💬 Preparing to message: {phone}")

        # Direct URL to the chat with the message pre-filled
        url = f"https://web.whatsapp.com/send?phone={phone}&text={msg}"
        driver.get(url)

        # Random wait while "typing" (8 to 15 seconds)
        typing_delay = random.randint(8, 15)
        print(f"⌨️ Mimicking typing for {typing_delay} seconds...")
        time.sleep(typing_delay)

        try:
            # Locate the send button
            send_btn = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
            send_btn.click()
            print(f"✅ Message sent to {phone}: '{msg}'")
        except Exception as e:
            print(
                f"⚠️ Could not send to {phone}. The chat might not have loaded correctly."
            )

        # Long break between different contacts (30 to 90 seconds)
        # This is the most important part for account safety!
        cooldown = random.randint(30, 90)
        print(f"😴 Resting for {cooldown} seconds before next contact...")
        time.sleep(cooldown)

    print("\n✨ Warm-up session complete. Closing browser.")
    driver.quit()


if __name__ == "__main__":
    warm_up()
