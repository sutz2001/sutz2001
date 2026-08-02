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

# Personal info (customize these!)
PERSONAL_INFO = {
    'location': 'Germany',
    'bio': 'Business Intelligence Manager | Product Owner | Authorized Signatory',
    'current_project': 'Building a scalable Cloud Data Platform with Azure & Fabric, plus SQL analytics and Python automation',
    'fact': 'Turning data into insights for digital transformation.',
    'fun_fact': 'Certified Can Opener for Cats, providing premium 24/7 meow-based service.',
    'tools': 'SQL, Python, Azure, Fabric, Databricks, SAP SAC/Datasphere, Git, Docker',
    'linkedin': 'linkedin.com/in/seitzmarc',
}

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

# Clear and show final content
t.delete_row(row_num=1)
t.delete_row(row_num=2)
t.delete_row(row_num=3)

# Catppuccin-mocha color palette
COLORS = {
    'bg': '#1E1E2E',        # Background
    'fg': '#CDD6F4',        # Foreground
    'cyan': '#94E2D5',      # Cyan
    'green': '#A6E3A1',     # Green
    'yellow': '#F9E2AF',    # Yellow
    'blue': '#89B4FA',      # Blue
    'magenta': '#F5C2E7',   # Magenta
    'red': '#F38BA8',       # Red
    'orange': '#FAB387',    # Orange
    'gray': '#6C7086',      # Gray (subtext)
    'white': '#BAC2DE',     # White
}

# Generate neofetch-style output with GitHub stats
row = 1
t.set_bg_color(COLORS['bg'])
t.set_txt_color(COLORS['cyan'])
t.gen_text(text="+==========================================================+", row_num=row)
row += 1
t.set_txt_color(COLORS['magenta'])
t.gen_text(text=f"|  {github_stats.account_name}@{github_stats.account_name}  --------------------", row_num=row)
row += 1
t.set_txt_color(COLORS['fg'])
t.gen_text(text="|  OS: GitHub Profile", row_num=row)
row += 1
t.gen_text(text=f"|  Host: {github_stats.account_name}", row_num=row)
row += 1
t.gen_text(text=f"|  Commits: {github_stats.total_commits_all_time} total", row_num=row)
row += 1
t.gen_text(text=f"|  Rank: {github_stats.user_rank}", row_num=row)
row += 1
t.gen_text(text="|", row_num=row)
row += 1
t.set_txt_color(COLORS['yellow'])
t.gen_text(text=f"|  Followers: {github_stats.total_followers}", row_num=row)
row += 1
t.set_txt_color(COLORS['red'])
t.gen_text(text=f"|  Stars: {github_stats.total_stargazers}", row_num=row)
row += 1
t.gen_text(text=f"|  Issues: {github_stats.total_issues}", row_num=row)
row += 1
t.set_txt_color(COLORS['green'])
t.gen_text(text=f"|  PRs: {github_stats.total_pull_requests_made}", row_num=row)
row += 1
t.gen_text(text=f"|  Contributed to: {github_stats.total_repo_contributions}", row_num=row)
row += 1
t.gen_text(text="|", row_num=row)
row += 1
t.set_txt_color(COLORS['gray'])
t.gen_text(text="|  Shell: bash", row_num=row)
row += 1
t.gen_text(text="|  Theme: catppuccin-mocha", row_num=row)
row += 1
t.gen_text(text="|  Terminal: github-readme-terminal", row_num=row)
row += 1
t.gen_text(text="|", row_num=row)
row += 1
t.set_txt_color(COLORS['orange'])
t.gen_text(text=f"|  Location: {PERSONAL_INFO['location']}", row_num=row)
row += 1
t.gen_text(text=f"|  Bio: {PERSONAL_INFO['bio']}", row_num=row)
row += 1
t.gen_text(text="|", row_num=row)
row += 1
t.set_txt_color(COLORS['blue'])
t.gen_text(text=f"|  Current: {PERSONAL_INFO['current_project']}", row_num=row)
row += 1
t.set_txt_color(COLORS['white'])
t.gen_text(text=f"|  Fact: {PERSONAL_INFO['fact']}", row_num=row)
row += 1
t.set_txt_color(COLORS['magenta'])
t.gen_text(text=f"|  Fun Fact: {PERSONAL_INFO['fun_fact']}", row_num=row)
row += 1
t.set_txt_color(COLORS['cyan'])
t.gen_text(text=f"|  LinkedIn: {PERSONAL_INFO['linkedin']}", row_num=row)
row += 1
t.set_txt_color(COLORS['green'])
t.gen_text(text=f"|  Tools: {PERSONAL_INFO['tools']}", row_num=row)
row += 1
t.set_txt_color(COLORS['cyan'])
t.gen_text(text="+==========================================================+", row_num=row)

# Add pause at the end (repeat last frame for 2-3 seconds)
# At 3 FPS, 8 frames = ~2.67 seconds pause
for _ in range(8):
    t.clone_frame()

# Set FPS and generate GIF (slower for better readability)
print("Generating GIF...")
t.set_fps(3)
t.gen_gif()

print("Done! Generated terminal.gif")