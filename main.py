import time
import requests
from documentcloud.addon import AddOn

class DebugTokenAddOn(AddOn):
    """Debug Add-On to inspect DocumentCloud client tokens safely."""

    def main(self):
        # Get client tokens and Authorization header
        access_token = getattr(self.client, "access_token", None)
        refresh_token = getattr(self.client, "refresh_token", None)
        auth_header = self.client.session.headers.get("Authorization")

        print("=== Initial Client State ===")
        print("Access Token:", access_token)
        print("Refresh Token:", refresh_token)
        print("Authorization header:", auth_header)

        # Warn if no tokens
        if not refresh_token:
            print("Warning: No refresh token set!")
        if not access_token:
            print("Warning: No access token set!")

        # Sleep to give you time to inspect logs
        # print("Sleeping for 360 seconds to inspect token refresh logic...")
        self.set_message("Test Point 1")

        access_token = getattr(self.client, "access_token", None)
        refresh_token = getattr(self.client, "refresh_token", None)
        auth_header = self.client.session.headers.get("Authorization")

        print("=== Client State After 1st Call ===")
        print("Access Token:", access_token)
        print("Refresh Token:", refresh_token)
        print("Authorization header:", auth_header)

        # Warn if no tokens
        if not refresh_token:
            print("Warning: No refresh token set!")
        if not access_token:
            print("Warning: No access token set!")




        # time.sleep(360)

        # Optionally, try refreshing tokens if a refresh token exists
        # self.set_message("Test Point 2")

if __name__ == "__main__":
    DebugTokenAddOn().main()