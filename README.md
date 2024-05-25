# 🎲Dice Roller 
 
 A python program for rolling "Dices" on a "Tray".

 This was originally a university assignment but more features were and will be added independently of that.

 ## Dependencies

  - [`Python-1.12.3`](https://www.python.org/downloads/) installed

## Usage

The program will start you off with 100 Dices on the tray, all with the value of 1.

On the terminal window you will be prompted to input the amount of force you want to apply on the tray. The value must be Between 0.1 and 10:

    Type the amount of force applied(between 0.1 and 10):

After that's done you'll be prompted to input the amount of times the tray should be shaken.

    Type the amount of times that the tray should be shaken:

<hr>

After this the program will create 2 files one named `CSVArray.csv` and another named `SumChart.csv`.

- `CSVArray.csv`'s contents can be read using [`Calc`](https://www.libreoffice.org/discover/calc/) or [`Excel`](https://www.microsoft.com/en-us/microsoft-365/excel) as a spreadsheet.
  
  - The document should contain be 100 rows representing the dices and a number of columns representing the amount of shakes. 

  - According to the amount of`force typed a percentage of the dices will be rolled and gain a random value between 1 and 6, all dices unaffected will remain with the value of 1.

  - At the bottom of the document you'll find the sum of all dices in each a column. Bellow that you'll find the median , mean and mode of all  the sums.

- `SumChart.csv` contains the sums of all dices in each column.
  - This file exists only to create a graph within whatever software you chose to open the file with.