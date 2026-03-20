import time
from documentcloud.addon import AddOn

class DebugTokenAddOn(AddOn):
    """Debug Add-On to inspect DocumentCloud client tokens safely."""

    def main(self):
        for i in range(1, 8):
            # Get client tokens and Authorization header
            access_token = getattr(self.client, "access_token", None)
            refresh_token = getattr(self.client, "refresh_token", None)
            auth_header = self.client.session.headers.get("Authorization")

            print(f"=== Client State Before Call {i} ===")
            print("Access Token:", access_token)
            print("Refresh Token:", refresh_token)
            print("Authorization header:", auth_header)

            if not refresh_token:
                print("Warning: No refresh token set!")
            if not access_token:
                print("Warning: No access token set!")

            # Set a message
            self.set_message(f"Test Point {i}")

            print(f"=== Message {i} sent, sleeping 60s ===")
            time.sleep(60)  # sleep for 60 seconds between each message

        print("Finished sending 7 messages at 1-minute intervals.")

if __name__ == "__main__":
    DebugTokenAddOn().main()