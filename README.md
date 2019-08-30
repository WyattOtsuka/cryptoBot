# cryptoBot

## TODO

 - Gather data required to train the bot
 - Process said data into useable format
    - Split the data in half with half for training and half for testing
    - Both sets should have the local points of significance calculated
    - Similar points of significance cannot be next to each other (ie. peak, peak/valley, valley)

#### Training
 - The training data should be broken into 2 hour segments (or 2 minute segments based on the timescale to act on)
    - The last half of one segment should overlap the first half of the next
 - The first half of the segment is fed into the bot
 - The data is then cylced through each node with new data entering the top node and old data exiting the bottom
 - The last layer should have 3 nodes: 0 (buy), 1 (sell), 2 (wait)
 - The bot is correct if:
    - The next instance is a local peak and the bot said buy
    - The next instance is a local valley and the bot said sell
    - The next instance is neither and the bot said wait
 - Once the data is ran through, the bot is tweaked, and the next segment is loaded in\


#### Testing
 - A faux acount is set up with only the abilities to buy and sell
    - Each transaction should have fees
    - Sales and purchases can fail if the bot doesnt correctly match the market price, to solve this, we can have it make them within 
      a margin of safety in the market price
 - The bot is given $100 dollars to start with
 - After each 24 hours of simulated time, profits are checked
 - A succesfull bot will have turned an average of at least a 0.5% profit daily (~ 300% APR) in a bearish market and have lost less than 0.5% in a bullish market


#### Testing stage 2 
 - The bot is given access to a live market data, but is still unable to make real buy/sell orders
 - The bot is tested for at least 5 days to see if it can also turn a .5% profit
    - It is important to look back at the trading during these days to ensure that the bot can survive in both a bullish and bearish    market
 - If the bot succeeds, It is given permission to go live


#### Implementation
 - The bot faux buy/sell abilities are suplemented with live abilities
 - If the bot does not have a an average of at least a .5% profit daily (bullish) and less than 0.5% loss (bearish), it is taken back for more training

#### Future plans
 - Increase capital to increase profits
    - Once the bot is well proven in both markets, we should begin to reach out to garner more capital
    - The investor will take most of the profits, while we would take a cut of them
    - Potential problems:
        - Markets behave differently for different quantities of sales. Large transactions take longer, to be fullfilled an thus, should be within a greater saftey margin
        - Lack of diversity could create a largescale failure if one market crashes. To avoid this, we should checkpoint the bot, and train it against other markets as well so that we can diversify our investments
        - At the time of the investment, the market could be at a peak and about to fall. This would be catastrophic, and as such, we would need to be extremely careful about when we look for investors
