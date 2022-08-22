# HigherLower-Spotify

The Higher Lower Game is an online game where one guesses which of two items has more global monthly searches on Google. I made a spin-off game based on Spotify songs. My game takes the "Top 50 - USA" playlist which contains the 50 most streamed songs in the U.S. on spotify and makes users guess which song is more popular. Spotify does not make the total views of a song public, but instead gives developers a "popularity rating" for each song. This data which comes as a value from 0 to 100 (the higher the value, the more popular a song is), is something Spotify develops through an algorithm which they say is mainly based on how many streams a song has and how recent those streams are. More information can be found in the documentation of Spotify's developer page (https://developer.spotify.com/documentation/web-api/reference/#/operations/get-several-tracks). It was interesting to learn that the popularity rating of songs does not accurately match the ranking of the songs in the "Top 50 - USA" playlist. This is because the popularity rating is not just based on U.S. streams, but rather the global streams. I noticed this as Hispanic songs (Bad Bunny's album "Un Verano Sin Ti" came out around the time I was making this game) would often have extremely high popularity ratings even if they were not highest on the charts. This worked out in my favor though as it becomes more difficult to cheat if one were to have the playlist open while playing.

I built this game using Flask, the Spotify API, HTML, CSS, and Javascript. I used this project as an excuse to get familiar with these languages and frameworks. In order to play the game, you need to run the app.py file. Prior to this, however, you need go to data.py and click the link in the comment. Then, you need to scroll down and press "Get Token" and then "Request Token." Then, copy the OAuth Token and paste it inside the string for the "spotify_token" variable. If you do not do these step, the code will error out upon hitting "Play." This token needs to be refreshed every hour. I could create a program that refreshes the token automatically (in fact, I actually did for another project), but this would lead to more hassle for the user who I assume just wants to try the game out a few times. The refresh program requires users to have a spotify account and paste an id and secret code associated with their account into another file.
