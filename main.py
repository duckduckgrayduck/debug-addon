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

            if not refresh_token:
                print("Warning: No refresh token set!")
            if not access_token:
                print("Warning: No access token set!")

            # Analyze refresh token expiration
            if refresh_token:
                try:
                    # JWT is base64url encoded: header.payload.signature
                    payload_b64 = refresh_token.split('.')[1]
                    payload_b64 += '=' * (-len(payload_b64) % 4)  # fix padding
                    payload_json = base64.urlsafe_b64decode(payload_b64)
                    payload = json.loads(payload_json)

                    exp_timestamp = payload.get("exp")
                    if exp_timestamp:
                        exp_dt = datetime.utcfromtimestamp(exp_timestamp)
                        now = datetime.utcnow()
                        remaining = exp_dt - now
                        print(f"Refresh token expires at (UTC): {exp_dt}")
                        print(f"Time remaining: {remaining}")
                    else:
                        print("No 'exp' field found in refresh token payload")
                except Exception as e:
                    print(f"Failed to decode refresh token: {e}")

if __name__ == "__main__":
    DebugTokenAddOn().main()