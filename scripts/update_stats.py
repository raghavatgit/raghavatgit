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
TELEMETRY_PATH = os.path.join(REPO_ROOT, "assets", "telemetry.svg")

def fetch_telemetry():
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
    # 1. Try gh CLI first if available
    try:
        proc = subprocess.run(
            ["gh", "api", "graphql", "-F", f"login={USER_NAME}", "-f", f"query={query}"],
            capture_output=True,
            text=True,
            timeout=15
        )
        if proc.returncode == 0:
            data = json.loads(proc.stdout)
            if "data" in data and "user" in data["data"]:
                return data["data"]["user"]
    except Exception:
        pass

    # 2. Fallback to urllib with GITHUB_TOKEN
    token = os.environ.get("GITHUB_TOKEN")
    payload = json.dumps({"query": query, "variables": {"login": USER_NAME}}).encode("utf-8")
    headers = {
        "User-Agent": "raghavatgit-telemetry-sync",
        "Content-Type": "application/json",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = urllib.request.Request("https://api.github.com/graphql", data=payload, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
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
    
    streak = 0
    for day in reversed(all_days):
        count = day.get("contributionCount", 0)
        if count > 0:
            streak += 1
        elif streak > 0:
            break
    return streak

def update_telemetry_svg(total_contributions, public_repos):
    if not os.path.exists(TELEMETRY_PATH):
        print(f"Telemetry SVG not found at {TELEMETRY_PATH}")
        return False
    
    with open(TELEMETRY_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # Update Annual Contributions counter
    content = re.sub(
        r"(\d+\+?)(\s*</text>\s*<text[^>]*>\s*ANNUAL\s+CONTRIBUTIONS)",
        f"{total_contributions}+\\2",
        content
    )

    # Update Public Codebases counter
    content = re.sub(
        r"(\d+)(\s*</text>\s*<text[^>]*>\s*PUBLIC\s+CODEBASES)",
        f"{public_repos}\\2",
        content
    )

    if content != original:
        with open(TELEMETRY_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {TELEMETRY_PATH} with {total_contributions}+ contributions, {public_repos} repos.")
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
    user_data = fetch_telemetry()
    if not user_data:
        print("Failed to fetch GitHub telemetry.")
        sys.exit(1)

    calendar = user_data.get("contributionsCollection", {}).get("contributionCalendar", {})
    total_contributions = calendar.get("totalContributions", 0)
    weeks = calendar.get("weeks", [])
    streak = calculate_streak(weeks)
    public_repos = user_data.get("repositories", {}).get("totalCount", 12)

    print(f"Fetched Telemetry: {total_contributions} contributions, {streak} day streak, {public_repos} public repos.")

    new_version = int(time.time())

    telemetry_updated = update_telemetry_svg(total_contributions, public_repos)
    readme_updated = update_readme(total_contributions, public_repos, new_version)

    if telemetry_updated or readme_updated:
        print("Telemetry synchronization successfully completed.")
    else:
        print("No changes required. Files already up to date.")

if __name__ == "__main__":
    main()
