import os
import re
import sys
import json
import time
import subprocess
import urllib.request
import urllib.error

USER_NAME = "raghavatgit"
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")
SNAKE_PATH = os.path.join(REPO_ROOT, "assets", "snake.svg")

def get_auth_token():
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token
    try:
        out = subprocess.check_output(["gh", "auth", "token"], text=True, stderr=subprocess.DEVNULL)
        if out.strip():
            return out.strip()
    except Exception:
        pass
    return None

def fetch_telemetry(token):
    graphql_url = "https://api.github.com/graphql"
    query = """
    query($login: String!) {
      user(login: $login) {
        contributionsCollection {
          contributionCalendar {
            totalContributions
            weeks {
              contributionDays {
                date
                contributionCount
                color
              }
            }
          }
        }
        repositories(first: 100, ownerAffiliations: OWNER, privacy: PUBLIC) {
          totalCount
        }
      }
    }
    """
    payload = json.dumps({"query": query, "variables": {"login": USER_NAME}}).encode("utf-8")
    headers = {
        "User-Agent": "raghavatgit-telemetry-sync",
        "Content-Type": "application/json",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = urllib.request.Request(graphql_url, data=payload, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if "errors" in data:
                print(f"GraphQL Errors: {data['errors']}")
                return None
            return data.get("data", {}).get("user")
    except Exception as e:
        print(f"Error querying GitHub GraphQL API: {e}")
        return None

def calculate_streak(weeks):
    all_days = []
    for week in weeks:
        for day in week.get("contributionDays", []):
            all_days.append(day)
    
    if not all_days:
        return 0
    
    # Calculate streak from the latest day
    streak = 0
    for day in reversed(all_days):
        count = day.get("contributionCount", 0)
        if count > 0:
            streak += 1
        elif streak > 0:
            # streak broken
            break
    return streak

def update_snake_svg(total_contributions):
    if not os.path.exists(SNAKE_PATH):
        print(f"Snake SVG not found at {SNAKE_PATH}")
        return False
    
    with open(SNAKE_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r"\d+\s+CONTRIBUTIONS\s+IN\s+PAST\s+YEAR"
    replacement = f"{total_contributions} CONTRIBUTIONS IN PAST YEAR"
    
    new_content, count = re.subn(pattern, replacement, content)
    if count > 0 and new_content != content:
        with open(SNAKE_PATH, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {SNAKE_PATH} with {total_contributions} contributions.")
        return True
    return False

def update_readme(total_contributions, public_repos, new_version):
    if not os.path.exists(README_PATH):
        print(f"README.md not found at {README_PATH}")
        return False

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # 1. Update Annual Activity row
    content = re.sub(
        r"\|\s*\*\*Annual Activity\*\*\s*\|\s*[^|]+?\s*\|",
        f"| **Annual Activity** | {total_contributions}+ Contributions (Active Streak) |",
        content
    )

    # 2. Update Active Codebases count
    content = re.sub(
        r"\|\s*\*\*Active Codebases\*\*\s*\|\s*\d+\s+Public Repositories\s*\|",
        f"| **Active Codebases** | {public_repos} Public Repositories |",
        content
    )

    # 3. Bump cache version query params ?v=X -> ?v=new_version
    content = re.sub(
        r"(\.svg\?v=)\w+",
        f"\\g<1>{new_version}",
        content
    )

    if content != original:
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {README_PATH} with total {total_contributions}, {public_repos} repos, cache ?v={new_version}.")
        return True
    return False

def main():
    token = get_auth_token()
    if not token:
        print("Warning: No GITHUB_TOKEN or gh CLI token found. Attempting unauthenticated request...")
    
    user_data = fetch_telemetry(token)
    if not user_data:
        print("Failed to fetch GitHub telemetry.")
        sys.exit(1)

    calendar = user_data.get("contributionsCollection", {}).get("contributionCalendar", {})
    total_contributions = calendar.get("totalContributions", 0)
    weeks = calendar.get("weeks", [])
    streak = calculate_streak(weeks)
    public_repos = user_data.get("repositories", {}).get("totalCount", 12)

    print(f"Fetched Telemetry: {total_contributions} contributions, {streak} day streak, {public_repos} public repos.")

    # Unique cache version tag based on unix timestamp
    new_version = int(time.time())

    snake_updated = update_snake_svg(total_contributions)
    readme_updated = update_readme(total_contributions, public_repos, new_version)

    if snake_updated or readme_updated:
        print("Telemetry synchronization successfully completed.")
    else:
        print("No changes required. Files already up to date.")

if __name__ == "__main__":
    main()
