# # ✨ *Automation Exercise* ==> *WAP* *Test Automation* ✨ TwitchTest
### 🌐 Website URL: https://m.twitch.tv/

- ### 📝 The main Frameworks included in the project:
 **SHAFT Engine on the Top of:**

 *Selenium WebDriver*
 
 *Python*
 
 *Pytest*
 - ### 🔍️ Covered Test case in this project :
#### ✅Test Case 1: Test case to search for a streamer on Twitch, handle popups, wait for page load, and take a screenshot.
   Steps:
    1. Launch Chrome emulator (headless for efficiency)
    2. Navigate to Twitch
    3. Click the search icon
    4. Input "StarCraft II" in the search bar
    5. Scroll down twice to simulate user behavior
    6. Select the first streamer result
    7. Wait for the streamer page to load completely, handling popups if present
    8. Take a screenshot of the streamer page
    9. Quit the browser

  Notes:
    - This test case prioritizes efficiency by using headless Chrome and waiting specifically for relevant elements.
    - Consider refining the popup handling logic based on specific modal/popup characteristics.
    
