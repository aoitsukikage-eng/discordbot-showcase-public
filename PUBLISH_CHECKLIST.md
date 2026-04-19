# GitHub Publish Checklist

## A. Security Gate

- [ ] Confirm `.env` is not tracked.
- [ ] Confirm no token or key in source.
- [ ] Confirm no personal host paths hardcoded for production.
- [ ] Confirm logs and pid files are excluded.

Recommended local checks:

```bash
rg -n "(api[_-]?key|token|secret|password|DISCORD_BOT_TOKEN|AIza|sk-)" .
rg --files -g "*.env" .
git status
```

## B. Portfolio Completeness

- [ ] README has problem, solution, and architecture summary.
- [ ] Engine private/public boundary is clearly documented.
- [ ] Demo scenarios are reproducible.
- [ ] Metrics file has real values (or marked as planned).

## C. Initial Git Commands

```bash
cd /home/esgcenter0/python/Academic/DiscordBot/discordbot-showcase-public
git init
git add .
git commit -m "chore: initial public showcase structure"

git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

## D. Post-Publish

- [ ] Add repo topic tags (`discord-bot`, `ai-assistant`, `python`).
- [ ] Pin repository on GitHub profile.
- [ ] Add screenshot/demo assets to `assets/`.
