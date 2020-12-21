# turnip

I often need to SSH into my home box when I'm travelling, but my ISP wants me to pay to have a static ip.
`turnip` helps me solve this problem, by notifying me of IP changes on Discord.

## Usage

- Install `discord.py`
- [Create a Discord bot](https://discord.com/developers/applications), give it message permissions
- Run `turnip` to check if the bot correctly sends a message to the desired channel containing your public IP
- Add the script to your path
- Create a cron job to run this script every once in a while
- Never get locked out of your machine by your ISP again

## Example cron job

```bash
*/10 * * * * turnip --token your_discord_bot_token --server server_name --channel channel_name
```

## FAQ

Q: Discord ? Why not email ?
A: Does this look like 1971 to you ?
