#!/usr/bin/env python3
"""Generate terminal GIF with catppuccin-mocha theme for GitHub README."""

import os
import sys

# Add gifos to path
sys.path.insert(0, '/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages')

# Load .env file
from dotenv import load_dotenv
load_dotenv()

import gifos
from gifos.utils.fetch_github_stats import fetch_github_stats
from gifos.utils.schemas.github_user_stats import GithubUserStats
from gifos.utils.schemas.github_user_rank import GithubUserRank

# Try to fetch GitHub stats for sutz2001, use fallback data if no token
print("Fetching GitHub stats...")
try:
    github_stats = fetch_github_stats(user_name="sutz2001")
    if github_stats is None:
        raise Exception("Failed to fetch stats")
except (Exception, SystemExit) as e:
    print(f"Warning: Could not fetch GitHub stats ({e})")
    print("Using fallback data...")
    # Fallback data based on current README stats
    github_stats = GithubUserStats(
        account_name="sutz2001",
        total_followers=5,
        total_stargazers=0,
        total_issues=0,
        total_commits_all_time=0,
        total_commits_last_year=0,
        total_pull_requests_made=0,
        total_pull_requests_merged=0,
        pull_requests_merge_percentage=0.0,
        total_pull_requests_reviewed=0,
        total_repo_contributions=0,
        languages_sorted=[],
        user_rank=GithubUserRank(
            level="Advanced",
            percentile=90.0
        )
    )

# Create terminal with appropriate size for README
# width=640, height=320 ensures all content is visible
t = gifos.Terminal(
    width=640,
    height=320,
    xpad=5,
    ypad=5,
    font_size=16,
    line_spacing=4
)

# Set color scheme to catppuccin-mocha
t.set_bg_color("#1E1E2E")  # catppuccin-mocha background
t.set_txt_color("#CDD6F4")  # catppuccin-mocha foreground

# Generate boot sequence
t.gen_text(text="\x1b[32m> Initializing system...\x1b[0m", row_num=1)
t.gen_text(text="\x1b[32m> Loading neofetch...\x1b[0m", row_num=2)
t.gen_text(text="\x1b[32m> Fetching GitHub stats...\x1b[0m", row_num=3)

# Clear and show final content
t.delete_row(row_num=1)
t.delete_row(row_num=2)
t.delete_row(row_num=3)

# Generate neofetch-style output with GitHub stats
row = 1
t.gen_text(text="\x1b[36m+==========================================================+\x1b[0m", row_num=row)
row += 1
t.gen_text(text=f"\x1b[36m|\x1b[0m  \x1b[35m{github_stats.account_name}\x1b[0m@{github_stats.account_name}  \x1b[90m--------------------\x1b[0m", row_num=row)
row += 1
t.gen_text(text="\x1b[36m|\x1b[0m  \x1b[90mOS:\x1b[0m GitHub Profile", row_num=row)
row += 1
t.gen_text(text=f"\x1b[36m|\x1b[0m  \x1b[90mHost:\x1b[0m {github_stats.account_name}", row_num=row)
row += 1
t.gen_text(text=f"\x1b[36m|\x1b[0m  \x1b[90mCommits:\x1b[0m {github_stats.total_commits_all_time} total", row_num=row)
row += 1
t.gen_text(text=f"\x1b[36m|\x1b[0m  \x1b[90mRank:\x1b[0m {github_stats.user_rank}", row_num=row)
row += 1
t.gen_text(text="\x1b[36m|\x1b[0m", row_num=row)
row += 1
t.gen_text(text=f"\x1b[36m|\x1b[0m  \x1b[90mFollowers:\x1b[0m \x1b[33m{github_stats.total_followers}\x1b[0m", row_num=row)
row += 1
t.gen_text(text=f"\x1b[36m|\x1b[0m  \x1b[90mStars:\x1b[0m \x1b[31m{github_stats.total_stargazers}\x1b[0m", row_num=row)
row += 1
t.gen_text(text=f"\x1b[36m|\x1b[0m  \x1b[90mIssues:\x1b[0m \x1b[31m{github_stats.total_issues}\x1b[0m", row_num=row)
row += 1
t.gen_text(text=f"\x1b[36m|\x1b[0m  \x1b[90mPRs:\x1b[0m \x1b[32m{github_stats.total_pull_requests_made}\x1b[0m", row_num=row)
row += 1
t.gen_text(text=f"\x1b[36m|\x1b[0m  \x1b[90mContributed to:\x1b[0m \x1b[32m{github_stats.total_repo_contributions}\x1b[0m", row_num=row)
row += 1
t.gen_text(text="\x1b[36m|\x1b[0m", row_num=row)
row += 1
t.gen_text(text="\x1b[36m|\x1b[0m  \x1b[90mShell:\x1b[0m bash", row_num=row)
row += 1
t.gen_text(text="\x1b[36m|\x1b[0m  \x1b[90mTheme:\x1b[0m catppuccin-mocha", row_num=row)
row += 1
t.gen_text(text="\x1b[36m|\x1b[0m  \x1b[90mTerminal:\x1b[0m github-readme-terminal", row_num=row)
row += 1
t.gen_text(text="\x1b[36m+==========================================================+\x1b[0m", row_num=row)

# Set FPS and generate GIF
print("Generating GIF...")
t.set_fps(15)
t.gen_gif()

print("Done! Generated terminal.gif")