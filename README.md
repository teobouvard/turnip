# turnip

I often need to SSH into my home box when I'm travelling, but my ISP wants me to pay to have a static ip.
`turnip` helps me solve this problem, by notifying me of IP changes on Discord.

## Usage

- Install `python-discord`
- [Create a Discord bot](https://discord.com/developers/applications), give it message permissions
- Run `turnip` to check if the bot correctly sends a message to the desired channel containing your public IP
- Copy `turnip` to `~/.local/bin` or any directory in your path
- Edit `turnip.service` to specify the path to the script and its arguments
- Link turnip unit file and timer `systemctl --user link $(readlink --canonicalize turnip.*)`
- Enable the timer `systemctl --user enable turnip.timer --now`
- Never get locked out of your machine by your ISP again

## FAQ

Q: Discord ? Why not email ?  
A: What is this, 1971 ?

Q: Systemd ? Why not cron ?
A: What is this, 1975 ?
