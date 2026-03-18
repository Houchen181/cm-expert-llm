# Discord Community Setup Guide

This guide helps you set up a Discord community server for CondensAI users and contributors.

## Why Discord?

A Discord server provides:
- Real-time help and troubleshooting
- Community building among physics researchers
- Announcement channel for updates
- Casual discussion about LLM + physics applications

## Setup Steps

### 1. Create the Server

1. Open Discord and click **"+"** in the server list
2. Choose **"Create My Own"**
3. Select **"For a community"** or **"For a club or community"**
4. Name: **CondensAI**
5. Add description: "Domain-expert LLM toolkit for condensed matter physics"
6. Upload the CondensAI logo (from `docs/logo.svg` - convert to PNG first)
7. Click **Create**

### 2. Set Up Channels

Create the following text channels:

| Channel | Purpose |
|---------|---------|
| `#welcome` | Introduction and rules |
| `#announcements` | Project updates (read-only for most users) |
| `#general` | General discussion |
| `#help-troubleshooting` | Installation and usage help |
| `#physics-discussion` | Condensed matter physics topics |
| `#model-training` | Training tips, configs, results |
| `#showcase` | Users share their domain experts |
| `#development` | Contributing code, PRs, feature requests |

### 3. Set Up Roles

Create these roles:

| Role | Color | Permissions |
|------|-------|-------------|
| `@CondensAI Team` | Blue | Manage channels, kick/ban |
| `@Moderator` | Green | Manage messages, mute |
| `@Contributor` | Purple | Special mention for code contributors |
| `@Researcher` | Gold | Verified physics researchers |
| `@Member` | Default | Default role |

### 4. Configure Welcome Screen

In **Server Settings** → **Welcome Screen**:
- Enable welcome screen
- Add channel recommendations: `#welcome`, `#help-troubleshooting`, `#announcements`
- Write a friendly welcome message

### 5. Set Up Verification

In **Server Settings** → **Safety Setup**:
- Enable verification level (Medium recommended)
- Set up AutoMod for spam protection

### 6. Create Welcome Message

In `#welcome`:

```
Welcome to the CondensAI Discord! 🦀

This is a community for researchers, students, and enthusiasts interested in building domain-expert LLMs for condensed matter physics.

**Getting Started:**
1. Read the rules below
2. Introduce yourself in #general
3. Check out #announcements for latest updates
4. Need help? Visit #help-troubleshooting

**Resources:**
- GitHub: https://github.com/Houchen181/CondensAI
- Documentation: https://github.com/Houchen181/CondensAI/tree/main/docs
- arXiv: [link to paper when available]

Please be respectful and follow our Code of Conduct. Happy physics-ing! 🚀
```

### 7. Get Your Invite Link

1. Go to **Server Settings** → **Invites**
2. Click **Create Invite**
3. Set to never expire (or long duration)
4. Copy the link for your README

## Add to README

Once you have the invite link, add this badge to your README:

```markdown
[![Discord](https://img.shields.io/discord/123456789?logo=discord&logoColor=white)](https://discord.gg/YOUR_INVITE)
```

Replace `123456789` with your actual server ID (found in Server Settings → Widget).

## Best Practices

- **Be active**: Respond to questions within 24-48 hours
- **Pin important messages**: Rules, FAQs, getting started guide
- **Regular updates**: Post in #announcements when new releases drop
- **Encourage showcase**: Highlight cool domain experts users build
- **Office hours**: Consider weekly/monthly voice chat Q&A sessions

---

*Template created for CondensAI community building*
