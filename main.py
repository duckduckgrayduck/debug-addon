import time
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
        # time.sleep(360)

        # Optionally, try refreshing tokens if a refresh token exists
        if refresh_token:
            print("Attempting manual _set_tokens() refresh...")
            self.client._set_tokens()
            print("After _set_tokens():")
            print("Access Token:", getattr(self.client, "access_token", None))
            print("Refresh Token:", getattr(self.client, "refresh_token", None))
            print("Authorization header:", self.client.session.headers.get("Authorization"))
        self.set_message("DebugTokenAddOn finished inspection!")

if __name__ == "__main__":
    DebugTokenAddOn().main()