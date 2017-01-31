# rut1.py
### Calculate probabilities for MTV's dating show *Are You The One?*

#### Background
MTV hosts an amazing show called *[Are You The One?](http://www.mtv.com/shows/are-you-the-one)* where 10 guys and 10 girls have to figure out their "perfect match" (as determined by the show's producers). 

Each episode, the group gets to send one pair to the "Truth Booth" where they learn definitively if that couple is a match or not. Then, at the end of the episode, they pair off into 10 couples and learn *how many* of those couples are perfect matches, but not which ones.

#### Instructions
With some logic and a spreadsheet, you can usually make a lot of conclusions to help you make informed guesses, but `rut1.py` calculates the probability of each potential couple each episode, both after the truth booth and after the "match ceremony."

I've included the data on the truth booth and match ceremony guesses for both seasons 1 and 4. I am also slowly adding season 5 data as it comes in.

To run, simply input `./rut1.py s#`, where `s#` is replaced with the season of your choice (e.g. `s4`). 

**Spoiler warning: Running this script will output the probability results for every episode of the season, which will mean you see the final matches! Don't run if you don't want spoilers for that season!**

#### Dependencies

Both Python 2.x and 3.x will work fine, but the script does use Pandas. If you don't have it, run `pip install pandas`. 

#### Credits

The script is entirely my own, but credit is due to Alex of [Are You The One? Math](http://areuthe.blogspot.com/), a great blog which inspired me to make this. Alex uses a program of his own to calculate the odds during each episode, but since he didn't put up his code (or at least I didn't find it), I decided to make it myself.
