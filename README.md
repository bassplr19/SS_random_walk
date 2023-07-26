# SS_random_walk
Taking your SS data (collection dates and monthly check) it runs many iterations to see when you should start collecting SS

Retirement Planning with Random Walks
This code simulates the growth of a retirement portfolio over time using a random walk. The user inputs their desired retirement age, the year they expect to die, and the monthly Social Security benefits they expect to receive at different retirement ages. The code then runs 200 simulations of the portfolio's growth, and outputs the mean, median, and standard deviation of the final portfolio value.

How to use the code
Clone the repository to your computer.
Install the required Python libraries: numpy, pandas, random, yfinance, pyinputplus.

The code will prompt you to enter your desired retirement age, the year you expect to die, and the monthly Social Security benefits you expect to receive at different retirement ages. The code will then run 200 simulations of the portfolio's growth, and output the mean, median, and standard deviation of the final portfolio value.

Example output
What year will you turn 62? 2045
What year to plan until? 2067
What will your monthly check be at 62? 2170
What will your monthly check be at 67? 3099
What will your monthly check be at 70? 3848

Mean: 1,082,627.75
Median: 1,074,352.25
+Std Dev: 132,388.25
-Std Dev: 124,002.75

This output shows that, in the 200 simulations, the final portfolio value had a mean of \$1,082,627.75. The median final portfolio value was \$1,074,352.25, and the standard deviation was \$132,388.25.

License
This code is licensed under the MIT License.

Author
This code was written by Josh Zagorski.
