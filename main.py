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
        # time.sleep(360)

        # Optionally, try refreshing tokens if a refresh token exists
        if refresh_token:
            print("\nAttempting manual refresh using refresh token...")
            try:
                url = "https://accounts.muckrock.com/api/refresh/"
                response = requests.post(url, json={"refresh": refresh_token}, timeout=10)
                print("Manual refresh status code:", response.status_code)
                try:
                    data = response.json()
                    print("Manual refresh response JSON:", data)
                    # Update client session headers safely if refresh succeeded
                    if "access" in data:
                        self.client.access_token = data["access"]
                        self.client.refresh_token = data["refresh"]
                        self.client.session.headers["Authorization"] = f"Bearer {data['access']}"
                        print("Client updated with new access token.")
                except Exception:
                    print("Manual refresh response content:", response.content)
            except Exception as e:
                print("Manual refresh failed:", e)

if __name__ == "__main__":
    DebugTokenAddOn().main()