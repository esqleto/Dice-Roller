# 🎲Dice Roller 
 
 A python program for rolling "Dices" on a "Tray".

 This was originally a university assignment but more features were and will be added independently of that.

 ## Dependencies

 - [`pyenv`](https://github.com/pyenv/pyenv)-Python version manager
    - [`Python-1.12.3`](https://www.python.org/downloads/) installed

## Usage

The program will start you off with 100 Dices on the tray, all with the value of 1.

On the terminal window you will be prompted to input the amount of `Force` you want to apply on the tray. The value must be Between `0.1 and 10`:

    Type the amount of force applied(between 0.1 and 10):

After that's done you'll be prompted to input the amount of `Times` the tray should be shaken.

    Type the amount of times that the tray should be shaken:

After this the program will create 2 files one named `CSVArray.csv` and another named `SumChart.csv`.

- `CSVArray.csv`'s contents can be read using [`Calc`](https://www.libreoffice.org/discover/calc/) or [`Excel`](https://www.microsoft.com/en-us/microsoft-365/excel) as a spreadsheet.
  
  - The data should be `100 rows` `representing the dices` and `a number of columns` `representing the amount of shakes`. 
  
  - According to the amount of `Force` a percentage of the dices will be rolled and gain a `random value between 1 and 6`, all dices unaffected `will remain with the value of 1.`
  - At the bottom of the document you'll find the `Sum of all dices within a column`. Bellow that you'll find the `Median` , `Mean` and `Mode` of all  the sums.
  
  - How it should look like:

    - Top:
    ![top](https://cdn.discordapp.com/attachments/1243428190660071557/1243428225414205491/image.png?ex=66517046&is=66501ec6&hm=5f9a602e9ec37eb2230b8200941209654c15e9aead523f9b98d05e6d80ffe10d&) 
    - Bottom:
      ![bottom](https://cdn.discordapp.com/attachments/1243428190660071557/1243428381362749490/image.png?ex=6651706b&is=66501eeb&hm=8d0e47eb61a6ad53c09ab4b55b58fbdcd089df1a62229369f460696fc1ae8dbc&) 





- `SumChart.csv` contains the `Sums of all dices in each column.`
  - This file exists only to create a graph within whatever software you chose to open the file with.
  - How it should look like:
    
    ![sums](https://cdn.discordapp.com/attachments/1243428190660071557/1243434216373616650/image.png?ex=665175db&is=6650245b&hm=a933cd148f0b5a1e4104445caa3dc5a3037921d2b46f2a7689693e4fd9b53cb4&) 
  - Example in graph form: 
  ![graph](https://cdn.discordapp.com/attachments/1243428190660071557/1243435350152450109/image.png?ex=665176e9&is=66502569&hm=4890148df9bd6ea346d61b5dc0ffd28284248838bf3ab7eb2fdaf5b1e0500bbb&)
  