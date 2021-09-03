# Mark multiple Spotify Podcast Episodes as played
I wanted to switch my podcasting over to Spotify and I was really frustrated that I couldn't mark episodes as played in mass. So I wrote this quick and dirty tool to do this through the Spotify Web API. There is probably a much more elegant way to do this...

* Get the show ID from either the Spotify webplayer or the share option in the desktop app
* Get the episode ID that you want to start marking as played from. This tool will start with this episode and mark it and all the older ones as played.
* Get an an OAuth Token from the Spotify Developers Console (https://developer.spotify.com/console/)
   * Make sure you include the modify **user-modify-playback-state** permission in this token
* Figure out if the show's episodes return in ascending or descending order


## TO DO
* Figure out why some shows return in ascending order and some shows return in descending order
* Figure out why 'duration_ms' doesn't match the actual duration of the episode. I think Spotify is tacking on an ad at the end of episodes. We have to play the episode to the end to get it to be marked as played